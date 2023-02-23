import tkinter as tk

def setGUI(message):

    window = tk.Tk()
    window.geometry("500x200")
    window["background"] ='#856ff8'
    greeting = tk.Label(text=message, bg='#856ff8', fg='#fff', padx=10, pady=10, font=10)
    greeting.pack()
    window.mainloop()