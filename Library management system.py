from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from datetime import date,timedelta

home=Tk()
home.title("Login")
home.geometry("800x800")
whitespace=" "
home.title(95*whitespace+"Welcome")
home.config(bg="violetred")
mainframe=Frame(home,bg="skyblue",relief=GROOVE,bd=15)
mainframe.place(x=10,y=10,width=780,height=780)
'''bg=ImageTk.PhotoImage(file=r"D:\dra.Jpg")
bg_label=Label(mainframe,image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)'''
label=Label(mainframe,text="WELCOME TO HOME PAGE",font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
label.pack(side=TOP,fill=X)

def exit():
    exit=messagebox.askyesno(" ","Do you want to exit")
    if exit>0:
        home.destroy()
        return
def combb():
    value=usertype.get()
    if value=="admin":
        f1=Toplevel(home)
        f1.geometry("1000x1000")
        f1.config(bg="skyblue")
        whitespace=" "
        f1.title(150*whitespace+"login")
        login=Label(f1,text="WELCOME TO LOGIN PAGE",font=("TimesNewRomans",20,"bold"),bg="skyblue",bd=10,fg="black")
        user=StringVar()
        pas=StringVar()
        def password123():
            username3=user1.get()
            password3=pas1.get()
            if username3=="" or password3=="":
                messagebox.showerror("","Blank username or password is not allowed")
            elif username3=="Amirtha" and password3=="Amiramirtha":
                mh=Toplevel(home)
                mh.geometry("800x800")
                mh.config(bg="lightpink")
                whitespace=" "
                mh.title(150*whitespace+"Admin page")
                def nstudent():
                    stu=Toplevel(mh)
                    stu.geometry("1500x800")
                    stu.config(bg="lightpink")
                    whitespace=" "
                    stu.title(150*whitespace+"New student")
                    sid11=StringVar()
                    name11=StringVar()
                    branch11=StringVar()
                    course11=StringVar()
                    year11=StringVar()
                    def add():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("insert into student(sid,name,branch,course,year) values(%s,%s,%s,%s,%s)",(sid11.get(),name11.get(),branch11.get(),course11.get(),n.get()))
                        mysqldb.commit()
                        mysqldb.close()
                        messagebox.showinfo("","Successfully inserted")
                    def delete():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("delete from student where sid=%s",(sid11.get(),))
                        mysqldb.commit()
                        mysqldb.close()
                        messagebox.showinfo("","Successfully deleted")
                    def update():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("update student set name=%s,branch=%s,course=%s,year=%s where sid=%s",(name11.get(),branch11.get(),course11.get(),n.get(),sid11.get()))
                        mysqldb.commit()
                        mysqldb.close()
                        messagebox.showinfo("","Successfully update")
                    def display():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("select sid,name,branch,course,year from student ")
                        result=mysqlcon.fetchall()
                        print(result)

                        for i,(sid,name,branch,course,year) in enumerate(result,start=1):
                            tv.insert("","end",values=(sid,name,branch,course,year))

                        mysqldb.commit()
                        mysqldb.close()
                        
                    clgname=Label(stu,text="ADDING NEW STUDENT",font=("TimesNewRomans",20,"bold"),bg="skyblue",fg="black",bd=10,relief=GROOVE,justify="center")
                    clgname.pack(side=TOP,fill=X)
                    sid=Label(stu,text="Student id",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    sid.place(x=100,y=200)
                    sid1=Entry(stu,width=20,textvariable=sid11,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    sid1.place(x=300,y=200)
                    name=Label(stu,text="Name",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    name.place(x=100,y=270)
                    name1=Entry(stu,textvariable=name11,font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=4)
                    name1.place(x=300,y=270)
                    branch=Label(stu,text="Branch",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    branch.place(x=100,y=340)
                    branch1=Entry(stu,textvariable=branch11,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    branch1.place(x=300,y=340)
                    course=Label(stu,text="course",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    course.place(x=100,y=410)
                    course1=Entry(stu,textvariable=course11,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    course1.place(x=300,y=410)
                    year=Label(stu,text="Year",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    year.place(x=100,y=480)
                    n=StringVar()
                    year1=ttk.Combobox(stu,font=("TimesNewRomans",20),textvariable=n,width=20)
                    year1["value"]="I","II","III","IV"
                    year1.place(x=300,y=480)
                    subbut=Button(stu,text="Add",command=add,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    subbut.place(x=100,y=600)
                    delbut=Button(stu,text="delete",command=delete,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    delbut.place(x=300,y=600)
                    updatebut=Button(stu,text="Update",command=update,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    updatebut.place(x=500,y=600)
                    clsbut=Button(stu,text="Close",command=password123,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    clsbut.place(x=100,y=700)
                    dis=Button(stu,text="dis",command=display,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    dis.place(x=500,y=700)
                                        
                    frame=Frame(stu,bg="skyblue",bd=5,relief=GROOVE)
                    frame.place(x=650,y=80,width=600,height=635)
                    scroll_y=Scrollbar(frame,orient=VERTICAL)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    tv=ttk.Treeview(frame,column=("sid11","name11","branch11","course11","n"),yscrollcommand=scroll_y)
                    tv.heading("sid11",text="SID")
                    tv.heading("name11",text="Name")
                    tv.heading("branch11",text="Branch")
                    tv.heading("course11",text="Course")
                    tv.heading("n",text="Year")
                    tv["show"]="headings"
                    tv.column("sid11",width=20)
                    tv.column("name11",width=80)
                    tv.column("branch11",width=50)
                    tv.column("course11",width=50)
                    tv.column("n",width=50)
                    tv.pack(fill=BOTH,expand=1)

                def nbook():
                    bk=Toplevel(mh)
                    bk.geometry("1200x800")
                    bk.config(bg="lightpink")
                    whitespace=" "
                    bk.title(150*whitespace+"New student")
                    sid11=StringVar()
                    name11=StringVar()
                    price11=StringVar()
                    pub11=StringVar()
                    p_year11=StringVar()

                    def add():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("insert into book(id,name,publisher,price,p_year) values(%s,%s,%s,%s,%s)",(sid11.get(),name11.get(),pub11.get(),price11.get(),p_year11.get()))
                        mysqldb.commit()
                        mysqldb.close()
                        messagebox.showinfo("","Successfully inserted")
                    def delete():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("delete from book where id=%s",(sid11.get(),))
                        mysqldb.commit()
                        mysqldb.close()
                        messagebox.showinfo("","Successfully deleted")
                    def update():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("update book set name=%s,publisher=%s,price=%s,p_year=%s where id=%s",(name11.get(),pub11.get(),price11.get(),p_year11.get(),sid11.get()))
                        mysqldb.commit()
                        mysqldb.close()
                        messagebox.showinfo("","Successfully updated")
                    def display():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("select id,name,publisher,price,p_year from book ")
                        result=mysqlcon.fetchall()
                        print(result)

                        for i,(sid,name,publisher,price,p_year) in enumerate(result,start=1):
                            tv.insert("","end",values=(sid,name,publisher,price,p_year))

                        mysqldb.commit()
                        mysqldb.close()

        
            
                    clgname=Label(bk,text="ADDING NEW BOOK",font=("TimesNewRomans",20,"bold"),bg="skyblue",fg="black",bd=10,relief=GROOVE,justify="center")
                    clgname.pack(side=TOP,fill=X)
                    bid=Label(bk,text="Book id",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    bid.place(x=100,y=200)
                    bid=Entry(bk,textvariable=sid11,width=20,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    bid.place(x=300,y=200)
                    bname=Label(bk,text="Book Name",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    bname.place(x=100,y=270)
                    bname1=Entry(bk,textvariable=name11,font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=4)
                    bname1.place(x=300,y=270)
                    publisher=Label(bk,text="Publisher",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    publisher.place(x=100,y=340)
                    pub1=Entry(bk,textvariable=pub11,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    pub1.place(x=300,y=340)
                    price=Label(bk,text="Price",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    price.place(x=100,y=410)
                    price1=Entry(bk,textvariable=price11,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    price1.place(x=300,y=410)
                    p_year=Label(bk,text="Published_Year",font=("TimesNewRomans",15,"bold"),bg="white",fg="black",bd=5)
                    p_year.place(x=100,y=480)
                    p_year1=Entry(bk,textvariable=p_year11,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    p_year1.place(x=300,y=480)
                    subbut=Button(bk,text="Add",command=add,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    subbut.place(x=100,y=600)
                    delbut=Button(bk,text="delete",command=delete,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    delbut.place(x=300,y=600)
                    updatebut=Button(bk,text="Update",command=update,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    updatebut.place(x=500,y=600)
                    clsbut=Button(bk,text="Close",command=password123,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    clsbut.place(x=100,y=700)
                    dis=Button(bk,text="dis",command=display,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    dis.place(x=500,y=700)
                    
                    frame=Frame(bk,bg="skyblue",bd=5,relief=GROOVE)
                    frame.place(x=650,y=80,width=600,height=635)
                    scroll_y=Scrollbar(frame,orient=VERTICAL)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    tv=ttk.Treeview(frame,column=("sid11","name11","pub11","price11","p_year11"),yscrollcommand=scroll_y)
                    tv.heading("sid11",text="SID")
                    tv.heading("name11",text="Name")
                    tv.heading("pub11",text="Branch")
                    tv.heading("price11",text="Course")
                    tv.heading("p_year11",text="Year")
                    tv["show"]="headings"
                    tv.column("sid11",width=20)
                    tv.column("name11",width=80)
                    tv.column("pub11",width=50)
                    tv.column("price11",width=50)
                    tv.column("p_year11",width=50)
                    tv.pack(fill=BOTH,expand=1)
                def issuebook():
                    ib=Toplevel(mh)
                    ib.geometry("1200x800")
                    ib.config(bg="lightpink")
                    whitespace=" "
                    ib.title(150*whitespace+"New student")
                    
                    def add():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        id1=bid.get()
                        sid1=sid.get()
                        current_date=date.today().isoformat()
                        days_after=(date.today()+timedelta(days=30)).isoformat()
                        returnbook="no"
                        returndate="null"
                        mysqlcon.execute("insert into issue(id,sid,issuedate,duedate,returnbook,returndate) values(%s,%s,%s,%s,%s,%s)",(bid.get(),sid1,current_date,days_after,returnbook,returndate))
                        mysqldb.commit()
                        mysqldb.close()
                        messagebox.showinfo("","Successfully issued")
                    def display():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("select id,sid,issuedate,duedate from issue ")
                        result=mysqlcon.fetchall()
                        print(result)

                        for i,(id,sid,issuedate,duedate) in enumerate(result,start=1):
                            tv.insert("","end",values=(id,sid,issuedate,duedate))

                        mysqldb.commit()
                        mysqldb.close()
                
                    clgname=Label(ib,text="ISSUE BOOK",font=("TimesNewRomans",20,"bold"),bg="skyblue",fg="black",bd=10,relief=GROOVE,justify="center")
                    clgname.pack(side=TOP,fill=X)
                    bid=Label(ib,text="Book id",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    bid.place(x=100,y=200)
                    bid=Entry(ib,width=20,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    bid.place(x=300,y=200)
                    sid=Label(ib,text="student id",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    sid.place(x=100,y=270)
                    sid=Entry(ib,font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=4)
                    sid.place(x=300,y=270)
                    subbut=Button(ib,text="Submit",command=add,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    subbut.place(x=100,y=340)
                    clsbut=Button(ib,text="Close",command=password123,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    clsbut.place(x=300,y=340)
                    dis=Button(ib,text="display",command=display,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    dis.place(x=500,y=340)                    
                    frame=Frame(ib,bg="skyblue",bd=5,relief=GROOVE)
                    frame.place(x=650,y=80,width=600,height=635)
                    scroll_y=Scrollbar(frame,orient=VERTICAL)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    tv=ttk.Treeview(frame,column=("bid","sid","current_date","days_after"),yscrollcommand=scroll_y)
                    tv.heading("bid",text="BID")
                    tv.heading("sid",text="SID")
                    tv.heading("current_date",text="issuedate")
                    tv.heading("days_after",text="duedate")
               
                    tv["show"]="headings"
                    tv.column("bid",width=20)
                    tv.column("sid",width=80)
                    tv.column("current_date",width=50)
                    tv.column("days_after",width=50)
                  
                    tv.pack(fill=BOTH,expand=1)
                def returnbook():
                    rb=Toplevel(mh)
                    rb.geometry("1500x800")
                    rb.config(bg="lightpink")
                    whitespace=" "
                    rb.title(150*whitespace+"New student")
                    def update():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        id1=bid.get()
                        sid1=sid.get()
                        
                        returndate1=date.today().isoformat()
                        mysqlcon.execute("update issue set returnbook='Yes' where sid=%s",(sid.get(),))
                        mysqlcon.execute("update issue set returndate=%s where sid=%s",(returndate1,sid.get(),))
                        mysqldb.commit()
                        mysqldb.close()
                        messagebox.showinfo("","Successfully updated")
                    def display():
                        mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                        mysqlcon=mysqldb.cursor()
                        mysqlcon.execute("select id,sid,returnbook,returndate from issue ")
                        result=mysqlcon.fetchall()
                        print(result)

                        for i,(id,sid,returnbook,returndate) in enumerate(result,start=1):
                            tv.insert("","end",values=(id,sid,returnbook,returndate))

                        mysqldb.commit()
                        mysqldb.close()                    
                    clgname=Label(rb,text="RETURN BOOK",font=("TimesNewRomans",20,"bold"),bg="skyblue",fg="black",bd=10,relief=GROOVE,justify="center")
                    clgname.pack(side=TOP,fill=X)
                    bid=Label(rb,text="Book id",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    bid.place(x=100,y=200)
                    bid=Entry(rb,width=20,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                    bid.place(x=300,y=200)
                    sid=Label(rb,text="student id",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                    sid.place(x=100,y=270)
                    sid=Entry(rb,font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=4)
                    sid.place(x=300,y=270)
                    subbut=Button(rb,text="Submit",command=update,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    subbut.place(x=100,y=340)
                    delbut=Button(rb,text="Close",command=password123,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    delbut.place(x=300,y=340)
                    dis=Button(rb,text="display",command=display,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    dis.place(x=500,y=340)

                    frame=Frame(rb,bg="skyblue",bd=5,relief=GROOVE)
                    frame.place(x=650,y=80,width=600,height=635)
                    scroll_y=Scrollbar(frame,orient=VERTICAL)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    tv=ttk.Treeview(frame,column=("bid","sid","returnbook","returndate"),yscrollcommand=scroll_y)
                    tv.heading("bid",text="BID")
                    tv.heading("sid",text="SID")
                    tv.heading("returnbook",text="returnbook")
                    tv.heading("returndate",text="returndate")
                    tv["show"]="headings"
                    tv.column("bid",width=20)
                    tv.column("sid",width=80)
                    tv.column("returnbook",width=50)
                    tv.column("returndate",width=50)
                    tv.pack(fill=BOTH,expand=1)

                #Label
                welcome=Label(mh,text="Welcome",font=("TimesNewRomans",30,"bold"),bg="blue",fg="Black",relief=GROOVE)
                welcome.pack(side=TOP,fill=X)

                #button creation
                new_student=Button(mh,text="New student",command=nstudent,font=("TimesNewRomans",15,"bold"),bg="black",fg="white")
                new_student.place(x=100,y=100)

                new_book=Button(mh,text="New book",command=nbook,font=("TimesNewRomans",15,"bold"),bg="black",fg="white")
                new_book.place(x=600,y=100)

                issue=Button(mh,text="issue_book",command=issuebook,font=("TimesNewRomans",15,"bold"),bg="black",fg="white")
                issue.place(x=150,y=230)

                return_book=Button(mh,text="return_book",command=returnbook,font=("TimesNewRomans",15,"bold"),bg="black",fg="white")
                return_book.place(x=500,y=230)

                logout=Button(mh,text="logout",command=combb,font=("TimesNewRomans",15,"bold"),bg="black",fg="white")
                logout.place(x=350,y=360)

            else:
                messagebox.showerror("","Invalid username or password")
        def exit():
            exit=messagebox.askyesno("","Do you want to exit")
            if exit>0:
                f1.destroy()
                return
        def reset():
            user1.delete(0,END)
            pas1.delete(0,END)
          
        #label creation
        username=Label(f1,text="Username",font=("TimesNewRomans",20),bg="black",fg="white",bd=5)
        username.place(x=300,y=200)
        password=Label(f1,text="Password",font=("TimesNewRomans",20),bg="black",fg="white",bd=5)
        password.place(x=300,y=300)
        #entry creation
        user1=Entry(f1,bd=10,width=20,textvariable=user,font=("TimesNewRomans",20),bg="white",fg="black")
        user1.place(x=470,y=200)
        pas1=Entry(f1,bd=10,width=20,textvariable=pas,show="*",font=("TimesNewRomans",20),bg="white",fg="black")
        pas1.place(x=470,y=300)
        #button creation
        login1=Button(f1,text="login",command=password123,font=("TimesNewRomans",20),bg="red",fg="yellow",bd=5).place(x=200,y=500)
        reset=Button(f1,text="reset",command=reset,font=("TimesNewRomans",20),bg="red",fg="yellow",bd=5).place(x=500,y=500)
        exit=Button(f1,text="exit",command=exit,font=("TimesNewRomans",20),bg="red",fg="yellow",bd=5).place(x=800,y=500)

        f1.mainloop()

        
    else:
        student=Toplevel(home)
        student.config(bg="grey")
        student.geometry("800x800")
        student.title("Student page")
#signup function
        def signup():
            sup=Toplevel(student)
            sup.title("Login")
            sup.config(bg="magenta")
            sup.geometry("800x800")
            whitespace=" "
            sup.title(150*whitespace+"SIGN IN")
            signp=Label(sup,text="WELCOME TO SIGN-UP PAGE",font=("TimesNewRomans",20,"bold"),bg="blue",bd=10,fg="black")
            signp.pack(side=TOP,fill=X)
            def cpass():
                user=un1.get()
                passw=pw1.get()
                cpassw=cpw1.get()
                if passw==cpassw:
                
                    mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                    mysqlcon=mysqldb.cursor()
                    mysqlcon.execute("insert into login(username,password) values(%s,%s)",(un1.get(),cpw1.get()))
                    mysqldb.commit()
                    mysqldb.close()
                    messagebox.showinfo("","Password and username created successfully")
                else:
                    messagebox.showerror("","Incorrect password")

            un=Label(sup,text="username",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
            un.place(x=100,y=200)
            un1=Entry(sup,width=20,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
            un1.place(x=300,y=200)
            pw=Label(sup,text="password",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
            pw.place(x=100,y=270)
            pw1=Entry(sup,font=("TimesNewRomans",20,"bold"),show="*",bg="white",fg="black",bd=4)
            pw1.place(x=300,y=270)
            cpw=Label(sup,text="confirm",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
            cpw.place(x=100,y=350)
            cpw1=Entry(sup,font=("TimesNewRomans",20,"bold"),show="*",bg="white",fg="black",bd=4)
            cpw1.place(x=300,y=350)
            sinb=Button(sup,text="OK",command=cpass,font=("TimesNewRomans",20,"bold"),bd=10,fg="white",bg="black")
            sinb.place(x=150,y=420)
            close=Button(sup,text="close",command=combb,font=("TimesNewRomans",20,"bold"),bd=10,fg="white",bg="black")
            close.place(x=300,y=420)
#signin function
        def signin():
            sin=Toplevel(student)
            sin.title("Login")
            sin.config(bg="pink")
            sin.geometry("800x800")
            whitespace=" "
            sin.title(150*whitespace+"SIGN IN")
            def sinb():
                if un1.get()=="" or pw1.get()=="":
                    messagebox.showerror("","All fields are required")
                else:
                    mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                    mysqlcon=mysqldb.cursor()
                    mysqlcon.execute("Select * from login where username=%s and password=%s",(un1.get(),pw1.get()))
                    row=mysqlcon.fetchone()
                    if row==None:
                        messagebox.showerror("","Invalid username or password")
                    else:
                        messagebox.showinfo("","valid")
                        mysqldb.commit()
                        mysqldb.close()
                        sup1=Toplevel(sin)
                        sup1.config(bg="pale green")
                        sup1.title("Login")
                        sup1.geometry("800x800")
                        whitespace=" "
                        sup1.title(100*whitespace+"SIGN IN")
                        def bookdetails():
                            iss1=Toplevel(sup1)
                            iss1.title("Book details")
                            iss1.geometry("1500x800")
                            iss1.config(bg="deepskyblue2")
                            whitespace=" "
                            iss1.title(100*whitespace+"Book details")
                            def display():
                                mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                                mysqlcon=mysqldb.cursor()
                                res=mysqlcon.execute("select id,name,publisher,price,p_year from book where id=%s",(sd1.get(),))
                                result=mysqlcon.fetchall()
                                if result==None:
                                    messagebox.showerror("","Invalid book id")
                                else:
                                    
                                    print(result)
                                    for i,(id,name,publisher,price,p_year) in enumerate(result,start=1):  
                                    
                                        tv.insert("","end",values=(id,name,publisher,price,p_year))
                                    mysqldb.commit()
                                    mysqldb.close()
                            iss=Label(iss1,text="WELCOME TO BOOK DETAILS PAGE",font=("TimesNewRomans",20),bg="lightblue",bd=10,fg="black")
                            iss.pack(side=TOP,fill=X)
                            sd=Label(iss1,text="Book id",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                            sd.place(x=100,y=200)
                            sd1=Entry(iss1,width=20,textvariable=n,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                            sd1.place(x=300,y=200)
                            okb=Button(iss1,text="Ok",command=display,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                            okb.place(x=100,y=270)
                            close=Button(iss1,text="close",command=combb,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                            close.place(x=190,y=270)

                            frame=Frame(iss1,bg="skyblue",bd=5,relief=GROOVE)
                            frame.place(x=650,y=80,width=600,height=635)
                            scroll_y=Scrollbar(frame,orient=VERTICAL)
                            scroll_y.pack(side=RIGHT,fill=Y)
                            tv=ttk.Treeview(frame,column=("id","name","publisher","price","p_year"),yscrollcommand=scroll_y)
                            tv.heading("id",text="BID")
                            tv.heading("name",text="Name")
                            tv.heading("publisher",text="Publisher")
                            tv.heading("price",text="Price")
                            tv.heading("p_year",text="Published year")
                            tv["show"]="headings"
                            tv.column("id",width=20)
                            tv.column("name",width=80)
                            tv.column("publisher",width=50)
                            tv.column("price",width=50)
                            tv.column("p_year",width=50)
                            tv.pack(fill=BOTH,expand=1)
                        def issuedetails():
                            iss1=Toplevel(sup1)
                            iss1.title("ISSUE")
                            iss1.config(bg="deepskyblue2")
                            iss1.geometry("1500x800")
                            whitespace=" "
                            iss1.title(100*whitespace+"ISSUE")
                            
                            def display():
                                mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="library")
                                mysqlcon=mysqldb.cursor()
                                res=mysqlcon.execute("select id,sid,issuedate,duedate,returnbook,returndate from issue where sid=%s",(sd1.get(),))
                                result=mysqlcon.fetchall()
                                print(result)
                                for i,(id,sid,issuedate,duedate,returnbook,returndate) in enumerate(result,start=1):  
                                    
                                    tv.insert("","end",values=(id,sid,issuedate,duedate,returnbook,returndate))
                                mysqldb.commit()
                                mysqldb.close()
                            iss=Label(iss1,text="WELCOME TO ISSUE DETAILS PAGE",font=("TimesNewRomans",20),bg="lightblue",bd=10,fg="black")
                            iss.pack(side=TOP,fill=X)
                            sd=Label(iss1,text="Student id",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
                            sd.place(x=100,y=200)
                            sd1=Entry(iss1,width=20,textvariable=n,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
                            sd1.place(x=300,y=200)
                            okb=Button(iss1,text="Ok",command=display,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                            okb.place(x=100,y=270)
                            close=Button(iss1,text="close",command=combb,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                            close.place(x=190,y=270)

                            frame=Frame(iss1,bg="skyblue",bd=5,relief=GROOVE)
                            frame.place(x=650,y=80,width=600,height=635)
                            scroll_y=Scrollbar(frame,orient=VERTICAL)
                            scroll_y.pack(side=RIGHT,fill=Y)
                            tv=ttk.Treeview(frame,column=("id","sid","issuedate","duedate","returnbook","returndate"),yscrollcommand=scroll_y)
                            tv.heading("id",text="BID")
                            tv.heading("sid",text="SID")
                            tv.heading("issuedate",text="Issuedate")
                            tv.heading("duedate",text="Duedate")
                            tv.heading("returnbook",text="returnbook")
                            tv.heading("returndate",text="returndate")
                            tv["show"]="headings"
                            tv.column("id",width=20)
                            tv.column("sid",width=80)
                            tv.column("issuedate",width=50)
                            tv.column("duedate",width=50)
                            tv.column("returnbook",width=50)
                            tv.column("returndate",width=50)
                            tv.pack(fill=BOTH,expand=1)
                            
                                                       
                        issued=Button(sup1,text="issue-details",command=issuedetails,font=("TimesNewRomans",20,"bold"),bd=10,fg="dark green",bg="white")
                        issued.place(x=150,y=200)
                        bookd=Button(sup1,text="bookdetails",command=bookdetails,font=("TimesNewRomans",20,"bold"),bd=10,fg="dark green",bg="white")
                        bookd.place(x=400,y=200)
                        subb=Button(sup1,text="Ok",font=("TimesNewRomans",20,"bold"),bd=10,fg="dark green",bg="white")
                        subb.place(x=200,y=300)
                        close=Button(sup1,text="close",command=combb,font=("TimesNewRomans",20,"bold"),bd=10,fg="dark green",bg="white")
                        close.place(x=400,y=300)
            signn=Label(sin,text="WELCOME TO SIGN-IN PAGE",font=("TimesNewRomans",20,"bold"),bg="blue",bd=10,fg="black")
            signn.pack(side=TOP,fill=X)
            un=Label(sin,text="username",font=("TimesNewRomans",20,"bold"),bg="lightblue",fg="black",bd=5)
            un.place(x=100,y=200)
            un1=Entry(sin,width=20,font=("TimesNewRomans",20),bg="lightblue",fg="black",bd=4)
            un1.place(x=300,y=200)
            pw=Label(sin,text="password",font=("TimesNewRomans",20,"bold"),bg="lightblue",fg="black",bd=5)
            pw.place(x=100,y=270)
            pw1=Entry(sin,font=("TimesNewRomans",20,"bold"),show="*",bg="lightblue",fg="black",bd=4)
            pw1.place(x=300,y=270)
            sinb=Button(sin,text="sign-in",command=sinb,font=("TimesNewRomans",20,"bold"),bd=10,fg="white",bg="black")
            sinb.place(x=150,y=350)
            close=Button(sin,text="sign-out",command=combb,font=("TimesNewRomans",20,"bold"),bd=10,fg="white",bg="black")
            close.place(x=300,y=350)
        #label
        login=Label(student,text="STUDENT PAGE",font=("TimesNewRomans",20),bg="lightblue",bd=10,fg="black")
        login.pack(side=TOP,fill=X)

        signin=Button(student,text="Sign-in",command=signin,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
        signin.place(x=150,y=200)

        signout=Button(student,text="Sign-up",command=signup,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
        signout.place(x=450,y=200)

        close=Button(student,text="Close",command=combb,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
        close.place(x=300,y=350)
        

l1=Label(mainframe,text="Select the user type",font=("TimesNewRomans",20),bg="yellow",bd=10,fg="white")
l1.place(x=250,y=300)

###creating combobox
n=StringVar()
usertype=ttk.Combobox(mainframe,textvariable=n,font=("TimesNewRomans",15))
usertype["values"]=["User","admin"]
usertype.place(x=250,y=380)

###creating button
b1=Button(mainframe,text="login",command=combb,font=("TimesNewRomans",20),bg="orange",fg="black")
b1.place(x=250,y=460)
b2=Button(mainframe,text="exit",command=exit,font=("TimesNewRomans",20),bg="orange",fg="black")
b2.place(x=400,y=460)



home.mainloop()
