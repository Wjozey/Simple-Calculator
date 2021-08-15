from tkinter import *

#Create a root and label widget

root = Tk()
root.title("Basic Calculator")
# myLabel1 = Label(root, text="Calc")
# myLabel2 = Label(root, text="row2")
# #Dispay the label on the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)


e = Entry(root, width=40, borderwidth=3)
e.grid(row=0, column=0, columnspan=3,padx=10,pady=10)

# e.insert(0, "")


# Defining a button operation(op) function and Creating Buttons
def button_op(number):
#    e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))


def reset():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    # second_number = e.get()
    # global s_num
    # s_num = int(second_number)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    else:
        e.insert(0, f_num / int(second_number))

def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


# button nos.

button_1 = Button(root, text="1", padx=30, pady=30, command=lambda: button_op(1))
button_2 = Button(root, text="2", padx=30, pady=30, command=lambda: button_op(2))
button_3 = Button(root, text="3", padx=30, pady=30, command=lambda: button_op(3))
button_4 = Button(root, text="4", padx=30, pady=30, command=lambda: button_op(4))
button_5 = Button(root, text="5", padx=30, pady=30, command=lambda: button_op(5))
button_6 = Button(root, text="6", padx=30, pady=30, command=lambda: button_op(6))
button_7 = Button(root, text="7", padx=30, pady=30, command=lambda: button_op(7))
button_8 = Button(root, text="8", padx=30, pady=30, command=lambda: button_op(8))
button_9 = Button(root, text="9", padx=30, pady=30, command=lambda: button_op(9))
button_0 = Button(root, text="0", padx=70, pady=30, command=lambda: button_op(0))
button_plus = Button(root, text="+", padx=30, pady=70, command= button_add)
button_minus = Button(root, text="-", padx=30, pady=30, command= button_minus)
button_divide = Button(root, text="/", padx=30, pady=30, command= button_divide)
button_multiply = Button(root, text="*", padx=30, pady=30, command= button_multiply)
button_equal = Button(root, text="=", padx=30, pady=70, command= button_equal)
button_reset = Button(root, text="C", padx=30, pady=30, command= reset)
button_decimal = Button(root, text=".", padx=30, pady=30, command=lambda: button_decimal())



button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=0, columnspan=2)
button_plus.grid(row=2,column=3, rowspan=2)
button_minus.grid(row=1, column=3)
button_divide.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_equal.grid(row=4, column=3, rowspan=2)
button_reset.grid(row=1, column=0)
button_decimal.grid(row=5, column=2)





root.mainloop()