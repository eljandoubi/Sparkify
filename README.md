# Sparkify


## Table of Contents
1. [Description](#description)
2. [Files Descriptions](#files)
3. [Getting Started](#getting_started)
	1. [Dependencies](#dependencies)
	2. [Installation](#installation)


<a name="descripton"></a>
## Description

Use case:
Sparkify, an innovative startup, delivers music streaming services to users across the United States. Our users engage with the service daily, either through the free tier with intermittent advertisements or the premium subscription model, which offers ad-free music at a fixed monthly cost. Users have the flexibility to upgrade, downgrade, or cancel their service as desired, making it crucial for us to ensure their satisfaction. Each interaction a user has with our service, such as playing songs, logging out, liking tracks with a thumbs-up, listening to ads, or changing their subscription level, generates valuable data. This data holds key insights for maintaining user happiness and driving Sparkify's success. As members of the data team, our mission is to accurately predict which users are likely to churn, either by downgrading from the premium tier to the free tier or canceling their subscription altogether. By identifying these users in advance, Sparkify can proactively offer them discounts and incentives, potentially saving millions in revenue for the business.

As the volume of data in the log file has exceeded the memory capacity of standard desktop computers, Sparkify has adopted the distributed file system Apache Spark™. To analyze this large dataset, Udacity™ provides the complete 12GB dataset on AWS™ S3, and you can leverage AWS or IBM™ Cloud to run a Spark cluster in the cloud.

The project aim is to build a Natural Language Processing (NLP) model capable of predicting whether a user will churn or not on a real time basis.

This project is divided in the following key sections:

1. Processing data, building an ETL pipeline to extract data from source, clean the data and save them.
2. Build a machine learning pipeline for training a model capable of predicting whether a user will churn or not.
3. Run a web app which can show model results in real time.

<a name="files"></a>
## Files Descriptions 

The files structure is arranged as below:

	- README.md: read me file.
 	- requirement.txt: dependencies list
	- web_app.py: gradio file to run the app
	- bestModel.zip: the compressed file of MLlib in PySpark.
	- exemples.json: examples of inputs for the web app.
	- Sparkify.ipynb: ETL process and ML & NLP pipeline notebook.


<a name="getting_started"></a>
## Getting Started

<a name="dependencies"></a>
### Dependencies
* Python 3.6+
* Big data and Machine Learning Libraries: PySpark
* Web App: Gradio
* Jupyter: ipython
* Boto3: the AWS SDK for Python

<a name="installation"></a>
### Installation
1. Clone the git repository:

```git clone https://github.com/eljandoubi/Sparkify.git```

2. Change directory

```cd Sparkify```

3. Create conda environment

```conda create -n "Sparkify" python=3.6```

4. Install dependencies

```pip install -r requirements.txt```

5. You can run the following commands in the project's directory to set up the database, train model and save the model.
You need first to set your AWS key id and secret key.
    
```ipython Sparkify.ipynb```

6. To run your web app, execute the following command.

```python web_app.py```
