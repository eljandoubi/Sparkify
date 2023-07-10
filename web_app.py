import json
from pyspark.sql import SparkSession, Row
from pyspark.ml import PipelineModel
import gradio as gr


spark = SparkSession \
    .builder \
    .appName("Sparkify") \
    .getOrCreate()

cols=["history","artists","songs","userAgent","location","gender"]

with open('exemples.json', 'r') as f:
    examples = json.load(f)
    
examples=[[example[col] for col in cols] for example in examples]

pipe=PipelineModel.load("bestModel")

def predictor(*arg):
    
    dic=dict(zip(cols,arg))
    
    for key in ["history","artists","songs"]:
        dic[key]=dic[key].split(",")
    
    d=spark.createDataFrame([Row(**dic)])
    pred=pipe.transform(d).collect()[0].probability
    
    return dict(zip(['not churn','churn'],pred))#[1,0]))#
	

inputs=[gr.Text(label="history",placeholder="Type in the user history page by page separated by coma"),
        gr.Text(label="artists",placeholder="Type in the user list of artists by page separated by coma"),
        gr.Text(label="songs",placeholder="Type in the user list of songs by page separated by coma"),
        gr.Text(label="userAgent",placeholder="example: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0"),
        gr.Text(label="location",placeholder="example: Bakersfield, CA"),
        gr.Radio(label="gender",choices=["F","M","None"],value="None"),
        ]

gr.Interface(fn=predictor,inputs=inputs,outputs="label",
             title="Sparkify",examples=examples).launch(inbrowser=True,share=True)

spark.stop()