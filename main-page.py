from tkinter import*
import subprocess
import pymysql
import pymysql.cursors
from tkinter import messagebox

def deposit():
    
    win=Tk()
    win.config(bg="orange")
    win.geometry("400x350")
    win.title("Welcome to the Deposit")
    def dep():
        card=tx.get()
        pin=tx2.get()
        amount=tx3.get()
        typ='deposit'
        try:
            conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
            a=conn.cursor()
            a.execute("select * from bank where Card_no='"+card+"' and Pin='"+pin+"'")
            a.execute("insert into type(Card_no,Amount,type) values('"+card+"','"+amount+"','"+typ+"')")
            a.execute("update bank set Amount = Amount + '"+amount+"' where Pin='"+pin+"'")
            conn.commit()
            result=a.fetchall()
            count=a.rowcount
            if count>0:
                messagebox.showinfo("Deposit","successful")
            else:
                messagebox.showerror("Deposit","Failed")
        except:
            conn.rollback()
            messagebox.error("Deposit","failed")
        conn.close()
    lb=Label(win,text="Card_no",font=20).grid(row=0,column=0,padx=10,pady=10)
    lb2=Label(win,text="Pin",font=20).grid(row=1,column=0,padx=10,pady=10)
    lb3=Label(win,text="Amount",font=20).grid(row=3,column=0,padx=10,pady=10)
    tx=Entry(win,font=20)
    tx.grid(row=0,column=2,padx=20,pady=10)
   
    tx2=Entry(win,font=20)
    tx2.grid(row=1,column=2,padx=20,pady=10)
    
    tx3=Entry(win,font=20)
    tx3.grid(row=3,column=2,padx=20,pady=10)
    btn=Button(win,text="Deposit",font=20,bd=10,relief="raised",command=dep).place(x=180,y=200)

#WITHDRAW CASH
def withdraw():
    win=Tk()
    win.config()
    win.geometry("400x350")
    win.title("Welcome to the Withdraw cash")
    def wit():
        card=w.get()
        pin=w1.get()
        Amount=w2.get()
        typ='withdraw'
        try:
            conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
            a=conn.cursor()
            a.execute("select * from bank where Card_no='"+card+"' and Pin='"+pin+"'")
            a.execute("insert into type(Card_no,Amount,type) values('"+card+"','"+Amount+"','"+typ+"')")
            a.execute("update bank set Amount = Amount - '"+Amount+"' where Pin='"+pin+"' and Card_no='"+card+"'")
            conn.commit()
            result=a.fetchall()
            count=a.rowcount
            if count>0:
                messagebox.showinfo("Withdraw","successful")
            else:
                messagebox.showerror("withdraw","Failed")
        except:
            conn.rollback()
            messagebox.showinfo("Withdraw","failed")
        conn.close()
    lb=Label(win,text="Card_no",font=20).grid(row=0,column=0,padx=10,pady=10)
    lb2=Label(win,text="Pin",font=20).grid(row=1,column=0,padx=10,pady=10)
    
    lb3=Label(win,text="Amount",font=20).grid(row=3,column=0,padx=10,pady=10)
    
    w=Entry(win,font=20)
    w.grid(row=0,column=2,padx=20,pady=10)
    w1=Entry(win,font=20)
    w1.grid(row=1,column=2,padx=20,pady=10)
    w2=Entry(win,font=20)
    w2.grid(row=3,column=2,padx=20,pady=10)
    btn=Button(win,text="Withdraw",font=20,bd=10,relief="raised",command=wit).place(x=180,y=200)

#BALANCE ENQUIRY
def checkbalance():
    win=Tk()
    win.config()
    win.geometry("350x300")
    win.title("Welcome to the Balance Enquiry")
    
 
    def Balance():
       a=bal.get()
       b=bal2.get()
       conn = pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
       mydb=conn.cursor()
       mydb.execute("select Amount from Bank where Card_no='"+a+"'")
       result=mydb.fetchall()
       count=mydb.rowcount
       if count>0:
           for row in result:
              {
              messagebox.showinfo("Balance",result)
              }
       else:
           messagebox.showinfo("Balance","INVALID Card Number and PIN")

    lb=Label(win,text="Enter Card Number",font=10).grid(row=0,column=0,padx=10,pady=10)
    lb2=Label(win,text="Enter Pin",font=10).grid(row=1,column=0,padx=10,pady=10)
    bal=Entry(win)
    bal.grid(row=0,column=1)
    bal2=Entry(win)
    bal2.grid(row=1,column=1)
    btn=Button(win,text="Show",command=Balance,font=10,width=10,bd=10,relief="raised").place(x=150,y=180)

#TRANSFER FUND
def transfer():
    win=Tk()
    win.config(bg="orange")
    win.geometry("500x350")
    win.title("Welcome to the Transfer ")
    def trans():
        from1=tx.get()
        pin=tx2.get()
        amount=tx3.get()
        to=tx4.get()
        typ='transfer'
        try:
            conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
            a=conn.cursor()
            a.execute("update bank set Amount=Amount -'"+amount+"' where Card_no='"+from1+"' and Pin='"+pin+"'")
            a.execute("insert into type(Card_no,Amount,type) values('"+from1+"','"+amount+"','"+typ+"')")
            a.execute("update bank2 set Amount=Amount +'"+amount+"' where Card_no='"+to+"'")
            conn.commit()
            print("transfer done")
        except:
            conn.rollback()
            print("transfer failed")
        conn.close()

    lb=Label(win,text="Enter Card No. From",font=10,bg="orange").grid(row=0,column=0,padx=10,pady=10)
    lb2=Label(win,text="Enter Pin",font=10,bg="orange").grid(row=1,column=0,padx=10,pady=10)
    lb3=Label(win,text="Enter Amount",font=10,bg="orange").grid(row=3,column=0,padx=10,pady=10)
    lb4=Label(win,text="Enter Card No. To",font=10,bg="orange").grid(row=4,column=0,padx=10,pady=10)

    tx=Entry(win,font=10)
    tx.grid(row=0,column=2,padx=20,pady=10)
    tx2=Entry(win,font=10)
    tx2.grid(row=1,column=2,padx=20,pady=10)
    tx3=Entry(win,font=10)
    tx3.grid(row=3,column=2,padx=20,pady=10)
    tx4=Entry(win,font=10)
    tx4.grid(row=4,column=2,padx=20,pady=10)
    btn=Button(win,text="Transfer",font=20,bd=10,relief="raised",command=trans).place(x=180,y=240)

#MINI STATEMENT
def mini():
    state=Tk()
    state.config(bg="orange")
    state.geometry('400x250')
    state.title("welecome to mini statement")
    def login():
        min=Tk()
        min.geometry('1000x800')
        card=entry.get()
        lb=Label(min,text="MINI STATEMENT",font=('times 30 bold'),bd=10,fg="Red",width=30,relief="sunken").grid(row=0,column=1,padx=350,pady=20)
        frame=Frame(min)
        frame.grid(row=3,column=1,padx=20,pady=20)

        conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
        a=conn.cursor()
        a.execute("select * from type where Card_no='"+card+"'")
        results=a.fetchall()
        count=a.rowcount
        num=2
        text=Text (frame,font="vendata 16")
        text.insert(END,"\n\tCard_no\t\tAmount\t\tType")
        text.grid(row=num,column=0)
        for i in results:
            text.insert(END,"\n\t{0}\t\t{1}\t\t{2}".format(i[0],i[1],i[2]))
            num=num+1
    
        
    lb=Label(state,text="Enter Card No.",font=10).grid(row=0,column=0,padx=10,pady=10)
    lb1=Label(state,text="Enter Pin",font=10).grid(row=1,column=0,padx=10,pady=10)
    entry=Entry(state,font=10)
    entry.grid(row=0,column=1,padx=10,pady=10)
    entry1=Entry(state,font=10)
    entry1.grid(row=1,column=1,padx=10,pady=10)
    btn=Button(state,text="Mini statement",font=10,bd=10,relief="raised",command=login).place(x=100,y=150)

#CHANGE PIN
def change():
    ch=Tk()
    ch.geometry("400x300")
    def chp():
        card=cha.get()
        op=cha1.get()
        np=cha2.get()
        rp=cha3.get()
        try:
            if(rp==np):
                conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
                a=conn.cursor()
                a.execute("update bank set Pin='"+np+"' where Card_no='"+card+"' and Pin='"+op+"'")
                conn.commit()
                messagebox.showinfo("Change Pin","successful")
            else:
                messagebox.showinfo("Change Pin","Failed")
        except:
            conn.rollback()
            print("not updated")
        conn.close()

        
    ch.title("welcome to the change pin ")
    lb=Label(ch,text="Enter Card Number",font=20)
    lb.grid(row=0,column=0,padx=10,pady=10)
    lb1=Label(ch,text="Enter old pin",font=20)
    lb1.grid(row=1,column=0,padx=10,pady=10)
    lb2=Label(ch,text="Enter the new pin",font=20).grid(row=3,column=0,padx=10,pady=10)
    lb3=Label(ch,text="Renter the new pin",font=20).grid(row=5,column=0,padx=10,pady=10)
    cha=Entry(ch)
    cha.grid(row=0,column=1,padx=10,pady=10)
    cha1=Entry(ch)
    cha1.grid(row=1,column=1,padx=10)
    cha2=Entry(ch)
    cha2.grid(row=3,column=1,padx=10)
    cha3=Entry(ch)
    cha3.grid(row=5,column=1,padx=10)
    btn=Button(ch,text="Change pin",font=15,bd=5,relief="raised",command=chp).place(x=150,y=220)
#FAST CASH    
def fast():
    ch=Tk()

    def cash():
        card=en.get()
        pin=en1.get()
        typ='Fast cash'
        amount='200'
        try:
            conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
            my=conn.cursor()
            my.execute("select * from bank where Card_no='"+card+"' and Pin='"+pin+"'")
            my.execute("insert into type(Card_no,Amount,type) values('"+card+"','"+amount+"','"+typ+"')")
            my.execute("update bank set Amount= Amount - 200 where Card_no='"+card+"' and Pin='"+pin+"'")
            conn.commit()
            result=my.fetchall()
            count=my.rowcount
            if count>0:
                messagebox.showinfo("Fast Cash","successful")
            else:
                messagebox.showerror("Fast Cash","Failed")
        except:
            conn.rollback()
            print("not updated")
        conn.close()
    def cash1():
        card=en.get()
        pin=en1.get()
        typ='Fast cash'
        amount='500'
        try:
            conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
            my=conn.cursor()
            my.execute("select * from bank where Card_no='"+card+"' and Pin='"+pin+"'")
            my.execute("insert into type(Card_no,Amount,type) values('"+card+"','"+amount+"','"+typ+"')")
            my.execute("update bank set Amount= Amount - 500 where Card_no='"+card+"' and Pin='"+pin+"'")
            conn.commit()
            result=my.fetchall()
            count=my.rowcount
            if count>0:
                messagebox.showinfo("Fast Cash","successful")
            else:
                messagebox.showerror("Fast Cash","Failed")
        except:
            conn.rollback()
            print("not updated")
        conn.close()
    def cash2():
        card=en.get()
        pin=en1.get()
        typ='Fastcash'
        amount='1000'
        try:
            conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
            my=conn.cursor()
            my.execute("select * from bank where Card_no='"+card+"' and Pin='"+pin+"'")
            my.execute("insert into type(Card_no,Amount,type) values('"+card+"','"+amount+"','"+typ+"')")
            my.execute("update bank set Amount= Amount - 1000 where Card_no='"+card+"' and Pin='"+pin+"'")
            conn.commit()
            result=my.fetchall()
            count=my.rowcount
            if count>0:
                messagebox.showinfo("Fast Cash","successful")
            else:
                messagebox.showerror("Fast Cash","Failed")
        except:
            conn.rollback()
            print("not updated")
        conn.close()
    def cash3():
        card=en.get()
        pin=en1.get()
        typ='Fast cash'
        amount='2000'
        try:
            conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
            my=conn.cursor()
            my.execute("select * from bank where Card_no='"+card+"' and Pin='"+pin+"'")
            my.execute("insert into type(Card_no,Amount,type) values('"+card+"','"+amount+"','"+typ+"')")
            my.execute("update bank set Amount= Amount - 2000 where Card_no='"+card+"' and Pin='"+pin+"'")
            conn.commit()
            result=my.fetchall()
            count=my.rowcount
            if count>0:
                messagebox.showinfo("Fast Cash","successful")
            else:
                messagebox.showerror("Fast Cash","Failed")
        except:
            conn.rollback()
            print("not updated")
        conn.close()
    ch.geometry("400x300")
    ch.title("welcome to the Fast Cash ")
    lb=Label(ch,text="Enter Card Number",font=20).grid(row=0,column=0,padx=10,pady=10)
    lb2=Label(ch,text="Enter pin",font=20).grid(row=1,column=0,padx=10,pady=10)
    en=Entry(ch)
    en.grid(row=0,column=1,padx=10,pady=10)
    en1=Entry(ch)
    en1.grid(row=1,column=1,padx=10)
    btn=Button(ch,text="200",font=15,bd=10,relief="raised",command=cash).grid(row=2,column=0,padx=10,pady=10)
    btn2=Button(ch,text="500",font=15,bd=10,relief="raised",command=cash1).grid(row=2,column=1,padx=10,pady=10)
    btn3=Button(ch,text="1000",font=15,bd=10,relief="raised",command=cash2).grid(row=3,column=0,padx=15,pady=15)
    brn4=Button(ch,text="2000",font=15,bd=10,relief="raised",command=cash3).grid(row=3,column=1,padx=15,pady=15)

#UPDATE CONTACT
def update():
    up=Tk()
    up.geometry("450x340")
    up.title("welcome to the Update contact ")
    def upda():
        card=upd.get()
        pin=upd1.get()
        oc=upd2.get()
        nc=upd3.get()
        rc=upd4.get()
        try:
            if(rc==nc):
                conn=pymysql.connect(host='localhost',user='root',password='123456',db='deepanshu')
                a=conn.cursor()
                a.execute("update bank set Contact_no='"+nc+"' where Card_no='"+card+"' and Pin='"+pin+"' and Contact_no='"+oc+"'")
                conn.commit()
                messagebox.showinfo("update contact","successful")
            else:
                messagebox.showinfo("update contact","Failed")
        except:
            conn.rollback()
            print("not updated")
        conn.close()
    lb=Label(up,text="Enter Card Number",font=20).grid(row=0,column=0,padx=10,pady=10)
    lb2=Label(up,text="Enter pin",font=20).grid(row=1,column=0,padx=10,pady=10)
    lb3=Label(up,text="Enter the old Contact number",font=20).grid(row=2,column=0,padx=10,pady=10)
    lb4=Label(up,text="Enter the new Contact number",font=20).grid(row=3,column=0,padx=10,pady=10)
    lb5=Label(up,text="Renter the new Contact number",font=20).grid(row=4,column=0,padx=10,pady=10)
    upd=Entry(up)
    upd.grid(row=0,column=1,padx=10,pady=10)
    upd1=Entry(up)
    upd1.grid(row=1,column=1,padx=10)
    upd2=Entry(up)
    upd2.grid(row=2,column=1,padx=10)
    upd3=Entry(up)
    upd3.grid(row=3,column=1,padx=10)
    upd4=Entry(up)
    upd4.grid(row=4,column=1,padx=10)
    btn=Button(up,text="Update",font=15,bd=5,relief="raised",command=upda).place(x=150,y=250)   

lin=Tk()
lin.config(bg="sky blue")
lin.geometry("600x370")
lin.title("Welcome to the main page")
Deposit=Button(lin,text="Deposit Cash",width=20,bd=10,relief="raised",font=20,command=deposit).grid(row=0,column=0,padx=10,pady=10,ipadx=5,ipady=5)
withdraw=Button(lin,text="Withdraw Cash",width=20,bd=10,relief="raised",font=20,command=withdraw).grid(row=1,column=0,padx=10,pady=10,ipadx=5,ipady=5)           
Balance=Button(lin,text="Balance Enquiry",width=20,bd=10,relief="raised",font=20,command=checkbalance).grid(row=2,column=0,padx=10,pady=10,ipadx=5,ipady=5)
Transfer=Button(lin,text="Transfer Fund",width=20,bd=10,relief="raised",font=20,command=transfer).grid(row=3,column=0,padx=10,pady=10,ipadx=5,ipady=5)
Mini=Button(lin,text="Mini Statement",width=20,bd=10,relief="raised",font=20,command=mini).grid(row=0,column=2,padx=20,pady=10,ipadx=5,ipady=5)
Fast=Button(lin,text="Fast Cash",bd=10,width=20,relief="raised",font=20,command=fast).grid(row=1,column=2,padx=20,pady=10,ipadx=5,ipady=5)
Change=Button(lin,text="Change Pin",bd=10,width=20,relief="raised",font=20,command=change).grid(row=2,column=2,padx=15,pady=10,ipadx=5,ipady=5)
Update=Button(lin,text="Update Contact",width=20,bd=10,relief="raised",font=20,command=update).grid(row=3,column=2,padx=20,pady=10,ipadx=5,ipady=5)
lin.mainloop()
input()




