# ML-5
SmartSense Agriculture Price Prediction



## File structure

1. All code is present inside the src folder
2. All data, along with the cleaned data is present in the data folder
3. The saved models are stored in the saved folder to be used while inference.


## Approach

1. Identified the contributing factors to the price of every commodity, removed redundant data and removed the outliers in the data.
2. Used an pipiline consisting of Random Forest Regressor and a polinomial regressor.
3. Used FASTAPI for user side of the model.

## How to run?

- Pull the code base
- Make sure you have the standard ML libraries(sklear, pandas) installed.
- Install the fastapi library.
- go into the src folder and type uvicorn main:app --reload
- now open the link and go to some link for example:  http://127.0.0.1:8000/make_prediction/?commodity=commodity_name&APMC=APMC_name&date=date
- otherwise you can use the saved model to make inference

## Result:

- Did a train test split of 80:20
- Got an MAE of 699.2
