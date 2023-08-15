import tkinter as tk
import pyperclip
pyperclip.copy('this text is copied to your clipboard because you used this calculator, thank you for using this calculator :)')
spam = pyperclip.paste()
class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
    #create widgets
        self.firstNumberEntry = tk.Entry(bd = 0)
        self.plusSign = tk.Label(text = "-")
        self.secondNumberEntry = tk.Entry(bd = 0)
        self.equalSign = tk.Label(text = "=")
        self.resultLabel = tk.Label(text = "Result...", bg = "green", fg = "white")
        self.calculateButton = tk.Button(text = "Calculate", command = self.calculate, bd = 0, relief = "flat")
        self.calculateButton.config(activebackground = self.calculateButton.master.cget("bg"))

        #place widgets
        self.firstNumberEntry.pack(side = "left")
        self.plusSign.pack(side = "left")
        self.secondNumberEntry.pack(side = "left")
        self.equalSign.pack(side = "left")
        self.resultLabel.pack(side = "left")
        self.calculateButton.pack(side = "left")

    def calculate(self):
            try:
                first_value = float(self.firstNumberEntry.get())
                second_value = float(self.secondNumberEntry.get())
                result = first_value - second_value
                self.resultLabel.config(text = str(result), bg = "green", fg = "white")

            except ValueError:
                self.resultLabel.config(text="No number/s", bg="red", fg="black")

#create the app
app = Application()
app.master.frame()
app.master.title("Calculator (minus)")
app.master.minsize(width=50, height=50)

#start the program
app.mainloop()
