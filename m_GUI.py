import tkinter as tk

def setWindow():
    window = tk.Tk()
    window.geometry("500x500")
    window["background"] ='#856ff8'
    return window


def setListbox(window,messages):
    m_listbox = tk.Listbox(window, listvariable=messages, bg="#856ff8", fg="#fff",font=10)
    m_listbox.pack()