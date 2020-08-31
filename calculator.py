import tkinter as tk

class Interface:

    font = ("Sans Serif", 20)
    button_styling = {"font": font, "bg": "#262525", "fg": "#2349de", "relief": tk.FLAT}
    grid_styling = {"sticky": tk.N + tk.S + tk.E + tk.W, "padx": 1, "pady": 1}
    symbols = ["+", "-", "*", "/"]

    def __init__(self, master):
        self.master = master

        self.entry = tk.Entry(self.master,
                                bd = 2,
                                bg = "#262525",
                                fg = "#2349de",
                                font = Interface.font,
                                relief = tk.FLAT
                             )

        self.entry.grid(row = 0, column = 0,
                        columnspan= 3,
                        pady = 5,
                        padx = 5,
                        ipady = 14
                        )

        #make the number buttons
        for a in range(10):
            self.button= tk.Button(self.master,
                                    text = a,
                                    cnf = Interface.button_styling ,
                                    command = lambda a=a: self.insert(a),
                                    )

            self.button.config(width = 0, height = 2)

            if a == 0:
                self.button.grid(row = 4, column = a, cnf = Interface.grid_styling)
            elif 0<a and a<4:
                self.button.grid(row = 3, column = a - 1, cnf = Interface.grid_styling)
            elif 3<a and a<7:
                self.button.grid(row = 2, column = a - 4, cnf = Interface.grid_styling)
            else :
                self.button.grid(row = 1, column = a - 7, cnf = Interface.grid_styling)

        #make the symbol and operator buttons
        for a in Interface.symbols :
            num = Interface.symbols.index(a)
            self.button = tk.Button(self.master,
                                    text = a,
                                    cnf = Interface.button_styling,
                                    command = lambda a=a: self.insert(a))

            self.button.config(width = 0, height = 2)

            if num < 2:
                self.button.grid(row = 4, column = num + 1, cnf = Interface.grid_styling)
            else :
                self.button.grid(row = 5, column = num - 2, cnf = Interface.grid_styling)

        # equals button
        self.button = tk.Button(self.master,
                                text = "=",
                                cnf = Interface.button_styling,
                                command = self.evaluate
                                )

        self.button.grid(row = 5, column = 2, cnf = Interface.grid_styling)

        #clear button
        self.button = tk.Button(self.master,
                                text = "Clear",
                                cnf = Interface.button_styling,
                                command = self.clear)

        self.button.config(width = 0, height = 2)
        self.button.grid(row = 6, column = 0, columnspan= 3, cnf= Interface.grid_styling)

    def insert(self, num):
        self.entry.insert(tk.END, num)

    def evaluate(self):
        expression = str( self.entry.get() )
        result = eval(expression)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, result)

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg = "#1A1A1A")
    gui = Interface(root)
    root.tk.mainloop()
