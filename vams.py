from tkinter import *
from tkinter import ttk

window = Tk()

#Setting the size of the window
window.geometry('350x200')
window.title("Welcome to Tkinter")

#username
lb1 = Label(window, text="Username", font=("Arial Bold", 15))
lb1.place(x=50,y=50)

var1 = StringVar() 
txt1 = Entry(window,width=20, textvariable=var1)
txt1.place(x=170,y=57)

#password
lb2 = Label(window, text="Password", font=("Arial Bold", 15))
lb2.place(x=50,y=100)

var2 = StringVar() 
txt2 = Entry(window,width=20, textvariable=var2)
txt2.place(x=170,y=100)

btn = ttk.Button(window, text="Login", width=20)
btn.place(x=100,y=150)

window.mainloop()
