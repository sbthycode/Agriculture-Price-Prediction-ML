# Agriculture Price Prediction using Machine Learning


## File structure

1. All code is present inside the src folder
2. All data, along with the cleaned data is present in the data folder
3. The saved models are stored in the saved folder to be used while inference.


## Approach

1. Identified the contributing factors to the price of every commodity, removed redundant data and removed the outliers in the data.
2. Used an pipiline consisting of Random Forest Regressor and a polinomial regressor.
3. Used FASTAPI to prepare the model endpoint.
4. Developed a Frontend for the user.

## How to run?

- Pull the code base
- Create a conda environment 
- Install the fastapi library
- Make sure you have the standard ML libraries(sklearn, pandas) installed.
- go into the src folder and type uvicorn main:app --reload
- now open the link and go to some link for example to make sure the endpoint works:  http://127.0.0.1:8000/make_prediction/?commodity=commodity_name&APMC=APMC_name&date=date&arrival=arrival (fill accordingly)
- For the frontend:
    - go to src/backend
    - run ``` npm install ```
    - run ```  node server.js  ```     
    - go to the server location, and you're good to go!

## Result:

- Got an MAE of 552 on the Modal Price based on given features.
