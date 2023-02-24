
from tradingview_ta import TA_Handler, Interval, Exchange
import tkinter as tk

class Manager:

  m_message_array =[]
  def getResult(self, stock_id):
    #m_GUI_Window =m_GUI.setWindow()
    
    stock = TA_Handler(
      symbol=stock_id,
      screener="turkey",
      exchange="BIST",
      interval=Interval.INTERVAL_1_DAY,
      timeout=None)
    check_oscillators = False
    check_moving_averages = False
    try:
      #m_indicators = stock.get_analysis().indicators
      m_oscillators = stock.get_analysis().oscillators
      m_moving_averages = stock.get_analysis().moving_averages
      if m_oscillators['RECOMMENDATION'] == "STRONG_BUY" or m_oscillators['RECOMMENDATION'] == "BUY":
        check_oscillators = True
      if m_moving_averages['RECOMMENDATION'] == "STRONG_BUY" or m_moving_averages['RECOMMENDATION'] == "BUY":
        check_moving_averages = True
      if(check_oscillators and check_moving_averages):
        message = str(stock.symbol) + " " + " Oscillators : "+str(m_oscillators['RECOMMENDATION']) + " Moving Averages : "+str(m_moving_averages['RECOMMENDATION'])
        self.m_message_array.append(message)
        print(self.m_message_array)
        
    except:
      pass

  def setGUI(self,messages):
    window = tk.Tk()
    window.geometry("500x500")
    window["background"] ='#856ff8'
    var = tk.Variable(value=messages)
    m_listbox = tk.Listbox(window, listvariable=var, bg="#856ff8", fg="#fff",font=10, height=20,width=75 ,selectmode=tk.EXTENDED)
    m_listbox.pack(expand=True, fill=tk.BOTH)
    window.mainloop()
    return window


  


