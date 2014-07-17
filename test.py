from turtle import *
from Tkinter import *

class Painter(Turtle):

    def __init__(self):
        self.window_height(200)
        self.window_width(200)

    def paint(self, x, y):
        print x, y
        #self.fillcolor("yellow")
        self.dot()


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.init()

    def init(self):
        turtle = Turtle()
        turtle.onclick(turtle.fd(15))

app = App()
app.mainloop()