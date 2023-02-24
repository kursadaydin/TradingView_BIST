
from tradingview_ta import TA_Handler, Interval, Exchange
import tkinter as tk


def getResult(stock_id):
  #m_GUI_Window =m_GUI.setWindow()
  
  stock = TA_Handler(
    symbol=stock_id,
    screener="turkey",
    exchange="BIST",
    interval=Interval.INTERVAL_1_HOUR,
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
      message = str(stock.symbol) + " " + "\n Oscillators : "+str(m_oscillators['RECOMMENDATION']) + "\n Moving Averages : "+str(m_moving_averages['RECOMMENDATION'])
      print(message)
      
     
  except:
    pass
  
  def setArray(result):
    temp_message_array =[]
    temp_message_array.append(result)
    tk.setListbox(window=setWindow(), messages=temp_message_array)
    setWindow().mainloop()


  def setWindow():
    window = tk.Tk()
    window.geometry("500x500")
    window["background"] ='#856ff8'
    return window


  def setListbox(window,messages):
      var = tk.Variable(value=messages)
      m_listbox = tk.Listbox(window, listvariable=var, bg="#856ff8", fg="#fff",font=10, height=20,width=75 ,selectmode=tk.EXTENDED)
      m_listbox.pack()


