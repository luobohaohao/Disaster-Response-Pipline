# Disaster-Response-Pipline
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
![image](https://user-images.githubusercontent.com/30916036/137128224-3b4af8f6-c4ad-46f1-941a-d85201c2d29d.png)

- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py     #script to run the ETL
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py   #script to build the model
|- classifier.pkl  # saved model 


- Screenshot
|- process_data_success   #When successfully run process_data.py it showed this screenshot
|- train_classifier_success  #when successfully run train_classifier.py it showed this screenshot
|- run_success #when successfully run run.py it showed this screenshot
|- visulization.   #the visualization in website
|- classifier_result  # the classifier result in website
|- model_evaluation # the evaluation result for the model in test dataset

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

2.When I typed a text message in the search box,it showed the classified result.The green highlighted category is the classification for this message.
![image](https://user-images.githubusercontent.com/30916036/137123945-c685fecd-0da6-4678-a32b-0ebde491cdae.png)

# Model Evaluation
Here is the model evaluation result for each category in test datasets.
![image](https://user-images.githubusercontent.com/30916036/137124192-2a55673f-1f5d-426f-a747-93d7ed8e2af8.png)

