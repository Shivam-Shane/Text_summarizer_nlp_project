FROM python:3.11-slim-buster
LABEL image="text_summarization"
# Set the working directory
WORKDIR /app 
# coping all data to working directory app
COPY . /app  
# updating the linux os
RUN apt update -y && apt install awscli -y
# installing all the dependencies of project
RUN apt-get update && pip install -r requirements.txt
# exposing port 1001 for external access
EXPOSE 1001:1001
# at last running the application
CMD ["sh", "-c", "python3 /app/main.py; python3 /app/app.py"]