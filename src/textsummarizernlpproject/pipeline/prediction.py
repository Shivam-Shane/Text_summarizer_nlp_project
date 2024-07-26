from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from transformers import pipeline,AutoTokenizer

class PredictPipelineClass:

    # class variables
    _runonce = False
    _tokenizer = None
    _gen_kwargs = None
    _pipeline=None
    def __init__(self):
        self.config= ConfigurationManager().get_model_evaluation_config()
        if not PredictPipelineClass._runonce: # making sure we don't call this twice reducing workload time
            try:
                PredictPipelineClass._tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
                # tokenizer
                PredictPipelineClass._pipeline=pipeline("summarization",model=str(self.config.model_name),tokenizer=PredictPipelineClass._tokenizer)
                # pipeline
                PredictPipelineClass._gen_kwargs={'length_penalty':1.8,  # less than 1.0 encourages generation of shorter summaries.
                        'num_beams':10, #beams improves quality of summary considering potential sequences
                        "max_length":500, # max length of summary
                        'min_length': 100, # min length of summary
                        'no_repeat_ngram_size': 3, # no repeat of ngram size in summary
                        } 
                PredictPipelineClass._runonce = True
                logging.info(f"Model and tokenizer loaded successfully")
            except Exception as e:
                 logging.error(f"Error initializing PredictPipelineClass: {e}")
                 raise e
        self.pipeline = PredictPipelineClass._pipeline
        self.tokenizer = PredictPipelineClass._tokenizer
        self.gen_kwargs = PredictPipelineClass._gen_kwargs
        logging.info(f"Predict pipeline class initialized successfully")

    def predict(self,text):
            """
            Summarize the data and return
            Args:
                text: string(that needs to be summarize)
            Returns:
                text: string(Summarized text)    
            """
            logging.info(f">>>> Inside {self.__class__.__name__}.{self.predict.__name__}")
            logging.info(f"Starting prediction")
            try:
                 
                output=self.pipeline(text,**self.gen_kwargs)[0]["summary_text"].replace("<n>", " ") #type: ignore
                logging.info("Returning result")
                return output
            except Exception as e:
                 logging.error(f"Error in predicting: {e}")
                 raise e
# ----------------------------------------------------------------------------------------------------------------