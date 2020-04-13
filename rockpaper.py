import tkinter as tk
from tkinter import font
import random

HEIGHT = 500
WIDTH = 600

userscore = 0
compscore = 0
userchoice = ''
compchoice = ''

def choicetonum(choice):
    rps = {'rock':0, 'paper':1, 'scissor':2}
    return rps.get(choice)

def comprand():
    return random.choice(['rock','paper','choice'])

def result(humchoice, comchoice):
    global userscore
    global compscore
    user = choicetonum(humchoice)
    comp = choicetonum(comchoice)
    if user == comp:
        win = 'It is a tie!'
    elif (user-comp)%3==1:
        win = 'You won!'
        userscore += 1
    else:
        win = 'You lost!'
        compscore += 1
    finalstr = 'Your choice: %s \nComputers choice: %s \n%s \nYour score: %s \nComputers score: %s' % (humchoice,comchoice,win,userscore,compscore)
    return finalstr

def rchoice():
    global userchoice
    global compchoice
    userchoice = 'rock'
    compchoice = comprand()
    label['text'] = result(userchoice, compchoice)

def pchoice():
    global userchoice
    global compchoice
    userchoice = 'paper'
    compchoice = comprand()
    label['text'] = result(userchoice, compchoice)

def schoice():
    global userchoice
    global compchoice
    userchoice = 'scissor'
    compchoice = comprand()
    label['text'] = result(userchoice, compchoice)

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='red', bd=5)
frame.place (relx=0.5, rely=0.1, relwidth=0.75, relheight= 0.1, anchor='n')

rock = tk.Button(frame, font=('Papyrus', 15), text='ROCK', highlightbackground='gold', fg='red2', command=lambda:rchoice())
rock.place(relwidth=0.3, relheight=1)

paper = tk.Button(frame, font=('Papyrus', 15), text='PAPER', highlightbackground='cyan', fg='red2', command=lambda:pchoice())
paper.place(relx=0.3, relwidth=0.4, relheight=1)

scissor = tk.Button(frame, font=('Papyrus', 15), text='SCISSOR', highlightbackground='green2', fg='red2', command=lambda:schoice())
scissor.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='red', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='salmon', font=('Papyrus', 30))
label.place(relwidth=1,relheight=1)

root.mainloop()