
from tkinter import *
x = Tk()

x.title("Calculator")
x.geometry("264x300")
a = StringVar()
e1 = Entry(x, width=42, bd=5, textvariable=a)
e1.grid(row=0, columnspan=4)
result_shown = False

def clear():
    global result_shown
    a.set("")
    result_shown = False

def click(y):

    global result_shown
    c = a.get()

    if result_shown:
        if y in "+-*/%":
            a.set(c + y)  
        else:
            a.set(y)
        result_shown = False
        return

    if c == "0":
        a.set(y)
   
    else:
        a.set(c + y)


def equal():
    global result_shown
    z = a.get()
    z = z.replace('+0', '+').replace('-0', '-').replace('*0', '*').replace('/0', '/')
    f = eval(z)
    a.set(f)
    result_shown = True

            
  

def backspace():
    c = a.get()
    a.set(c[:-1])

# Update button bindings without passing extra arguments
b1 = Button(x, text="clear", bg="black", fg="white", height=3, width=8, command=clear)
b1.grid(row=1, column=0)
b2 = Button(x, text="<", bg="black", fg="white", height=3, width=8, command=backspace)  # backspace
b2.grid(row=1, column=1)
b3 = Button(x, text="%", bg="black", fg="white", height=3, width=8, command=lambda: click('%'))
b3.grid(row=1, column=2)
b4 = Button(x, text="/", bg="black", fg="white", height=3, width=8, command=lambda: click('/'))
b4.grid(row=1, column=3)

b1 = Button(x, text="7", bg="black", fg="white", height=3, width=8, command=lambda: click('7'))
b1.grid(row=2, column=0)
b2 = Button(x, text="8", bg="black", fg="white", height=3, width=8, command=lambda: click('8'))
b2.grid(row=2, column=1)
b3 = Button(x, text="9", bg="black", fg="white", height=3, width=8, command=lambda: click('9'))
b3.grid(row=2, column=2)
b4 = Button(x, text="*", bg="black", fg="white", height=3, width=8, command=lambda: click('*'))
b4.grid(row=2, column=3)

b1 = Button(x, text="4", bg="black", fg="white", height=3, width=8, command=lambda: click('4'))
b1.grid(row=3, column=0)
b2 = Button(x, text="5", bg="black", fg="white", height=3, width=8, command=lambda: click('5'))
b2.grid(row=3, column=1)
b3 = Button(x, text="6", bg="black", fg="white", height=3, width=8, command=lambda: click('6'))
b3.grid(row=3, column=2)
b4 = Button(x, text="-", bg="black", fg="white", height=3, width=8, command=lambda: click('-'))
b4.grid(row=3, column=3)

b1 = Button(x, text="1", bg="black", fg="white", height=3, width=8, command=lambda: click('1'))
b1.grid(row=4, column=0)
b2 = Button(x, text="2", bg="black", fg="white", height=3, width=8, command=lambda: click('2'))
b2.grid(row=4, column=1)
b3 = Button(x, text="3", bg="black", fg="white", height=3, width=8, command=lambda: click('3'))
b3.grid(row=4, column=2)
b4 = Button(x, text="+", bg="black", fg="white", height=3, width=8, command=lambda: click('+'))
b4.grid(row=4, column=3)

b1 = Button(x, text="+/-", bg="black", fg="white", height=3, width=8, command=lambda: click(''))
b1.grid(row=5, column=0)
b2 = Button(x, text="0", bg="black", fg="white", height=3, width=8, command=lambda: click('0'))
b2.grid(row=5, column=1)
b3 = Button(x, text=".", bg="black", fg="white", height=3, width=8, command=lambda: click('.'))
b3.grid(row=5, column=2)
b4 = Button(x, text="=", bg="black", fg="white", height=3, width=8, command=equal)
b4.grid(row=5, column=3)

x.mainloop()
