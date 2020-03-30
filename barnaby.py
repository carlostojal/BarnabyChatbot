
#
# Copyright (c) Carlos Tojal
# BarnabyChatbot
# barnaby.py
#

from tkinter import *
from barnaby_consultant import BarnabyConsultant

def consult():
    text.config(state=NORMAL)
    text.insert(INSERT, "Me: {}\n".format(entry.get()))
    response = BarnabyConsultant().consult_barnaby(entry.get())
    entry.delete(0, END)
    text.insert(INSERT, "Barnaby: {}\n".format(response['response']))
    if response['functionality'] == "news":
        if response['lang'] == "en":
            text.insert(INSERT, "Here are the top headlines.\n")
        for n in response['content']:
            text.insert(INSERT, "{}\n".format(response['content'][str(n)]['title']))
    text.config(state=DISABLED)

print("** Barnaby Chatbot **\n")
print("Initializing...")

root = Tk()
root.title("Barnaby Chatbot")
root.resizable(False, False)
label = Label(root, text="Barnaby Chatbot")
label.pack()
text = Text(root)
text.insert(INSERT, "Barnaby: Hello, my name is Barnaby!\n")
text.config(state=DISABLED)
text.pack()
entry = Entry(root)
entry.pack(side=LEFT)
button = Button(root, text="Send", command=consult)
button.pack(side=RIGHT)

print("Initialized.")

root.mainloop()