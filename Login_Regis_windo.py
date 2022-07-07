from tkinter import *
root=Tk()
root.geometry("400x500")
root.title("Login_Regis_windo")
def th():
  f3=Frame()
  f3.place(x=0,y=0,width=400,height=500)
  l1=Label(root,text="Thank You",font=("Arial",20))
  l1.place(x=120,y=170)

def show():
  f1=Frame()
  f1.place(x=0,y=0,width=400,height=500)
  b3=Button(root,text="<--",font=("Arial",20),bg="blue",fg="white",command=home)
  b3.place(x=0,y=0)
  l1=Label(root,text="Login page",font=("Arial",20))
  l1.place(x=170,y=0)
  l2=Label(root,text="Name :",font=("Arial",19))
  l2.place(x=3,y=100)
  e1=Entry(root,font=("Arial",16))
  e1.place(x=130,y=110)
  l3=Label(root,text="Pass :",font=("Arial",19))
  l3.place(x=3,y=200)
  e2=Entry(root,font=("Arial",16),show="*")
  e2.place(x=130,y=210)
  b4=Button(root,text="Submit",font=("Arial",20),bg="blue",fg="white",command=th)
  b4.place(x=130,y=300)
  
def show1():
  f1=Frame()
  f1.place(x=0,y=0,width=400,height=500)
  b3=Button(root,text="<--",font=("Arial",20),bg="blue",fg="white",command=home)
  b3.place(x=0,y=0)
  l1=Label(root,text="Regis page",font=("Arial",20))
  l1.place(x=170,y=0)
  l2=Label(root,text="Name :",font=("Arial",19))
  l2.place(x=3,y=100)
  e1=Entry(root,font=("Arial",16))
  e1.place(x=130,y=110)
  l3=Label(root,text="Pass :",font=("Arial",19))
  l3.place(x=3,y=200)
  e2=Entry(root,font=("Arial",16),show="*")
  e2.place(x=130,y=210)
  l4=Label(root,text="CPass :",font=("Arial",19))
  l4.place(x=3,y=300)
  e3=Entry(root,font=("Arial",16),show="*")
  e3.place(x=130,y=310)
  b4=Button(root,text="Submit",font=("Arial",20),bg="blue",fg="white",command=th)
  b4.place(x=130,y=400)

def home():
  f2=Frame()
  f2.place(width=400,height=500)
  b1=Button(root,text="Login",font=("Arial",20),bg="blue",fg="white",command=show)
  b1.grid(pady=150,padx=70,row=0,column=0)

  b2=Button(root,text="Regis",font=("Arial",20),bg="blue",fg="white",command=show1)
  b2.grid(pady=20,padx=30,row=0,column=1)

home()



root.mainloop()
