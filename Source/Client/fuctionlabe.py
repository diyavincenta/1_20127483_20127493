import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import tkinter.scrolledtext as st
import json
from client import*
import requests
import time

import datetime
TODAY = datetime.date.today()
D1 =TODAY.strftime("%d/%m/%y")
print(D1)

def getData(date,month,year,company,winsearch):
        #ve farme hien thi

        framelist=Frame(winsearch,width=129,bg="white")
        framelist.grid(row=2,column=0)
        tableList = st.ScrolledText(framelist, height = 100, width = 110)
        tableList.pack()

        DateUserInput = datetime.date(int(year), int(month), int(date))
        Today = datetime.date.today()

        # dateNow=int(date)
        # MonthNow=int(month)
        # YearNow=int(year)

        if(DateUserInput > Today):
             tableList.insert(END, "INVALID DATE OR NOT EXIST DATA")

        else:   
        
            data=year+month+date
            print(data)
            send(data)
            data=receive()
            
            try:
                time.sleep(1)
            except data!="":
                exit
            send(company)
            #data2=receive()
            data2=receive()
            
            
            print(data2)
            num=0
            while (num!=int(data2)):
                Company=receive()
                sell=receive()
                buy=receive()
                brand=receive()
                brand1=receive()

                dataGold = f"Company: {Company} - Buy: {buy} - Sell: {sell} - Brand: {brand} - Brand1: {brand1}"
                
                print(dataGold)
                tableList.insert(END, dataGold)
                tableList.insert(END, "\n")
                num=num+1
    
def OMG():
    winsearch =Tk()
    winsearch.title('GoldPrices Search')
    winsearch.geometry("1090x613")
    
    str =D1
    day=int(str[0] + str[1])
    mo=int(str[3] + str[4])

    # Add something to the left
    frame1=Frame(winsearch,width=100,bg="white")
    frame1.grid(row=0,column=0,padx=165,pady=0,ipadx=0,ipady=0)

    goldprice=Label(frame1,text="GOLDPRICE",font="Helvetica 50 ",bg="white",fg="RED")
    goldprice.grid(row=0,column=0,padx=20,ipadx=1,ipady=1)

    framedate=Frame(frame1,width=100,bg="white")
    framedate.grid(row=1,column=0,padx=0,pady=0,ipadx=0,ipady=0)

    Datelabel=Label(framedate,text="DATE:",font=(16),bg="white",fg="Black")
    Datelabel.grid(row=1,column=0,ipadx=1,ipady=1)

    date=tk.StringVar()
    date=ttk.Combobox(framedate,width=2,textvariable=date,font = "Helvetica 13 ")
    date['values']=('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18'
    ,'19','20','21','22','23','24','25','26','27','28','29','30','31')
    date['state'] = 'readonly'
    date.bind('<<ComboboxSelected>>')
    date.current(day-1)
    date.grid(row=1,column=1)
    print(date.get())

    month=tk.StringVar()
    month=ttk.Combobox(framedate,width=2,textvariable=month,font = "Helvetica 13 ")
    month['values']=('01','02','03','04','05','06','07','08','09','10','11','12')
    month['state'] = 'readonly'
    month.bind('<<ComboboxSelected>>')
    month.current(mo-1)
    month.grid(row=1,column=2)
    print(month.get())

    year=tk.StringVar()
    year=ttk.Combobox(framedate,width=4,textvariable=month,font = "Helvetica 13 ")
    year['values']=('2021','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011')
    year['state'] = 'readonly'
    
    year.current(0)
    year.grid(row=1,column=3)
    print(year.get())
    none=Label(framedate,text="____",font="Helvetica 50 ",bg="white",fg="white")
    none.grid(row=1,column=4)

    companylabel=Label(framedate,text="TYPE:",font=(16),bg="white",fg="Black")
    companylabel.grid(row=1,column=5,ipadx=1,ipady=1)
    
    
    company=tk.StringVar()
    company=ttk.Combobox(framedate,width=9,textvariable=company,font = "Helvetica 13 ")
    company['values']=('none','V??ng SJC' ,'V??ng SJC 1L','V??ng nh???n SJC 99,99 0,5 ch???','V??ng nh???n SJC 99,99 1 ch???, 2 ch???, 5 ch???','V??ng n??? trang 99,99%','V??ng n??? trang 99%',
    'V??ng n??? trang 75%','V??ng n??? trang 58,3%','V??ng n??? trang 41,7%','AVPL / DOJI CT bu??n',' AVPL / DOJI CT l???'
    ,'AVPL / DOJI HCM bu??n','AVPL / DOJI HCM l???','AVPL / DOJI ??N bu??n','AVPL / DOJI ??N l???' ,'AVPL / DOJI HN bu??n'
    ,'AVPL / DOJI HN l???' ,'Nguy??n li??u 9999 - HN' ,'Nguy??n li??u 999 - HN' ,'Kim Ng??u ','Kim Th???n T??i' ,'L???c Ph??t T??i',
    'Kim Ng??n T??i','H??ng Th???nh V?????ng' ,'Nh???n H.T.V' ,'Nguy??n li???u 99.99','Nguy??n li???u 9999','Nguy??n li???u 999','Nguy??n li???u 999' ,
    'N??? trang 99.99','N??? trang 99.9','N??? trang 99','N??? trang 18k','N??? trang 16k','N??? trang 68 ','N??? trang 14k' 
    ,'N??? trang 10k','SJC','SJC*')   
    company['state'] = 'readonly'
    company.current(0)

    company.grid(row=1,column=6)
    none=Label(frame1,text="___",font="Helvetica 50 ",bg="white",fg="white")
    none.grid(row=1,column=2)
    spsearch=Button(frame1,text="Search",font=(5),width=10,bg="white",command=lambda:getData(date.get(),month.get(),year.get(),company.get(),winsearch))
    spsearch.grid(row=1,column=3)
  
    winsearch.protocol("WM_DELETE_WINDOW")
    winsearch.mainloop()

