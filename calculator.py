from tkinter import *
root = Tk()
root.title("Calculator")

# define the entry box
EntryBox = Entry(root, width = 35, borderwidth = 4)
#defining the cick functions
def button_click(num):
    current_number = EntryBox.get()
    EntryBox.delete(0, END)
    EntryBox.insert(0, str(current_number) + str(num) )

def button_clear():
    EntryBox.delete(0, END)

def button_add():
    global math
    math = 'add'
    fnumber = EntryBox.get()
    global first_number
    first_number = int(fnumber)
    EntryBox.delete(0, END)

def button_subtract():
    global math
    math = 'subtract'
    fnumber = EntryBox.get()
    global first_number
    first_number = int(fnumber)
    EntryBox.delete(0, END)

def button_divide():
    global math
    math = "divide"
    fnumber = EntryBox.get()
    global first_number
    first_number = int(fnumber)
    EntryBox.delete(0, END)

def button_multiply():
        global math
        math = "multiply"
        fnumber = EntryBox.get()
        global first_number
        first_number = int(fnumber)
        EntryBox.delete(0, END)

def button_equals():
    second_number = EntryBox.get()
    EntryBox.delete(0, END)
    if math == 'add':
        EntryBox.insert(0, first_number + int(second_number))
    elif math == 'subtract':
        EntryBox.insert(0, first_number - int(second_number))
    elif math == 'divide':
        EntryBox.insert(0, first_number / int(second_number))
    elif math == 'multiply':
            EntryBox.insert(0, first_number * int(second_number))

#define the buttons
button1 = Button(root, padx = 35, pady=10, text="1", command = lambda: button_click(1) )
button2 = Button(root,padx = 35, pady=10, text="2",command = lambda: button_click(2) )
button3 = Button(root,padx = 35, pady=10, text="3",command = lambda: button_click(3) )
button4 = Button(root, padx = 35, pady=10,text="4",command = lambda: button_click(4) )
button5 = Button(root,padx = 35, pady=10, text="5",command = lambda: button_click(5) )
button6 = Button(root, padx = 35, pady=10,text="6",command = lambda: button_click(6) )
button7 = Button(root,padx = 35, pady=10, text="7",command = lambda: button_click(7) )
button8 = Button(root,padx = 35, pady=10, text="8",command = lambda: button_click(8) )
button9 = Button(root,padx = 35, pady=10, text="9",command = lambda: button_click(9) )
button0 = Button(root, padx = 35, pady=10,text="0",command = lambda: button_click(0) )
button_add = Button(root,padx = 34, pady=10, text ='+',command =button_add)
button_equals = Button(root,padx = 34, pady=10, text= '=',command =button_equals)
button_clear = Button(root,padx = 35, pady=10, text="clear",command = button_clear)
button_subtract = Button(root, padx=35, pady= 10, text= '-', command= button_subtract)
button_multiply = Button(root, padx=35, pady=10, text = 'x', command= button_multiply)
button_divide = Button(root, padx=35, pady=10, text = '/', command = button_divide )

#put the buttons on the screen
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)
button0.grid(row = 4, column = 1)
button_add.grid(row = 4, column = 2)
button_equals.grid(row = 6, column=0 )
button_clear.grid(row=6,column=1, columnspan=3)
button_subtract.grid(row=4, column=0)
button_multiply.grid(row=3, column=2)
button_divide.grid(row=5, column=0)

EntryBox.grid(row = 0, column=0,columnspan = 3,  padx= 10, pady = 10)
root.mainloop()
