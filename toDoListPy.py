import tkinter as tk

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x500")
        

        self.topLabel = tk.Label(text="To do List", font=("Arial", 13))
        self.entertBtn = tk.Button(text="Enter", command=self.addtask)
        self.entry = tk.Entry( width= 50)

        self.topLabel.place(x= 315, y = 5)
        self.entry.place(x=150, y=30)
        self.entertBtn.place(x = 460, y = 30)

        self.list = []

        self.window.mainloop()

    def addtask(self):
        task_text = self.entry.get()

        nowe_zadanie = task(self.window, task_text, len(self.list), self.list)
        self.list.append(nowe_zadanie)

    



class task:
        def __init__(self, window, text, index, list):
            self.list = list
            self.text = text
            self.label = tk.Label(window, text=self.text, font=("Arial", 11))
            self.label.place(x=150, y=80 + (index * 30))

            self.delBtn = tk.Button(text="Delete task", command = lambda: self.deleteTask( self.text))
            self.delBtn.place(x=250, y=80 )

        def deleteTask(self, text):
            self.label.destroy()
            self.delBtn.destroy()

Gui()