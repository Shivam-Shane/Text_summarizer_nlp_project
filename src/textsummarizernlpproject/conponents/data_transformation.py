import os
from tabnanny import verbose
from src.textsummarizernlpproject.entity import DataTransformationConfig
from logger import logging
from transformers import AutoTokenizer
from datasets import load_dataset

class DataTransformations:
    def __init__(self, config: DataTransformationConfig):
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.__init__.__name__}")
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.convert_examples_to_features.__name__}")
        """Converting a list of examples/Datasets into features
        Args:
            dataset
        Returns: input_id, attention_mask, labels
        """
        input_encoding = self.tokenizer(example_batch['article'],max_length=1024,truncation=True)
        target_encoding = self.tokenizer(text_target=example_batch['highlights'],max_length=128,truncation=True)

        logging.info(f"Returning the transformed features") 
        return {
            'input_ids':input_encoding['input_ids'],
            'attention_mask':input_encoding['attention_mask'],
            'labels':target_encoding['input_ids'],
        } 
           
    def convert(self):
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.convert.__name__}")
        dataset_newsdata=load_dataset(str(self.config.data_path))
        dataset_newsdata_pt=dataset_newsdata.map(self.convert_examples_to_features,batched=True)
        dataset_newsdata_pt.save_to_disk(os.path.join(self.config.root_tradata_dir,"Newsdataset")) # type: ignore