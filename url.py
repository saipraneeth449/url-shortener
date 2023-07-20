import pyshorteners
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('250x250')


entry = Entry(root,fg='#FF4517',bg='#FFF9C2',bd=1)
entry.place(x=100,y=50,width=350,height=20)

entry1 = Entry(root,fg='#FF4517',bg='#FFF9C2',bd=1)
entry1.place(x=100,y=150,width=350,height=20)


label = Label(root,text='Enter the url')
label.place(x=15,y=50)

label1 = Label(root,text='short url:')
label1.place(x=25,y=150)

def gg():
    url=entry.get()
    s=pyshorteners.Shortener()
    entry1.insert(INSERT,s.tinyurl.short(url))
    




btn = Button(root,text="Submit",bd=0,bg='#1061E6',command=gg)
btn.place(x=120,y=120)

root.mainloop()