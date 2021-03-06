import sys
import os
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger','stopwords'])
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
from sqlalchemy import create_engine
from sklearn.pipeline import Pipeline
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import classification_report
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, AdaBoostClassifier
import re
import pickle


def load_data(database_filepath):
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('message_categories', engine)
    df.drop('original',axis=1)
    df=df.dropna()
    X = df['message']
    df['related']=df['related'].map(lambda x: 1 if x == 2 else x)
    Y = df.iloc[:,4:]
    category_names = Y.columns
    return X,Y,category_names
    


def tokenize(text):
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    stop_words = stopwords.words("english")
    #tokenize
    words = word_tokenize (text)
    #stemming
    stemmed = [PorterStemmer().stem(w) for w in words]
    #lemmatizing
    words_lemmed = [WordNetLemmatizer().lemmatize(w) for w in stemmed if w not in stop_words]
    return words_lemmed


def build_model():
    pipeline_red_dim =Pipeline([
            ('vect', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer()),
            ('clf', MultiOutputClassifier(RandomForestClassifier()))
        ])
    parameters_red = {
            'clf__estimator__min_samples_split': [2, 3, 4]
               }
    clf_red_dim = GridSearchCV(estimator=pipeline_red_dim, param_grid=parameters_red)
    return clf_red_dim
    

def evaluate_model(model, X_test, Y_test, category_names):
    Y_prediction_test = model.predict(X_test)
    print(classification_report(Y_test.values, Y_prediction_test, target_names=category_names))


def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath,'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,random_state=42)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
