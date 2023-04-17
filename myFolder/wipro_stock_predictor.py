import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Download data using web scraping
url = 'https://in.finance.yahoo.com/quote/WIPRO.NS/history?p=WIPRO.NS'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'W(100%) M(0)'})
df = pd.read_html(str(table))[0]

# Prepare data
x = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']
scaler = MinMaxScaler(feature_range=(0, 1))
x_scaled = scaler.fit_transform(x)
y_scaled = scaler.fit_transform(y.values.reshape(-1,1))

# Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_scaled, test_size=0.2)

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 4)))
model.add(LSTM(units=50))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, epochs=50, batch_size=32)

# Make predictions on test set
y_pred = model.predict(x_test)

# Scale back the predictions
y_pred = scaler.inverse_transform(y_pred)

# Evaluate the model
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean squared error: {mse}")
print(f"R2 score: {r2}")
