from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import subprocess
#login
def main():
    user=b.get()
    passwor=c.get()
    #mysql connection 
    conn=pymysql.connect(host='localhost',user='root',password='*******',db='deepanshu')
    a=conn.cursor()
    a.execute("select * from login where username='"+user+"'and Password='"+passwor+"'")
    result=a.fetchall()
    count=a.rowcount
    
    if(count>0):
        subprocess.run("main-page.py")

    else:
        messagebox.showinfo("message","not login")
    
first=Tk()
first.config(bg="orange")
first.geometry("350x300")
lb=Label(first,text="Login",font=15,width=30,bd=5,relief="raised",fg="black")
lb.grid(row=0,column=0,padx=5,pady=5)
lin=Frame(first,width=500,height=500,bd=10,relief="raised")
lin.place(x=30,y=50)
lb1=Label(lin,font=10,text="Username")
lb1.grid(row=1,column=0,padx=10,pady=10)
lb2=Label(lin,text="Password",font=10)
lb2.grid(row=2,column=0,padx=10,pady=10)
b=StringVar()
en=Entry(lin,textvariable=b)
en.grid(row=1,column=1,padx=10,pady=10)
c=StringVar()
en2=Entry(lin,textvariable=c)
en2.grid(row=2,column=1,padx=10,pady=10)
btn=Button(lin,text="Login",bd=5,relief="raised",command=main,font=10)
btn.grid(row=3,column=1,padx=15,pady=15)
lin.mainloop()
first.mainloop()
