import tkinter as tk

def setWindow():
    window = tk.Tk()
    window.geometry("500x500")
    window["background"] ='#856ff8'
    return window


def setListbox(window,messages):
    var = tk.Variable(value=messages)
    m_listbox = tk.Listbox(window, listvariable=var, bg="#856ff8", fg="#fff",font=10, height=20,width=50 ,selectmode=tk.EXTENDED)
    m_listbox.pack()



#m_array =["a","b","c","d","e","f"]


#m_window = setWindow()
#setListbox(m_window, m_array)
#m_window.mainloop()