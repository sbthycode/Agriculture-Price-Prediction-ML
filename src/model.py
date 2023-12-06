# Import libraries
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Load cleaned data
df = pd.read_csv('D:\ML-5\data\Cleaned_data.csv')

# Drop columns with names: min_price, max_price
df.drop(['min_price', 'max_price'], axis=1, inplace=True)
print(df.head())

# Now we train a model to predict the modal_price based 
# on the arrivals_in_qtl, APMC, Commodity, and date
# Since we have categorical features we need a label encoder
# to convert them to numerical values
le1 = LabelEncoder()
df['APMC'] = le1.fit_transform(df['APMC'])
le2= LabelEncoder()
df['Commodity'] = le2.fit_transform(df['Commodity'])

# We will need to convert the date column to datetime format
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.strftime('%Y%m').astype(int)
print(df.head())
# Split the data into train and test sets
X = df.drop(['modal_price'], axis=1)
y = df['modal_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# This is clearly a regression task. We create a random forest regressor object.
rf = RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_leaf=2, min_samples_split=2)

# We will do ensemble learning of polynomial regressor and Random Forest Regresson using stacking
model = make_pipeline(PolynomialFeatures(2), rf)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate the mean absolute error
mae = mean_absolute_error(y_test, y_pred)
print('Mean absolute error: ', mae)


# We save the model and label encoder using pickle
# pickle.dump(model, open('D:\ML-5\saved\model.pkl', 'wb'))
# pickle.dump(le1, open('D:\ML-5\saved\label_encoder_apmc.pkl', 'wb'))
# pickle.dump(le2, open('D:\ML-5\saved\label_encoder_commodity.pkl', 'wb'))
print('Model and label encoders saved successfully')