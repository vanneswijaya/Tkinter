import tkinter
from tkinter import ttk
from tkinter import *
import requests
import operator
from datetime import datetime, timedelta
from tkinter.ttk import Notebook,Entry
from tkscrolledframe import ScrolledFrame


class CoronaDB:

    def __init__(self, master):
        self.master = master
        self.createWidgets()

    def createWidgets(self):

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "LightText.TFrame",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.configure(
            "Button.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_PRIMARY,
        )


        self.corona_label = ttk.Label(self.master, text='Corona Virus Data Calculator', style="LightText.TLabel", font=('helvetica', 20))
        self.corona_label.grid(row=0, sticky='N', padx=50, pady=25)

        self.button = ttk.Button(text='Show(Country)', command=self.getcorona, style="Button.TButton")
        self.button.grid(row=2, sticky='W', padx=50, pady=5)

        self.button1 = ttk.Button(text='Show(All)', command=self.allcompare, style="Button.TButton")
        self.button1.grid(row=2, sticky='E', padx=50, pady=5)

        # self.corona_frame = ttk.Frame(self.master, borderwidth = 5, width=500, height=250, relief='groove', style="LightText.TFrame")
        # self.corona_frame.grid_propagate(False)
        # self.corona_frame.grid(row=3, sticky='w', padx=50, pady=5)

        self.corona_frame = ScrolledFrame(self.master, borderwidth = 5, width=400, height=220, bg='black')
        self.corona_frame.grid(row=4, sticky='w', padx=50, pady=5)

        # Bind the arrow keys and scroll wheel
        self.corona_frame.bind_arrow_keys(self.master)
        self.corona_frame.bind_scroll_wheel(self.master)

        self.inner_frame = self.corona_frame.display_widget(Frame)

        options = [
            "World",
            "Czech Republic",
            "India",
            "United States of America",
            "Spain",
            "Italy",
            "France",
            "Germany",
            "China",
            "United Kingdom",
            "Turkey",
            "Belgium",
            "Switzerland",
            "Netherlands",
            "Canada",
            "Brazil",
            "Portugal",
            "Austria",
            "Pakistan",
        ]

        self.clicked = StringVar()
        self.clicked.set(options[0])
        self.drop = OptionMenu(self.master, self.clicked, *options)
        self.drop.config(bg = "#808080")
        self.drop["menu"].config(bg="white")
        self.drop.grid(row=1, sticky='W', padx=50, pady=5)

    def allcompare(self):
        if self.inner_frame.grid_slaves():
            self.clearContents()

        endpoint = "https://api.covid19api.com/summary"
        response = requests.get(endpoint)
        corona = response.json()
        dict = {}
        for data in corona['Countries']:
            new_dict = {**dict, **{data['Country']: data['TotalConfirmed']}}
            dict = new_dict

        sorted_data = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)

        i = 1
        for item in sorted_data:
            text_val1 = item[0]
            text_val2 = item[1]
            ttk.Label(self.inner_frame,
                      borderwidth = 3,
                      width = 20,
                      text=text_val1,
                      font=('helvetica', 16),
                      style="Button.TButton",
                      wraplength=500).grid(row=i, column=2)

            ttk.Label(self.inner_frame,
                      borderwidth = 3,
                      width = 20,
                      text=text_val2,
                      font=('helvetica', 16),
                      style="Button.TButton",
                      wraplength=500).grid(row=i, column=4)
            i = i + 1


    def getcorona(self):
        if self.inner_frame.grid_slaves():
            self.clearContents()


        endpoint = "https://api.covid19api.com/summary"
        response = requests.get(endpoint)
        corona = response.json()  # corona data in json format
        dd_clicked = self.clicked.get()

        keys = {'NewConfirmed': 'New Confirmed', 'TotalConfirmed': 'Total Cases', 'NewDeaths': 'New Deaths', 'TotalDeaths': 'Total Deaths', 'NewRecovered': 'New Recovered', 'TotalRecovered': 'Total Recovered'}

        if dd_clicked != "World":
            for country_data in corona['Countries']:
                if country_data['Country'] == dd_clicked:
                    i = 1
                    for item in keys:
                        text_val1 = keys[item]
                        text_val2 = str(country_data[item])
                        ttk.Label(self.inner_frame,
                                  borderwidth = 3,
                                  width = 20,
                                  text=text_val1,
                                  font=('helvetica', 16),
                                  style="Button.TButton",
                                  wraplength=500).grid(row=i, column=2)

                        ttk.Label(self.inner_frame,
                                  borderwidth = 3,
                                  width = 20,
                                  text=text_val2,
                                  font=('helvetica', 16),
                                  style="Button.TButton",
                                  wraplength=500).grid(row=i, column=4)
                        i = i + 1
        else:
            i = 1
            for item in keys:
                text_val1 = keys[item]
                text_val2 = str(corona['Global'][item])
                ttk.Label(self.inner_frame,
                          borderwidth = 3,
                          width = 20,
                          text=text_val1,
                          font=('helvetica', 16),
                          style="Button.TButton",
                          wraplength=500).grid(row=i, column=2)

                ttk.Label(self.inner_frame,
                          borderwidth = 3,
                          width = 20,
                          text=text_val2,
                          font=('helvetica', 16),
                          style="Button.TButton",
                          wraplength=500).grid(row=i, column=4)
                i = i + 1

    def clearContents(self):
        for widget in self.inner_frame.grid_slaves():
            widget.destroy()



if __name__ == '__main__':
    COLOUR_PRIMARY = "#808080"
    COLOUR_SECONDARY = "#000000"
    COLOUR_LIGHT_BACKGROUND = "#fff"
    COLOUR_LIGHT_TEXT = "#eee"
    COLOUR_DARK_TEXT = "#8095a8"

    master = tkinter.Tk()
    CoronaDB(master)
    master.title('Virus Data Tracker')
    master.geometry('520x550+125+50')
    master.configure(bg=COLOUR_PRIMARY)
    master.mainloop()
