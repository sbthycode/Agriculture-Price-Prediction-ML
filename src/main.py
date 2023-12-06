from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI()

# Now we load the model and label encoder
model = pickle.load(open('D:\ML-5\saved\model.pkl', 'rb'))
le1 = pickle.load(open('D:\ML-5\saved\label_encoder_apmc.pkl', 'rb'))
le2 = pickle.load(open('D:\ML-5\saved\label_encoder_commodity.pkl', 'rb'))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/make_prediction/")
async def read_item(commodity: str = None, APMC: str = None, date: str = None, arrival: int = None):
    
    # We need to convert the categorical features to numerical values
    APMC = le1.transform([APMC])
    commodity = le2.transform([commodity])
    
    # We need to convert string date in format "YYYY-MM" to "YYYYMM"
    date = date.replace('-', '')

    # We need to create a dataframe with the given values
    df = pd.DataFrame({'APMC': APMC,'Commodity': commodity,'arrival_in_qtl': arrival, 'date': date})

    # We need to predict the modal price
    modal_price = model.predict(df)

        
    return {"predicted_price": modal_price[0]}
