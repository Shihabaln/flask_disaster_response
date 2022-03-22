import sys 
from sqlalchemy import create_engine
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report, fbeta_score

import re
import nltk
nltk.download(['punkt', 'wordnet'])
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pickle

def load_data(database_filepath):
    """
    Function to load data from databse 
    and parse it into features
    """
    
    connect_str = f"sqlite:///{database_filepath}"
    engine = create_engine(connect_str)
    df = pd.read_sql("SELECT * FROM df", engine)
    #drop all child alone as it has all zeros only
    df = df.drop(['child_alone'],axis=1)
    X = df.message
    Y = df.iloc[:, 4:]
    categories = Y.columns.tolist()

    return X,Y,categories

def tokenize(text):
    """
    Function to extract features
    
    Arguments:
        text -> Text message which needs to be tokenized
    Output:
        clean_tokens -> List of tokens extracted from the provided text
    """

    # Replace all urls with a urlplaceholder string
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    # Extract all the urls from the provided text 
    detected_urls = re.findall(url_regex, text)
    
    # Replace url with a url placeholder string
    for detected_url in detected_urls:
        text = text.replace(detected_url, 'url_place_holder')
    

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    # List of clean tokens
    clean_tokens = [lemmatizer.lemmatize(w).lower().strip() for w in tokens]

    return clean_tokens

def build_model():
  """
  Function to build NLP pipeline
  """
  pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('count_vectorizer', CountVectorizer(tokenizer=tokenize)),
                ('tfidf_transformer', TfidfTransformer())
            ]))
            
        ])),

        ('classifier', MultiOutputClassifier(RandomForestClassifier()))
    ])

  return pipeline

def evaluate_model(model, X_test, Y_test, category_names):
    """Print classification report for positive labels"""

    Y_predict = model.predict(X_test)
    for i, col in enumerate(Y_test):
      print(classification_report(Y_test[col], Y_predict[:, i]))

def save_model(model, model_filepath):
    '''
    Function saves the pipeline to local
    INPUT:
    model(object) - trained model
    model_filepath(str) - file path of the model
    OUTPUT:
    none
    '''
    with open(model_filepath, 'wb') as f:
        pickle.dump(model, f)

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
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