import requests
import tkinter as tk
from tkinter import messagebox, StringVar

# Create main windows
root = tk.Tk()
root.title("PyWeather")
units = StringVar(root, "")

# Create and configure labels and entry fields
city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()
state_label = tk.Label(root, text="State Code:")
state_label.pack()
state_entry = tk.Entry(root)
state_entry.pack()
country_label = tk.Label(root, text="Country Code:")
country_label.pack()
country_entry = tk.Entry(root)
country_entry.pack()
units_label = tk.Label(root, text="Units:")
units_label.pack()
values = {"Kelvin": "", "Celsius": "metric", "Fahrenheit": "imperial"}
for (text, value) in values.items():
    tk.Radiobutton(root, text=text, variable=units, value=value, indicator=0, background="light blue").pack(ipady=5)

# Create a button to fetch weather data
fetch_button = tk.Button(root, text="Fetch Weather")
fetch_button.pack()

# Create a label to display weather information
weather_label = tk.Label(root, text="")
weather_label.pack()


# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    state = state_entry.get()
    country = country_entry.get()
    # Call API
    api_key = "d9089f7a0ffa26ae1eee4c371bd93715"
    geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={api_key}"
    try:
        response = requests.get(geo_url)
        data = response.json()
        lat = data[0]["lat"]
        lon = data[0]["lon"]
    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch weather data: {e}")

    onecall_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units.get()}&appid={api_key}"

    try:
        response = requests.get(onecall_url)
        data = response.json()

        temperature = data["current"]["temp"]
        weather = data["current"]["weather"][0]["description"]
        if units.get() == "imperial":
            weather_label.config(text=f"Temperature: {temperature} F\nWeather: {weather}")
        elif units.get() == "metric":
            weather_label.config(text=f"Temperature: {temperature} C\nWeather: {weather}")
        else:
            weather_label.config(text=f"Temperature: {temperature} K\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch weather data: {e}")


fetch_button.config(command=fetch_weather)

# Start the GUI main loop
root.mainloop()
