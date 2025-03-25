# Text_summarizer_nlp_project

<p align ="center"><img src="bot.gif" width=50%></p>



# Brief explanation of the application
## Information 📱
This web application utilizes [Hugging Face Transformers](https://huggingface.co/transformers/task_summary.html#summarization) 🤗 to leverage a pre-trained summarisation pipeline to start **summarising** content. This web application excels in summarizing news articles. 

## Features 💻
* Summarize your text up to 500 words!
* Input the desired text that needed to summarize.
* See the summary of text afterwards!

## Hugging Face Transformers 🤗
Hugging Face Transformers provides thousands of pretrained models to perform tasks on texts such as classification, information extraction, question answering, summarization, translation, text generation, etc in 100+ languages. Its aim is to make cutting-edge NLP easier to use for everyone.



## Prerequisites:
1. Python.
2. Machine learning.
3. NLP(Natural Language Processing).
4. Github Action.
5. Aws pipelines.
6. Transformer.
7. OOPS concepts.
8. Pytorch.
9. Flask.

# Installation Instructions
1. Create a anaconda environment. visit https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
2. Clone the repo.
3. git clone https://github.com/Shivam-Shane/Text_summarizer_nlp_project
4. run Command pip install -r requirements.txt
5. run main.py
6. run app.py
7. open https://localhost:1001 in browser.
8. Input the desired text and see the result.



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: a url like thing.

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID= # you will found in Aws while creating user account for sepecif user account

    AWS_SECRET_ACCESS_KEY= # you will found in Aws while creating user account for sepecif user account

    AWS_REGION = us-east-1 # there region i which your cloud hosted server

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = text_summarizera/or the name you define.
## Contribution
Feel free to fork this project, submit pull requests, or report issues. Contributions to enhance the functionality and make the system more robust are welcome!

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE file for details.

## Contact

For questions, suggestions, or support, reach out at 
- **sk0551460@gmail.com** 
- **shivam.hireme@gmail.com**.

## Support the Project

Help support continued development and improvements:

- **Follow on LinkedIn**: Stay connected for updates – [LinkedIn Profile](https://www.linkedin.com/in/shivam-hireme/)
- **Buy Me a Coffee**: Appreciate the project? [Buy Me a Coffee](https://buymeacoffee.com/shivamshane)
- **Visit my Portfolio**: [Shivam's Portfolio](https://shivam-portfoliio.vercel.app/)
