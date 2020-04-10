import tkinter as tk
from tkinter import font
import requests
import sys
import os

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print('This is the entry:', entry)

#b0360521219674dadf74a781607524c4
#api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'Invalid input'
    return final_str

def get_weather(city):
    weather_key = 'b0360521219674dadf74a781607524c4'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

if getattr(sys, 'frozen', False):
    background_image = tk.PhotoImage(file=os.path.join(sys._MEIPASS, 'landscape.png'))
else:
    background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bd=10)
frame.place (relx=0.5, rely=0.1, relwidth=0.75, relheight= 0.1, anchor='n')

entry = tk.Entry(frame, highlightbackground='red', font=('Papyrus', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, font=('Papyrus', 15), text='Get Weather', highlightbackground='red', fg='white', command=lambda: get_weather(entry.get()))
button.place(relx=0.65,relwidth=0.35,relheight=1)

lower_frame = tk.Frame(root, bg='red', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='salmon', font=('Papyrus', 30))
label.place(relwidth=1,relheight=1)



root.mainloop()