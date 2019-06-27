"""
Simple Weather

A simple widget for location based weather using Python 3 and Tkinter.
This program is licenced under GPLv3.

"""

import tkinter as tk
from tkinter import font
import requests
from PIL import ImageTk, Image
import os

HEIGHT = 500
WIDTH = 600
FONT = 40


def test_function(entry):
    print("This is the entry:", entry)


def format_response(weather):

    try:

        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (ºC): %s' % (str(name), str(desc) ,str(temp))
    except:
        final_str = 'There was a problem retrieving the requested information.\n' \
                    'Please verify the name/code of the place and your spelling.\n' \
                    'Keep in mind that cities outside of the US must specify \nthe nation after the name/code.'

    return final_str


def get_weather(city):
    # Key to use the OpenWeatherMap
    weather_key = '10cc2c05606a3abcb22d5f4dfdae45fc'
    # URL of the weather api
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    # Gets parameters to the api using a valid key and a location
    weather_params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    # Requests the response using parameters
    response = requests.get(api_url, params=weather_params)
    # Receives the weather information in text format
    weather_info = response.json()

    label_main['text'] = format_response(weather_info)

    # api.openweathermap.org/data/2.5/forecast/hourly?q={city name},{country code}


# Creates a new window.
root_tk = tk.Tk()

# Create a new canvas
canvas_main = tk.Canvas(root_tk, height=HEIGHT, width=WIDTH)
canvas_main.pack()

# Finds the directory for the file
dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, '/Users/sckar/Documents/GitHub/SimpleWeather/images/landscape.png')

# Loads a png image on tk
bkg_image = ImageTk.PhotoImage(Image.open(filename))
# bkg_image = tk.PhotoImage(file="C:/Users/sckar/Documents/GitHub/SimpleWeather/images/kg.jpg")
bkg_label = tk.Label(root_tk, image=bkg_image)
bkg_label.place(relwidth=1, relheight=1)

# Create a new frame
frame_upper = tk.Frame(root_tk, bg='#80c1ff', bd=5)
# Places the frame
frame_upper.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Creates a text field
entry = tk.Entry(frame_upper, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

# Creates a new button
button_locate = tk.Button(frame_upper, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button_locate.place(relx=0.7, relwidth=0.3, relheight=1)

# Create the lower frame
frame_lower = tk.Frame(root_tk, bg='#80c1ff', bd=10)
frame_lower.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Creates a label
label_main = tk.Label(frame_lower, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label_main.place(relwidth=1, relheight=1)

# Runs the main window in a loop
root_tk.mainloop()
