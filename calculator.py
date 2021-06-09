from tkinter import *;

root = Tk()
root.title("Simple Calculator")
#root.maxsize(250, 250)
#root.minsize(250, 250)

#Main functions

recentNumber = ""
recentOperation = ""

def addValuesToDisplay(number):
    current = str(display.get())
    new = str(current) + str(number)
    display.delete(0, END)
    display.insert(0, new)
    
def clearScreenFunction():
    display.delete(0, END)
    
def buttonAdd():
    global recentNumber
    global recentOperation
    recentNumber = display.get()
    recentOperation = "+"
    display.delete(0, END)
    
def buttonSubstract():
    global recentNumber
    global recentOperation
    recentNumber = display.get()
    recentOperation = "-"
    display.delete(0, END)
    
def buttondivide():
    global recentNumber
    global recentOperation
    recentNumber = display.get()
    recentOperation = "/"
    display.delete(0, END)
    
def buttonMultiply():
    global recentNumber
    global recentOperation
    recentNumber = display.get()
    recentOperation = "*"
    display.delete(0, END)
    
def startOperation():
    if recentOperation == "+":
        result = int(recentNumber) + int(display.get())
        display.delete(0, END)
        display.insert(0, result)
    elif recentOperation == "-":
        result = int(recentNumber) - int(display.get())
        display.delete(0, END)
        display.insert(0, result)
    elif recentOperation == "*":
        result = int(recentNumber) * int(display.get())
        display.delete(0, END)
        display.insert(0, result)
    elif recentOperation == "/":
        result = int(recentNumber) / int(display.get())
        display.delete(0, END)
        display.insert(0, result)

#objects

#Text fields
display = Entry(root)

#Buttons
number1 = Button(root, text="1", padx=40, pady=20, command=lambda: addValuesToDisplay(1))
number2 = Button(root, text="2", padx=40, pady=20, command=lambda: addValuesToDisplay(2))
number3 = Button(root, text="3", padx=40, pady=20, command=lambda: addValuesToDisplay(3))
number4 = Button(root, text="4", padx=40, pady=20, command=lambda: addValuesToDisplay(4))
number5 = Button(root, text="5", padx=40, pady=20, command=lambda: addValuesToDisplay(5))
number6 = Button(root, text="6", padx=40, pady=20, command=lambda: addValuesToDisplay(6))
number7 = Button(root, text="7", padx=40, pady=20, command=lambda: addValuesToDisplay(7))
number8 = Button(root, text="8", padx=40, pady=20, command=lambda: addValuesToDisplay(8))
number9 = Button(root, text="9", padx=40, pady=20, command=lambda: addValuesToDisplay(9))
number0 = Button(root, text="0", padx=40, pady=20, command=lambda: addValuesToDisplay(0))
addButton = Button(root, text="+", padx=38, pady=20, command=buttonAdd)
subsButton = Button(root, text="-", padx=41, pady=20, command=buttonSubstract)
divButton = Button(root, text="/", padx=41, pady=20, command=buttondivide)
mulButton = Button(root, text="*", padx=40, pady=20, command=buttonMultiply)
enterButton = Button(root, text="=", padx=132, pady=20, command=startOperation)
clearButton = Button(root, text="CLEAR", padx=22, pady=20, command=clearScreenFunction)

#Positioning
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
number7.grid(row=1, column=0)
number8.grid(row=1, column=1)
number9.grid(row=1, column=2)
number4.grid(row=2, column=0)
number5.grid(row=2, column=1)
number6.grid(row=2, column=2)
number1.grid(row=3, column=0)
number2.grid(row=3, column=1)
number3.grid(row=3, column=2)
number0.grid(row=4, column=0)
addButton.grid(row=4, column=1)
subsButton.grid(row=4, column=2)
divButton.grid(row=5, column=0)
mulButton.grid(row=5, column=1)
clearButton.grid(row=5, column=2)
enterButton.grid(row=6, column=0, columnspan=3)

root.mainloop()