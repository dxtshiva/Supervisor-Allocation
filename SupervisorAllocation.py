import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import random as rd

class Start(tk.Tk):
    rname='14526'
    uname='147894'
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RegrPage,LoginPage,StuPage,SupPage,RsPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def sure(self):
        vara=messagebox.askquestion('Confirm','Are you sure to logout?')
        if vara=='yes':
            self.show_frame(StartPage)
               
    def verify(self,u,p,h):
        if u.get()=='' or p.get=='':
            messagebox.showinfo('Alert','Username or password cannot be blank.')
        elif h=='Student':
            crsr.execute("select * from student where username= binary '"+u.get()+"' ;")
            data=crsr.fetchall()
        elif h=='Supervisor':
            crsr.execute("select * from supervisor where username= binary '"+u.get()+"' ;")
            data=crsr.fetchall()
        else:
            messagebox.showinfo('Alert','Select the type of user.')
        if not data:
            messagebox.showerror('Error','Username not found')
        else:
            
            self.rname=data[0][1]
            self.uname=data[0][1]
            pswd=data[0][6]
            if p.get()!=pswd:
                messagebox.showerror('Error',"Incorrect Password")   
            else:
                if h=="Student" and data[0][7]=='null':
                    messagebox.showinfo('Alert','No supervisor allocated. Please request for a supervisor and then login again.')
                    self.show_frame(RsPage)
                elif h=='Student':
                    self.show_frame(StuPage)
                elif h=='Supervisor':
                    self.show_frame(SupPage)   
                    
   
        
    def check(self,fn,us,ps,cp,rg,mn,em,ty,sp):
        a=fn.get().strip()
        b=us.get().strip()
        c=ps.get().strip()
        d=cp.get().strip()
        e=rg.get().strip()
        f=mn.get().strip()
        g=em.get().strip()
        h=ty.strip()
        i=sp.strip()
        if(a=='' or b=='' or c=='' or d=='' or e==''or f==''or g=='' or h=='--Select--' or i=='--Select--' ):
            messagebox.showerror('Error','All fields are mandatory.')
        elif(c!=d):
            messagebox.showerror("Incorrect","Passwords do not match.")
        else:
            if h=='Student':
                crsr.execute("select * from student where username= binary '"+b+"' OR reg_no= binary'"+e+"' ;")
                data=crsr.fetchall()
            elif h=='Supervisor':
                crsr.execute("select * from supervisor where username= binary '"+b+"' OR uid= binary'"+e+"' ;")
                data=crsr.fetchall()
            
            if not data:
                #crsr.execute("select uid from supervisor where specialization='"+i+"';")
                #spr=crsr.fetchall()
                #sid=spr[rd.randint(0,len(spr)-1)][0]
                if h=='Student':
                    crsr.execute("insert into student values('"+a+"','"+e+"','"+i+"','"+f+"','"+g+"','"+b+"','"+c+"','null') ;")
                else:
                    crsr.execute("insert into supervisor values('"+a+"','"+e+"','"+i+"','"+f+"','"+g+"','"+b+"','"+c+"') ;")
                messagebox.showinfo("Success","User successfully registered.")
                self.show_frame(StartPage)
            elif data[0][5]==b:
                messagebox.showerror('Error',"Username already exists. Please retry.")
            elif data[0][1]==e:
                messagebox.showerror('Error','Reg.No/UID already registered.')
                
    def submit(self,regno,usrn):
        p=regno.get()
        q=usrn.get()
        if p.strip()=='' or q.strip()=='':
            messagebox.showerror("Incomplete","No field can be left blank !")
        else:
            crsr.execute("Select specialization, username,supervisorid from student where reg_no='"+p+"';")
            det=crsr.fetchall()
            if not det:
                messagebox.showerror("Invalid","Record not found for the given Reg.No./UID !")
            else:
                if q!=det[0][1]:
                    messagebox.showerror("Incorrect","Data do not match. Please check your entry !")
                elif det[0][2]!='null':
                     messagebox.showinfo("Alert","Supervisor already allocated. Please login to continue.")
                else:
                    crsr.execute("select uid from supervisor where specialization='"+det[0][0]+"';")
                    spr=crsr.fetchall()
                    sid=spr[rd.randint(0,len(spr)-1)][0]
                    crsr.execute("update student set supervisorid ='"+sid+"' where reg_no='"+p+"';")
                    crsr.execute("select name from supervisor where uid='"+sid+"';")
                    udet=crsr.fetchall()
                    messagebox.showinfo("Success",udet[0][0]+", UID: "+sid+" has been allocated as you supervisor.")
                    
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #controller.title("Start Page")
        #controller.geometry('800x728')
        controller.configure(background = "grey");
        tk.Label(self, text="Welcome to Supervisor Allocation System",font=("Times New Roman",20), fg="black",height=3).grid(row=0,columnspan=7,padx=370,pady=25);
        tk.Button(self, text="LOGIN", fg="green" ,height=2,width=8,font=("Times New Roman",12),command=lambda:controller.show_frame(LoginPage)).grid(row=2,column=2);
        tk.Button(self, text="NEW USER", fg="green" ,height=2,width=8,font=("Times New Roman",12),command=lambda: controller.show_frame(RegrPage)).grid(row=2,column=3);
        tk.Button(self, text="REGISTER FOR SUPERVISOR", fg="green" ,height=2,width=25,font=("Times New Roman",12),command=lambda: controller.show_frame(RsPage)).grid(row=2,column=4);

class RegrPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #controller.title("Registration Form")
        #controller.geometry('1024x728')
        controller.configure(background = "grey");
        fn = tk.StringVar()
        us = tk.StringVar()
        ps = tk.StringVar()
        cp = tk.StringVar()
        rg = tk.StringVar()
        mn = tk.StringVar()
        em = tk.StringVar()
        sp = tk.StringVar()
        dflt=tk.StringVar()
        dflt.set('--Select--')
        dflt1=tk.StringVar()
        dflt1.set('--Select--')
        tk.Button(self, text="Back", fg="green" ,height=1,width=8,font=("Times New Roman",12),command=lambda:controller.show_frame(StartPage)).grid(row=0,column=0,pady=30)
        tk.Label(self ,text = "Full Name",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 1,column = 0)
        tk.Label(self ,text = "Username",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 1,column = 2)
        tk.Label(self ,text = "Password",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 2,column = 0)
        tk.Label(self ,text = "Confirm Password",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 2,column = 2)
        tk.Label(self ,text = "Reg.no./UID",font=("Times New Roman",18)).grid(padx=30,pady=30,row =3 ,column = 0)
        tk.Label(self ,text = "Mobile Number",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 3,column = 2)
        tk.Label(self ,text = "Email",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 4,column = 0)
        tk.Label(self ,text = "Type",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 4,column = 2)

        tk.Entry(self,font=("Times New Roman",18),textvariable=fn).grid(padx= 30,row = 1,column = 1)
        tk.Entry(self,font=("Times New Roman",18),textvariable=us).grid(padx =30,row = 1,column = 3)
        tk.Entry(self,show ="*",font=("Times New Roman",18),textvariable=ps).grid(row = 2,column = 1)
        tk.Entry(self,show ="*",font=("Times New Roman",18),textvariable=cp).grid(row = 2,column = 3)
        tk.Entry(self,font=("Times New Roman",18),textvariable=rg).grid(padx= 30,row = 3,column = 1)
        tk.Entry(self,font=("Times New Roman",18),textvariable=mn).grid(padx =30,row = 3,column = 3)
        tk.Entry(self,font=("Times New Roman",18),textvariable=em).grid(row = 4,column = 1)
        lk=tk.OptionMenu(self,dflt,'--Select--',"Student","Supervisor")
        lk.configure(font=("Times New Roman",16),width=11,height=1)
        lk.grid(row =4,column = 3)
        tk.Label(self ,text = "Specialization",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 5,column = 0)
        lk1=tk.OptionMenu(self,dflt1,'--Select--',"Electronics Hardwaring","Computer Architecture","Electrical Devices","Mechanical Manufacturing","Cyber Security","Data Analytics")
        lk1.configure(font=("Times New Roman",16),width=25,height=1)
        lk1.grid(row = 5,column = 1)
        tk.Button(self ,text="Submit",font=("Times New Roman",15),command=lambda: controller.check(fn,us,ps,cp,rg,mn,em,dflt.get(),dflt1.get())).grid(row=6,column=2)
        
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        controller.title("")
        #controller.geometry('1024x728')
        controller.configure(background = "white");
        uname=tk.StringVar()
        pwd=tk.StringVar()
        dflt=tk.StringVar()
        dflt.set('--Select--')
        tk.Button(self, text="Back", fg="green" ,height=1,width=8,font=("Times New Roman",12),command=lambda:controller.show_frame(StartPage)).grid(row=0,column=0,columnspan=3);
        tk.Label(self, text="Login Page",font=("Times New Roman",20), fg="black",height=3).grid(row=0,column=2,columnspan=5,padx=370,pady=25);
        tk.Label(self, text="Username",font=("Times New Roman",18), fg="black",height=3).grid(row=1,column=3,pady=5);
        tk.Entry(self,font=("Times New Roman",16), fg="black",textvariable=uname).grid(row=1,column=4,pady=5);
        tk.Label(self, text="Password",font=("Times New Roman",18), fg="black",height=3).grid(row=2,column=3,pady=5);
        tk.Entry(self,show='*',font=("Times New Roman",16), fg="black",textvariable=pwd).grid(row=2,column=4,pady=5);
        tk.Label(self ,text = "Type",font=("Times New Roman",18)).grid(padx=30,pady=30,row = 3,column = 3)
        lk=tk.OptionMenu(self,dflt,'--Select--',"Student","Supervisor")
        lk.configure(font=("Times New Roman",16),width=11,height=1)
        lk.grid(row = 3,column = 4)
        tk.Button(self, text="LOGIN", fg="green" ,height=2,width=8,font=("Times New Roman",12),command=lambda:controller.verify(uname,pwd,dflt.get())).grid(row=5,column=2,columnspan=3,pady=3);

class StuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent) 
        crsr.execute("select name, supervisorid from student where reg_no='"+controller.rname+"';")
        detail=crsr.fetchall()
        crsr.execute("select * from supervisor where uid='"+detail[0][1]+"';")
        detail1=crsr.fetchall()
        tk.Label(self,text=detail[0][0],font=("Times New Roman",16),fg='black').grid(row=0,column=0,padx='40',pady='20')
        tk.Button(self,text='LOGOUT',fg='Black',height=1,width=8,font=('Times New Roman',16),command=lambda:controller.sure()).grid(row=0,column=3,columnspan=2)
        tk.Label(self,text='Supervisor Name',font=("Times New Roman",16),fg='black').grid(row=1,column=0,padx='30',pady='40')
        tk.Label(self,font=('Times New Roman',16),fg='black',text=detail1[0][0]).grid(row=1,column=1,padx='30',pady='40')
        tk.Label(self,text='UID',font=("Times New Roman",16),fg='black').grid(row=1,column=3,padx='30',pady='40')
        tk.Label(self,font=('Times New Roman',16),fg='black',text=detail1[0][1]).grid(row=1,column=4,padx='30',pady='40')
        tk.Label(self,text='Email',font=("Times New Roman",16),fg='black').grid(row=2,column=0,padx='30',pady='40')
        tk.Label(self,font=('Times New Roman',16),fg='black',text=detail1[0][4]).grid(row=2,column=1,padx='30',pady='40')
        tk.Label(self,text='Supervisor Name',font=("Times New Roman",16),fg='black').grid(row=2,column=3,padx='30',pady='40')
        tk.Label(self,font=('Times New Roman',16),fg='black',text=detail1[0][3]).grid(row=2,column=4,padx='30',pady='40')
        tk.Label(self,text='Specialization and Description',font=("Times New Roman",16),fg='black').grid(row=3,column=0,padx='30',pady='40')
        tk.Label(self,text=detail1[0][2]+'\n'+dictr[detail1[0][2]],font=('Times New Roman',16),fg='black',height=10,width=100).grid(row=3,column=1,columnspan=8,padx='30',pady='40')
        
class SupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)    
        crsr.execute("select * from supervisor where uid='"+controller.uname+"';")
        detail=crsr.fetchall()
        sname=tk.Label(self,text=detail[0][0],font=("times new roman",16)).grid(row=0,column=1,padx=70,pady=20,columnspan=3)
        uid=tk.Label(self,text=controller.uname,font=("times new roman",16)).grid(row=0,column=5,padx=70,pady=20,columnspan=3)
        logout=tk.Button(self,text='LOGOUT',fg='Black',height=1,width=8,font=('Times New Roman',16),command=lambda:controller.sure()).grid(row=0,column=8,padx=70,pady=20,columnspan=3)
        label = tk.Label(self, text="List of Allocated Students", font=("Times New Roman",25)).grid(row=2,column=3,columnspan=10,pady=40,padx=220)
        cols = ( 'Reg.No./UID No','Name', 'Mobile no','Email id')
        listBox = ttk.Treeview(self, columns=cols, show='headings')
        for col in cols:
            listBox.heading(col, text=col)  
        listBox.grid(row=4,column=3,columnspan=10,padx=200)
        regno=[]
        username=[]
        uname=[]
        email=[]
        tempList=[]
        crsr.execute("select * from student where supervisorid='"+controller.uname+"';")
        p=crsr.fetchall()
        for row in p:
                b=row[0]
                c=row[1]
                e=row[3]
                d=row[4]

                regno.append(b)
                username.append(c)
                uname.append(e)
                email.append(d)
                y=len(regno)
                x=[regno,username,uname,email]

        for j in range(y):
                temp=[]
                for i in x:
                    temp.append(i[j])
                tempList.append(temp)

        i=0    
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (regno,username,uname,email) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(regno,username,uname,email))
                

class RsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent) 
        regno=tk.StringVar()
        usrn=tk.StringVar()
        tk.Button(self, text="Back", fg="green" ,height=1,width=8,font=("Times New Roman",12),command=lambda:controller.show_frame(StartPage)).grid(row=0,column=0,columnspan=3,pady=20);
        tk.Label(self,text="REQUEST FOR SUPERVISOR",font=("Times New Roman",20),fg='black').grid(row=1,column=3,padx='240',pady='20',columnspan=8)
        tk.Label(self,text='Reg.No./UID',font=("Times New Roman",16),fg='black').grid(row=2,column=2,padx='50',pady='40')
        tk.Entry(self,font=("Times New Roman",18),textvariable=regno).grid(padx= 30,row = 2,column = 3)
        tk.Label(self,text='Username',font=("Times New Roman",16),fg='black').grid(row=3,column=2,padx=50,pady=40)
        tk.Entry(self,font=("Times New Roman",18),textvariable=usrn).grid(padx= 30,row = 3,column = 3)
        tk.Button(self, text="Submit", fg="green" ,height=1,width=8,font=("Times New Roman",12),command=lambda:controller.submit(regno,usrn)).grid(row=4,column=2,columnspan=3,pady=40);
        
mydb = mysql.connector.connect(host="localhost",user='root',passwd="123",buffered=True)
crsr = mydb.cursor()
crsr.execute("use python;")
crsr.execute('set autocommit=1;')

dictr={"Hello":"Null","Electronics Hardwaring":"\nElectronic hardwaring consists of interconnected electronic components which perform analog \n or logic operations on received and locally stored information to produce as output or store \nresulting new information or to provide control for output actuator mechanisms.",
       "Computer Architecture":"\nComputer architecture is a set of rules and methods that describe the functionality, \n organization, and implementation of computer systems. Some definitions\n of architecture define it as describing the capabilities and programming model \nof a computer but not a particular implementation.",
       "Electrical Devices":"\nElectrical devices take the energy of electrical current, the flow of electrons in a conductor, and transform it in simple ways into some other form of energy—most likely light, heat, or motion. An electric device is one that directly uses electrical energy to perform a task.",
       "Mechanical Manufacturing":"\nMechanical Manufacturing is all about turning energy into power and \n motion through the design of clever mechanical systems. Because \n it's such a broad field, you could expect to find a mechanical and \n manufacturing engineer almost anywhere that uses machines.",
       "Cyber Security":"\n Cyber security refers to the body of technologies, processes, \n and practices designed to protect networks, devices, programs, and \n data from attack, damage, or unauthorized access. Cyber \n security may also be referred to as information technology security.",
       "Data Analytics":"\nData analytics is the science of analyzing raw data in order \n to make conclusions about that information. Many of the \n techniques and processes of data analytics have been automated into \n mechanical processes and algorithms that work over raw data for human consumption."}

sp=Start()
sp.mainloop()
