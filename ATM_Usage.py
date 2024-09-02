#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox

atm=tk.Tk()
atm.geometry('700x500+400+200')
atm.title('ATM SYSTEM')
atm.configure(bg='Lime')
atm.resizable()

def Submit():
    
    cnum1=IntVar()
    pin1=IntVar()
    
    
    cnum1=e1.get()
    pin1=e2.get()
    global bal1
    bal1=IntVar()
    bal1=45000  

        
    
    if cnum1=="12345" and pin1=="134":
        print("Welcome Mam/Sir to our ATM.")
        messagebox.showinfo('Welcome',f'Mam/Sir to our ATM')
        win=tk.Tk()
        win.geometry('700x500+400+200')
        win.title('ATM SYSTEM')
        win.configure(bg='yellow')              
        
        def balance1():
            
            print("Your current balance is of",bal1)
            messagebox.showinfo('Balance',f'Your Current Balance is of {bal1}')
        def billpay1():
            bill=tk.Tk()
            bill.geometry('700x500+400+200')
            bill.title('Bill Payment')
            bill.configure(bg='gold')
            
                      
            
            
            def paym():
                
                paid=IntVar()
                
                paid=e4.get()
                
                
                print("You have successfully paid your Bill",paid)
                
                bala1=int(bal1)
                paymt=int(paid)
                bala1=bala1-paymt
                print("Your current balance is of",bala1)
                
                
                
                messagebox.showinfo('Bill Paid',f'You have successfully paid your bill {paid}')
                messagebox.showinfo('Balance',f'Your Current Balance is of {bala1}')
                
            li1=Label(bill,text="Bill Payment",width=32,bg="red",                   
                  font=('Gentium Plus',20),fg='white')
            li1.place(x=150,y=70)
            
            l1=Label(bill,text="Enter Amount to Pay",bg='Blue',width=17,bd=3,                     
                     font=('timesnewroman',13,'bold'),fg='yellow',relief='sunken')
            l1.place(x=190,y=200)
                
            e4=Entry(bill,width=30, borderwidth=2, relief='sunken', font=('Gentium Plus',10))
            e4.place(x=410,y=200)
                
            b1=Button(bill,text='Pay Amount',bg='Cyan',width=13,height=3, relief='solid',command=paym,                 
                      font=('Calibiri',13))
            b1.place(x=320,y=300)
            bill.mainloop()
            
            
        def withdraw():
            wit=tk.Tk()
            wit.geometry('700x500+400+200')
            wit.title('Withdraw Amount')
            wit.configure(bg='plum')
            
            
            
            
            
            def wtd():
                
                wd=IntVar()
                
                wd=e4.get()
                
                
                print("You have successfully withdrawn your money",wd)
                
                bala1=int(bal1)
                witd=int(wd)
                bala1=bala1-witd
                print("Your current balance is of",bala1)
                
                
                
                messagebox.showinfo('Bill Paid',f'You have successfully withdraw money of {witd}')
                messagebox.showinfo('Balance',f'Your Current Balance is of {bala1}')
                
            li1=Label(wit,text="Withdraw Amount",width=32,bg="red",                   
                  font=('Gentium Plus',20),fg='white')
            li1.place(x=150,y=70)
            
            l1=Label(wit,text="Enter Amount to Withdraw",bg='Blue',width=22,bd=3,                     
                     font=('timesnewroman',13,'bold'),fg='yellow',relief='sunken')
            l1.place(x=150,y=200)
                
            e4=Entry(wit,width=30, borderwidth=2, relief='sunken', font=('Gentium Plus',10))
            e4.place(x=410,y=200)
                
            b1=Button(wit,text='Withdraw Amount',bg='Cyan',width=20,height=3, relief='solid',command=wtd,                 
                      font=('Calibiri',13))
            b1.place(x=300,y=300)
            wit.mainloop()
        
        def depst():
            dep=tk.Tk()
            dep.geometry('700x500+400+200')
            dep.title('Deposit Money')
            dep.configure(bg='palegreen')
            
            
            
            
            def deps():
                depm=IntVar()
                
                depm=e5.get()
                
                
                
                print("You have successfully deposited the amount of ",depm)
                bala1=int(bal1)
                depam=int(depm)
                bala1=bala1+depam
                print("Your current balance is of",bala1)
                
                messagebox.showinfo('Amount Deposited',f'You have successfully deposited money {depm}')
                messagebox.showinfo('Balance',f'Your Current Balance is of {bala1}')
                #bal1=bala1
                #print(bal1)
                
            l1=Label(dep,text="Deposit Money",width=32,bg="red",                   
                  font=('Gentium Plus',20),fg='white')
            l1.place(x=150,y=70)
            
            l5=Label(dep,text="Enter Amount to deposit",bg='Blue',width=20,bd=3,                  
                     font=('timesnewroman',13,'bold'),fg='yellow',relief='sunken')
            l5.place(x=190,y=200)
                
            e5=Entry(dep,width=30, borderwidth=2, relief='sunken', font=('Gentium Plus',10))
            e5.place(x=410,y=200)
                
            b1=Button(dep,text='Deposit Amount',bg='Cyan',width=15,height=3, relief='solid',command=deps,               
                      font=('Calibiri',13))
            b1.place(x=320,y=300)
            dep.mainloop()
            
                
        li1=Label(win,text="Welcome to your Bank Account",width=32,bg="red",                   
                  font=('Gentium Plus',20),fg='white')
        li1.place(x=150,y=70)
            
        b1=Button(win,text='Balance',bg='Cyan',width=13,height=3, relief='solid',command=balance1,
                  font=('Calibiri',13))
        b1.place(x=220,y=150)
            
        b2=Button(win,text='Bill Pay',bg='Cyan',width=13,height=3, relief='solid',command=billpay1,
                  font=('Calibiri',13))
        b2.place(x=400,y=150)    
        
        b3=Button(win,text='Deposit',bg='Cyan',width=13,height=3, relief='solid',command=depst,
                  font=('Calibiri',13))
        b3.place(x=220,y=300)
            
        b4=Button(win,text='Withdraw',bg='Cyan',width=13,height=3, relief='solid',command=withdraw,
                  font=('Calibiri',13))
        b4.place(x400,y=300)
            
        win.mainloop()
        
        
        
    else:
        print("Invalid Credentials")
        messagebox.showerror('Error','You are not a Bank Account Holder.')

li1=Label(atm,text="Atm System",width=20,bg="red",
        font=('Gentium Plus',32),fg='white')
li1.place(x=150,y=100)

l1=Label(atm,text="Enter Card Number",bg='Blue',width=17,bd=3,
        font=('timesnewroman',13,'bold'),fg='yellow',relief='sunken')
l1.place(x=190,y=200)

l2=Label(atm,text="Pin",bg='yellow',width=17,bd=3,
        font=('timesnewrol',13,'bold'),fg='Blue',relief='sunken')
l2.place(x=190,y=250)


e1=Entry(atm,width=30, borderwidth=2, relief='sunken', font=('Gentium Plus',10))
e1.place(x=410,y=200)

e2=Entry(atm,width=30, borderwidth=2, relief='sunken', font=('Gentium Plus',10))
e2.place(x=410,y=250)

b1=Button(atm,text='Submit',bg='Cyan',width=13,height=3, relief='solid',command=Submit,
          font=('Calibiri',13))
b1.place(x=320,y=300)
atm.mainloop()


# In[ ]:




