import requests
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

# Replace with your OpenWeatherMap API key
api_key = "f496f4c9efc08706626a74e3ceb89186"
location = input("Enter Location (e.g., city, country): ")  # Prompt user for the location

# Function to get weather data from OpenWeatherMap API
api_key = 'f496f4c9efc08706626a74e3ceb89186'

def get_weather_forecast(city_name):
    base_url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit or 'metric' for Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_desc = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f"Weather in {city_name}:")
            print(f"Description: {weather_desc.capitalize()}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    get_weather_forecast(city_name)



# Sample dataset for crop prediction with multiple crop varieties
data = {
    'pH': [6.5, 7.2, 5.8, 6.9, 6.0, 6.8, 6.2, 7.1, 5.6],
    'Nitrogen': [25, 30, 20, 28, 22, 26, 24, 29, 18],
    'Phosphorus': [12, 15, 10, 14, 11, 13, 12, 16, 9],
    'Potassium': [35, 40, 30, 38, 32, 36, 34, 41, 28],
    'Temperature': [20, 25, 15, 5, 30, 10, -5, 22, 12],  # Temperature in degrees Celsius
    'Crop_Type': [0, 1, 0, 1, 0, 1, 0, 1, 0],  # 0 for home use, 1 for sale
    'Crop_Name': ['Wheat', 'Rice', 'Maize', 'Soybean', 'Barley', 'Corn', 'Potato', 'Oats', 'Sorghum'],
    'Yield_kg_per_acre': [2000, 2500, 3000, 1800, 2200, 2600, 2100, 2800, 2400],
    'Market_Price_per_kg': [0.5, 0.6, 0.4, 0.8, 0.7, 0.6, 0.4, 0.55, 0.65],
    'Profit_ton': [1.0, 1.5, 1.2, 1.8, 1.4, 1.6, 1.3, 1.7, 1.1],
    'Time_to_Grow_days': [120, 150, 90, 100, 130, 110, 80, 140, 95],  # Average time to grow in days
}

# Create a DataFrame with crop details
df = pd.DataFrame(data)

# Split the dataset into features (X) and target (y)
X = df[['pH', 'Nitrogen', 'Phosphorus', 'Potassium', 'Temperature']]
y_profit = df['Profit_ton']
y_crop_name = df['Crop_Name']
y_crop_type = df['Crop_Type']
y_time_to_grow = df['Time_to_Grow_days']  # New target for time duration prediction

# Initialize and train a Random Forest Regressor model for profit prediction
profit_model = RandomForestRegressor(random_state=42)
profit_model.fit(X, y_profit)

# Initialize and train a Random Forest Classifier model for crop name prediction
crop_name_model = RandomForestClassifier(random_state=42)
crop_name_model.fit(X, y_crop_name)

# Initialize and train a Random Forest Classifier model for crop type prediction
crop_type_model = RandomForestClassifier(random_state=42)
crop_type_model.fit(X, y_crop_type)

# Initialize and train a Random Forest Regressor model for time duration prediction
time_to_grow_model = RandomForestRegressor(random_state=42)
time_to_grow_model.fit(X, y_time_to_grow)

# User inputs for prediction
user_pH = float(input("Enter pH value (6.5, 7.2, 5.8, 6.9, 6.0, 6.8, 6.2, 7.1, 5.6): "))
user_Nitrogen = float(input("Enter Nitrogen value (25, 30, 20, 28, 22, 26, 24, 29, 18): "))
user_Phosphorus = float(input("Enter Phosphorus value (12, 15, 10, 14, 11, 13, 12, 16, 9): "))
user_Potassium = float(input("Enter Potassium value (35, 40, 30, 38, 32, 36, 34, 41, 28): "))
user_temperature = float(input("Enter Temperature (in degrees Celsius): "))
user_crop_quantity = float(input("Enter Quantity of Crop (in kg): "))
user_land_size = float(input("Enter Land Size (in acres 1-10 acres): "))
user_water_source = input("Enter Water Source (e.g., 'Well', 'Irrigation', 'Rainfed'): ").strip().lower()

user_data = [[user_pH, user_Nitrogen, user_Phosphorus, user_Potassium, user_temperature]]
user_profit_prediction = profit_model.predict(user_data)
user_crop_type_prediction = crop_type_model.predict(user_data)
user_crop_name_prediction = crop_name_model.predict(user_data)
user_time_to_grow_prediction = time_to_grow_model.predict(user_data)

# Determine the Recommendation for Crop Type
if user_crop_type_prediction[0] == 0:
    crop_type_recommendation = "Grow this crop for personal consumption (home use)."
else:
    crop_type_recommendation = "Grow this crop for sale."

# Determine the Recommendation for Water Source
water_source_recommendation = ""
if user_water_source == 'well':
    water_source_recommendation = "Ensure proper maintenance of your well for irrigation."
elif user_water_source == 'irrigation':
    water_source_recommendation = "Optimize your irrigation system for efficient water use."
elif user_water_source == 'rainfed':
    water_source_recommendation = "Monitor weather forecasts for rainfed crops."
else:
    water_source_recommendation = "Ensure you have a reliable water source for your crops."

# Additional Recommendations based on Land Size
land_size_recommendation = ""
if user_land_size >= 10:
    land_size_recommendation = "Consider expanding your cultivation area."
elif user_land_size < 1:
    land_size_recommendation = "Consider optimizing your land usage for higher yields."

# Display Predictions and Recommendations
print(f"Predicted crop name: {user_crop_name_prediction[0]}")
print(f"Predicted profit: {user_profit_prediction[0]:.2f} tons")
print(f"Predicted crop type: {crop_type_recommendation}")
print(f"Predicted time to grow: {user_time_to_grow_prediction[0]:.0f} days")
print(land_size_recommendation)
print(water_source_recommendation)
