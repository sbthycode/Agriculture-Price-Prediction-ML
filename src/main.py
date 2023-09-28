from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Now we load the model and label encoder

import pickle

model = pickle.load(open('D:\ML-5\saved\model.pkl', 'rb'))
le = pickle.load(open('D:\ML-5\saved\label_encoder.pkl', 'rb'))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/make_prediction/")
async def read_item(commodity: str = None, APMC: str = None, date: str = None):
    
    # We need to convert the categorical features to numerical values
    commodity = le.transform([commodity])
    APMC = le.transform([APMC])
    
    # We need to convert the date to datetime format
    date = pd.to_datetime(date)
    date = date.strftime('%Y%m').astype(int)

    # We need to create a dataframe with the given values
    df = pd.DataFrame({'Commodity': commodity, 'APMC': APMC, 'date': date})

    # We need to predict the modal price
    modal_price = model.predict(df)

        
    return {"predicted_price": modal_price[0]}
