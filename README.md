# Disaster-Response-Pipline
# Table of Contents
[Project overview](#project-overview)

[Dependencies](#dependencies)

[Folder Structure](#folder-structure)

[Instructions](#instructions)

[Execution Results](#execution-results)

[Model Evaluation](#model-evaluation)

# Project overview
In Udacity Data Scientist course, I've learned and built on my data engineering skills. In this project, I'll apply these skills to analyze disaster data from Figure Eight to build a model to classify disaster messages.These data all downloaded from workspace in Udacity data scientist course.All the steps I tried to follow the project specification:

1.Processing data, building an ETL pipeline to extract data from source, clean the data and save them in a SQLite DB

2.Build a machine learning pipeline to train the which can classify text message in various categories

3.Run a web app which can show model results in real time.You can also check the visualization result in the web

# Dependencies
1.Python 3

2.Machine Learning Libraries: NumPy, Pandas, Sciki-Learn

3.Natural Language Process Libraries: NLTK,re

4.SQLlite Database Libraqries: SQLalchemy

5.Model Loading and Saving Library: os,Pickle

6.Web App and Data Visualization: Flask, Plotly

7.Others:sys

# Folder Structure
![image](https://user-images.githubusercontent.com/30916036/137128615-7aba1f2e-e77e-40be-b356-37057870289b.png)

# Instructions
1. Run the following commands in the project's root directory to set up your database and model.
   - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
   - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the `python app/run.py` command in the app's directory to run your web app.

3. Go to your local host to check your result

# Execution Results
1.When I opened my local host website,firstly I saw the visulization result
![image](https://user-images.githubusercontent.com/30916036/137123772-14d56925-2fea-4674-a5a5-9fb5cfec05f9.png)

2.When I typed a text message in the search box,it showed the classified result.The green highlighted categories are the predicted categories for this message.
![image](https://user-images.githubusercontent.com/30916036/137180443-751ae67c-2a92-497e-8040-3db2e167f956.png)

# Model Evaluation
Here is the model evaluation result for each category in test datasets.
![image](https://user-images.githubusercontent.com/30916036/137162505-c232a77a-7c68-4b6d-bdea-c9031d0aa235.png)


