import streamlit as st
import requests
import datetime

def get_weather_data(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error: Unable to fetch weather data. Please check your API key and try again.")
        return None

def display_weather(data):
    st.header(f"Weather Forecast for {data['city']['name']}, {data['city']['country']}")

    for forecast in data['list'][:8]:  # Display the next 8 time periods (24 hours)
        dt = datetime.datetime.fromtimestamp(forecast['dt'])
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description'].capitalize()
        wind_speed = forecast['wind']['speed']

        st.subheader(f"{dt.strftime('%A, %d %b %Y %H:%M')}:")
        st.write(f"**Temperature:** {temp} °C")
        st.write(f"**Description:** {description}")
        st.write(f"**Wind Speed:** {wind_speed} m/s")
        st.write("---")

def main():
    st.title("Weather Forecast App for Erbil")

    # Replace this with your actual OpenWeatherMap API key
    api_key = "your_default_api_key_here"
    city = "Erbil"

    weather_data = get_weather_data(api_key, city)
    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
