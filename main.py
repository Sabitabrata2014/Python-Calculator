from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("400x400")

lb1 = Label(window,text="First Number")
lb2 = Label(window,text="Second Number")
lb3 = Label(window,text="Result")

t1 = Entry()
t2 = Entry()
t3 = Entry()

lb1.place(x=50,y=50)
t1.place(x=150,y=50)

lb2.place(x=50,y=100)
t2.place(x=155,y=100)

lb3.place(x=50,y=150)
t3.place(x=100,y=150)

def add():
  num1 = int(t1.get())
  num2 = int(t2.get())
  result = num1 + num2
  t3.insert(END,str(result))

def sub():
  num1 = int(t1.get())
  num2 = int(t2.get())
  result = num1 - num2
  t3.insert(END,str(result))

def mul():
  num1 = int(t1.get())
  num2 = int(t2.get())
  result = num1 * num2
  t3.insert(END,str(result))

def div():
  num1 = int(t1.get())
  num2 = int(t2.get())
  result = num1 / num2
  t3.insert(END,str(result))

def clear():
  t1.delete(0,END)
  t2.delete(0,END)
  t3.delete(0,END)

b1=Button(window,text="Add",command=add)
b1.place(x=40,y=200)

b2=Button(window,text="Subtract",command=sub)
b2.place(x=105,y=200)

b3=Button(window,text="Multiply",command=mul)
b3.place(x=200,y=200)

b4=Button(window,text="Divide",command=div)
b4.place(x=285,y=200)

b5=Button(window,text="Clear",command=clear)
b5.place(x=170,y=250)
