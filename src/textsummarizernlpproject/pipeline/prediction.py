from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from transformers import pipeline,AutoTokenizer

class PredictPipelineClass:
    def __init__(self):
        self.config= ConfigurationManager().get_model_evaluation_config()
    def predict(self,text):
            """
            Summarize the data and return
            Args:
                text: string(that needs to be summarize)
            Returns:
                text: string(Summarized text)    
            """
            logging.info(f">>>> Inside {self.__class__.__name__}.{self.__init__.__name__}")
            logging.info(f"Starting prediction")
            tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            gen_kwags={'length_penalty':0.8,'num_beams':10,"max_length":500}
            pipe=pipeline("summarization",model=str(self.config.model_name),tokenizer=tokenizer)
            output=pipe(text,**gen_kwags)[0]["summary_text"].replace("<n>", " ") #type: ignore
            logging.info("Returing result")
            return output