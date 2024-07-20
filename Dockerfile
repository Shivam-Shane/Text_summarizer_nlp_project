FROM python:3.11-slim-buster
LABEL image="text_summarization"
# Set the working directory
WORKDIR /application
# coping all data to working directory application
COPY . /application  
# updating the linux os
RUN apt update -y && apt install awscli -y
RUN apt install vim
# installing all the dependencies of project
RUN pip install uv && pip install -r requirements.txt
# exposing port 1001 for external access
EXPOSE 8082
# at last running the application
CMD ["sh", "-c", "python3 /application/main.py; python3 /application/app.py"]