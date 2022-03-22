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
In order to set up the model with data to do the processing and train the model, do the following: 

```cli
data\python process_data.py disaster_messages.csv disaster_categories.csv 'DisasterResponse.db'
```
Then train the model and save it

```cli
models\python train_classifier.py ./data/DisasterResponse.db classifier.pkl
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
main page :
<img width="945" alt="image" src="https://user-images.githubusercontent.com/83282165/159465963-ed423f58-60a1-4f0c-ab50-1510f59e16a7.png">

messages test of how the app works :
<img width="911" alt="image" src="https://user-images.githubusercontent.com/83282165/159412931-e87af2da-a7cc-4338-ba36-e1b2efcea030.png">

![Screenshot 2022-03-22 075706](https://user-images.githubusercontent.com/83282165/159412372-7619569e-ec8d-4ae5-abc8-347b4303d0a7.jpg)

![Screenshot 2022-03-22 075900](https://user-images.githubusercontent.com/83282165/159412234-d1e57cdb-0bb0-4236-a63a-e525d0934b0e.jpg)


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

This project is licensed under the MIT License

## Files
![image](https://user-images.githubusercontent.com/83282165/159412005-f1a68f00-c418-4186-a7ec-e6b9fef89c7b.png)

