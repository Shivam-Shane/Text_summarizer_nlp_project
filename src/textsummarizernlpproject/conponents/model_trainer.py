from datasets.load import load_from_disk
from transformers import TrainingArguments,Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from datasets import load_dataset,load_from_disk
import torch
import os
from src.textsummarizernlpproject.entity import ModelTraninerConfig
from logger import logging

class ModelTrainer:
    def __init__(self,config:ModelTraninerConfig):
        self.config = config

    def train(self):
        """ Train the model
        Args:
            Model Name: The name of the model
            Model Arguments: Arguments
            Dataset: The dataset to train on
            Path: The path to save the trained model and its tokens
        returns:
            None
        """
        logging.info(f"Inside {self.__class__.__name__}.{self.train.__name__}")

        device="cuda" if torch.cuda.is_available() else "cpu"
        tokenizer=AutoTokenizer.from_pretrained(self.config.model_name)
        model=AutoModelForSeq2SeqLM.from_pretrained(self.config.model_name).to(device)
        seq2seq_data_collator=DataCollatorForSeq2Seq(tokenizer,model)
        dataset_newsdata=load_from_disk(str(self.config.data_path))
                
        trainer_args=TrainingArguments(
                output_dir=str(self.config.root_model_dir),
                num_train_epochs=self.config.num_train_epoch,
                warmup_steps=self.config.warmup_steps,
                # pre_device_train_batch_size=self.config.pre_device_train_batch_size, # type: ignore
                weight_decay=self.config.weight_decay,
                logging_steps=self.config.logging_steps,
                evaluation_strategy=self.config.evaluation_strategy,
                eval_steps=self.config.eval_steps,
                save_steps=self.config.save_steps,
                gradient_accumulation_steps=self.config.gradient_accumulation_steps
                )
        trainer=Trainer(model=model,args=trainer_args,tokenizer=tokenizer,
                        data_collator=seq2seq_data_collator,
                        train_dataset=dataset_newsdata['train'],        # type: ignore
                        eval_dataset=dataset_newsdata['validation']     # type: ignore
                        )
        logging.info(f"Saving the model and tokens")                
        model.save_pretrained(os.path.join(self.config.root_model_dir,"Newsdataset"))
        tokenizer.save_pretrained(os.path.join(self.config.root_model_dir,"Tokenizer"))
        logging.info(f"End of {self.__class__.__name__}.{self.train.__name__}")        