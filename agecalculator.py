import tkinter as tk
from tkinter import font
import datetime

HEIGHT = 500
WIDTH = 600

def calcage():
    today = datetime.date.today()
    bornday = datetime.date(int(insyear.get()), int(insmonth.get()), int(insday.get()))
    birthday = datetime.date(today.year, bornday.month, bornday.day)
    if birthday < today:
        yourage = today.year - bornday.year
    else:
        yourage = today.year - bornday.year - 1
    msg = '%s is %s years old!' % (str(insname.get()), yourage)
    label['text'] = msg

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='salmon', bd=10)
frame.place (relx=0.5, rely=0.1, relwidth=0.75, relheight= 0.4, anchor='n')

nlabel = tk.Label(frame, text='NAME', bg='salmon', font=('Papyrus', 25))
nlabel.place(relx=0.07)

ylabel = tk.Label(frame, text='YEAR', bg='salmon', font=('Papyrus', 25))
ylabel.place(relx=0.07, rely=0.25)

mlabel = tk.Label(frame, text='MONTH', bg='salmon', font=('Papyrus', 25))
mlabel.place(relx=0.07, rely=0.5)

dlabel = tk.Label(frame, text='DAY', bg='salmon', font=('Papyrus', 25))
dlabel.place(relx=0.07, rely=0.75)

insname = tk.Entry(frame, highlightbackground='red', font=('Papyrus', 25))
insname.place(relx=0.35, relwidth=0.65, relheight=0.25)

insyear = tk.Entry(frame, highlightbackground='red', font=('Papyrus', 25))
insyear.place(rely=0.25, relx=0.35, relwidth=0.65, relheight=0.25)

insmonth = tk.Entry(frame, highlightbackground='red', font=('Papyrus', 25))
insmonth.place(rely=0.5, relx=0.35, relwidth=0.65, relheight=0.25)

insday = tk.Entry(frame, highlightbackground='red', font=('Papyrus', 25))
insday.place(rely=0.75, relx=0.35, relwidth=0.65, relheight=0.25)

mid_frame = tk.Frame(root, bg = 'red', bd=5)
mid_frame.place(relx=0.5, rely=0.55, relwidth=0.5, relheight=0.1, anchor='n')

button = tk.Button(mid_frame, font=('Papyrus', 20), text='CALCULATE AGE', highlightbackground='red', fg='white', command=lambda: calcage())
button.place(relwidth=1,relheight=1)

lower_frame = tk.Frame(root, bg='red', bd=5)
lower_frame.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(lower_frame, bg='salmon', font=('Papyrus', 30))
label.place(relwidth=1,relheight=1)

root.mainloop()