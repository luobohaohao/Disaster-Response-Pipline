import json
import plotly
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
import joblib
from sqlalchemy import create_engine
import pickle
import numpy as np

app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens

# load data
engine = create_engine('sqlite:///data/DisasterResponse.db')
df = pd.read_sql_table('message_categories', engine)

# load model
model = pickle.load(open("models/classifier.pkl", "rb"))

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    category_names = df.iloc[:,4:].columns
    category_above0_count= df[df.iloc[:,4:]!=0].iloc[:,4:].count().values
    category_max= np.max(df.iloc[:,4:], axis=0).values
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        # GRAPH 1 - genre graph
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        
        # GRAPH 2 - category graph for count >0 values  
        {
            'data': [
                Bar(
                    x=category_names,
                    y=category_above0_count
                )
            ],

            'layout': {
                'title': 'how many values>0 for  Message Categories',
                'yaxis': {
                    'title': "count"
                },
                'xaxis': {
                    'title': "Category",
                    'tickangle': 36
                }
            }
        },
        # GRAPH 3 - category graph for max values  
        {
            'data': [
                Bar(
                    x=category_names,
                    y=category_max
                )
            ],

            'layout': {
                'title': 'category graph for max values',
                'yaxis': {
                    'title': "max_value"
                },
                'xaxis': {
                    'title': "Category",
                    'tickangle': 36
                }
            }
        }
        
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
