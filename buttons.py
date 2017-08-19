from tkinter import *
from tkinter import ttk


root = Tk()
button = ttk.Button(root, text='Click me!')
button.pack()

def callback():
    print('Clicked!')

button.config(command=callback)

logo = PhotoImage(file='C:\\Users\\Paopao\\Pictures\\Python.gif')

small_logo = logo.subsample(5,5)
button.config(image = small_logo, compound = LEFT)


if __name__ == '__main__':
    mainloop()