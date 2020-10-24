import os
from datetime import date
from datetime import datetime
from time import sleep

hora = 3600

#Funções da semana
def segunda():
    if now.hour == 16:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        quit()
def terca():
    if now.hour == 18:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        quit()
def quarta():
    if now.hour == 10:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        sleep(hora * 6)
    elif now.hour == 16:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        quit()
def quinta():
    if now.hour == 9:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        sleep(hora * 6)
    elif now.hour == 15:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        quit()
def sexta():
    if now.hour == 10:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        sleep(hora * 3)
    elif now.hour == 13:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        sleep(hora * 2)
    elif now.hour == 15:
        os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
        quit()


while True:
    now = datetime.now()
    data = date(now.year, now.month, now.day)
#segunda
    if data.isoweekday() == 1:
        segunda()  
#terça
    elif data.isoweekday() == 2:
        terca()
#quarta
    elif data.isoweekday() == 3:
        quarta()
#quinta
    elif data.isoweekday() == 4:
        quinta()
#sexta
    elif data.isoweekday() == 5:
        sexta()
    elif data.isoweekday() == 6 or 7:
        print("É feriado danado, vai dormir.")
        quit()
    sleep(120)
    

