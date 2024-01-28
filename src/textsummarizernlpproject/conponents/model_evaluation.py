from datasets.load import load_from_disk,load_metric
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
import torch 
import pandas as pd
from tqdm import tqdm
from src.textsummarizernlpproject.entity import ModelEvaluationConfig
from logger import logging

class Model_Evaluation():
        def __init__(self,config:ModelEvaluationConfig):
            logging.info(f">>>> Inside {self.__class__.__name__}.{self.__init__.__name__}")
            self.config = config

        def generate_batch_sized_chunks(self,
                    list_of_element,
                    batch_size):
              """
              Split the dataset into chunks of batches that we can process simultaneously
              yield successive batch-sized chunks from the list of elements
                Args:
                    List_of_Element: dataset to be processed
                    Batch_size: int[size of batch that will be processed]    
                Returns:
                    None
              """
              logging.info(f">>>> Inside {self.__class__.__name__}.{self.generate_batch_sized_chunks.__name__}")
              for i in range(0, len(list_of_element),batch_size):
                yield list_of_element[i:i+batch_size]

        def calculate_metric_on_test(self,
                    dataset,
                    metric,
                    model,
                    tokenizer,
                    device="cuda" if torch.cuda.is_available() else "cpu",
                    batch_size=16,
                    column_text='article',
                    column_summary='highlights'):
            
            logging.info(f">>>> Inside {self.__class__.__name__}.{self.calculate_metric_on_test.__name__}")

            article_batchs=list(self.generate_batch_sized_chunks(dataset[column_text],batch_size=16))
            target_batchs=list(self.generate_batch_sized_chunks(dataset[column_summary],batch_size=16))
            logging.info("Done creating batch")

            for article_batchs,target_batchs in tqdm(zip(article_batchs,target_batchs),total=len(article_batchs)):
                 inputs=tokenizer(article_batchs,max_length=1024,truncation=True,padding='max_length',return_tensors="pt")
                 
                 with torch.no_grad():
                        summaries=model.generate(input_ids=inputs['input_ids'].to(device),
                                                      attention_mask=inputs['attention_mask'].to(device),
                                                      length_penalty=0.8,num_beams=2,max_length=200
                                                      )

                 decoded_summaries =[tokenizer.decode(s,skip_special_tokens=True,clean_up_tokenization_space=True) for s in summaries]
                 decoded_summaries=[d.replace(""," ") for d in decoded_summaries]
                 metric.add_batch(predictions=decoded_summaries,references=target_batchs)

            score=metric.compute()
            logging.info(f"Returing model score")
            return score     

        def evaluate(self):
             """
             Evaluate the model performance using rough metrics
                Args: 
                    None
                Returns: 
                    None
             """
             logging.info(f">>>> Inside {self.__class__.__name__}.{self.evaluate.__name__}")
             device="cuda" if torch.cuda.is_available() else "cpu"
             tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)   
             model=AutoModelForSeq2SeqLM.from_pretrained(self.config.model_name).to(device)
             dataset_newsdata=load_from_disk(str(self.config.data_path))                
             rouge_names=["rouge1", "rouge2", "rougeL","rougeLsum"]
             rouge_metric=load_metric('rouge')
             logging.info("Running calulate metric")

             score=self.calculate_metric_on_test(           
                    dataset_newsdata['test'][0:10],
                    rouge_metric,
                    model,
                    tokenizer,
                    batch_size=16,
                    column_text='article',
                    column_summary='highlights'
             )
             rouge_dict = dict((rn,score[rn].mid.fmeasure) for rn in rouge_names)
             data=pd.DataFrame(rouge_dict,index=['News'])
             data.to_csv(self.config.metric_file,index=False)      