## Installation <a name="installation"></a>

There should be no trouble running the python scripts as it only requires installing the requirment file in  Python 3 env and following are the main libraries used

* `pandas`
* `scikit-learn`
* `nltk`
* `sqlalchemy`

Data used and downloaded from [here](https://appen.com/datasets-resource-center/).
`categories.csv` - CSV file with main categories 
`messages.csv` - CSV file with messages recived from social, direct or news

In the created env , install all packages used:
```cli
pip install -r requirements.txt
```

Then run the app :
```cli
python app/run.py
```
## Project Motivation<a name="motivation"></a>

This project goal is to mimic how organizations responds to messages received during a disaster. 
A machine learning model was trained with messages received from news, social media, and other direct messages.
The user then can insert any message and the app will try to classify it to categories, so that organizations can priorities responses and act accordingly. 

## Results<a name="results"></a>



## Licensing, Authors, Acknowledgements<a name="licensing"></a>

This project is licensed under the MIT License

## Files
C:.
|   .gitignore
|   README.md
|   tree.txt
|   
+---.ipynb_checkpoints
|       ETL Pipeline Preparation-checkpoint.ipynb
|       ML Pipeline Preparation-checkpoint.ipynb
+---App
|   |   figure.py
|   |   run.py
|   |   
|   +---static
|   |   +---favicon
|   |   |            
|   |   +---img
|   |   |       
|   |   \---styles
|   |           
|   +---templates
|   |       go.html
|   |       master.html
+---data
|   |   categories.csv
|   |   DisasterResponse.db
|   |   ETL Pipeline Preparation.ipynb
|   |   messages.csv
|   |   process_data.py
|   
|   
\---models
        classifier.pkl
        Ml.ipynb
        train_classifier.py