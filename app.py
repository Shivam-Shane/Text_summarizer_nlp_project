from flask import Flask, request, render_template
from logger import logging
from src.textsummarizernlpproject.pipeline.prediction import PredictPipelineClass

logging.info("Starting application Text Summarization")
application = Flask(__name__)

@application.route('/',methods=['GET', 'POST'])
def index():
    processed_data=None
    if request.method == 'POST':
        logging.info(f"Starting prediction")
        input_data = request.form.get('input_data', '')
        processed_data = process_data(input_data)
        return render_template('index.html', processed_data=processed_data)
    
    return render_template('index.html')

def process_data(summarization_data):
    """
    Process(Summarization) the given data
    Args: 
        input data that needs to be processed
    Returns:
        Processed data
    """
    obj=PredictPipelineClass()
    value=obj.predict(summarization_data)
    return value
        
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8082,debug=False)
