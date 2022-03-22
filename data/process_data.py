import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """Function to load and merge datasets """
    messages = pd.read_csv('messages.csv')
    categories = pd.read_csv('categories.csv')

    return pd.merge(messages,categories, on='id')

def clean_data(df):
    """Function to split categories into seperate columns 
    and drop duplicate
    """
    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';',expand = True)

    #extract category labels
    row = categories.loc[0]
    category_colnames = row.apply(lambda x:x.split('-')[0])

    #rename all columns
    categories.columns = category_colnames

    #convert category valurd to either 0 or 1
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x:x[-1]) 
    
        # convert column from string to numeric
        categories[column] = categories[column].astype('int')
    
    #extract values with 0 and 1 only 
    categories = categories.clip(0, 1)
    #replacing categories column in df with new coumns 
    df = df.drop("categories", axis =1)
    df = pd.concat([df, categories], axis =1)

    #drop duplicate 
    df.drop_duplicates()
    return df

def save_data(df, database_filename):
    """Save DataFrame to sqlite database"""

    engine = create_engine('sqlite:///database_filename.db')
    df.to_sql('database_filename', engine, index=False, if_exists="replace")

      

def main():

    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'

              .format(messages_filepath, categories_filepath))

        df = load_data(messages_filepath, categories_filepath)


        print('Cleaning data...')

        df = clean_data(df)

        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))

        save_data(df, database_filepath)
        

        print('Cleaned data saved to database!')


    else:
 
        print('Please provide the filepaths of the messages and categories '\

              'datasets as the first and second argument respectively, as '\

              'well as the filepath of the database to save the cleaned data '\

              'to as the third argument. \n\nExample: python process_data.py '\

              'disaster_messages.csv disaster_categories.csv '\

              'DisasterResponse.db')



if __name__ == '__main__':

    main()