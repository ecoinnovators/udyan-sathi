import pandas as pd
from datetime import datetime, timedelta
from statsmodels.tsa.arima.model import ARIMA

# Load your CSV data
data = pd.read_csv('pollutiondata_Final3.csv')

# Check and clean data types
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data['AQI'] = pd.to_numeric(data['AQI'], errors='coerce')

# Function to predict next day's AQI for a given city using ARIMA
def predict_next_day_aqi(city):
    # Filter data for the specified city
    city_data = data[data['City'] == city]

    if city_data.empty:
        return "No data available for the specified city."

    # Sort data by date
    city_data = city_data.sort_values(by='Date')

    # Calculate the next day's date
    city_data['Next_Day'] = city_data['Date'] + timedelta(days=1)

    # Extract AQI values as a time series
    aqi_series = city_data.set_index('Date')['AQI'].dropna()  # Remove rows with NaN values

    # Create and train an ARIMA model
    model = ARIMA(aqi_series, order=(1, 1, 1))
    model_fit = model.fit()

    # Make a one-step forecast for the next day's AQI
    forecast = model_fit.get_forecast(steps=1)

    # Get the prediction for the next day's AQI
    predicted_next_day_aqi = forecast.predicted_mean
    

    return predicted_next_day_aqi

if __name__ == "__main__":
    # User input for the city
    city = input("Enter the city: ")

    # Predict the next day's AQI for the city using ARIMA
    predicted_aqi = predict_next_day_aqi(city)

    x = predicted_aqi.tolist()
    print('Tommorows expected AQI - ',x[0])

    
