#imports
from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk

#Main Screen
master = Tk()
master.title('Banking App'.center(420))
master.geometry("1000x1000+0+0")
master.configure(background = "black")

    
#Functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password == "":
        return messagebox.showerror("Error","All Fields Required")


    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account has been created")

def register():
    #Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.geometry("600x500+0+0")
    

    #Labels
    Label(register_screen, text="Enter Your details to Register", font=('times new roman',35)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name",fg='red', font=('times new roman',25)).grid(row=1,sticky=W)
    Label(register_screen, text="Age",fg='red', font=('times new roman',25)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", fg='red',font=('times new roman',25)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", fg='red',font=('times new roman',25)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=('times new roman',25))
    notif.grid(row=6,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_name,bd=5,fg='blue',font=('times new roman',20,"bold")).grid(row=1,column=0,padx=20,pady=10)
    Entry(register_screen,textvariable=temp_age,bd=5,fg='blue',font=('times new roman',20,"bold")).grid(row=2,column=0,padx=20,pady=10)
    #Entry(register_screen,textvariable=temp_gender,bd=5,font=('times new roman',20,"bold")).grid(row=3,column=0,padx=20,pady=10)
    gender=ttk.Combobox(register_screen,textvariable=temp_gender,font=('times new roman',20,"bold"),width=20,state="readonly")
    gender['values']=("Male","Female","Others")
    gender.grid(row=3,column=0,padx=20,pady=10,)
    Entry(register_screen,textvariable=temp_password,bd=5,show="*",fg='blue',font=('times new roman',20,"bold")).grid(row=4,column=0,padx=20,pady=10)

    #Buttons
    Button(register_screen, text="Register", command = finish_reg,fg='blue', font=('times new roman',25)).grid(row=5,sticky=N,pady=10)

def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
 

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password  = file_data[1]
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                account_dashboard.geometry("500x700+0+0")
                account_dashboard.configure(background = "black")
                #Labels
                Label(account_dashboard, text="Account Dashboard", fg="#ff00bf",font=('times new roman',40)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+name,fg="#ff00bf", font=('times new roman',40)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Personal Details",fg="blue",font=('times new roman',30),width=20,command=personal_details).grid(row=2,sticky=N,padx=10,pady=20)
                Button(account_dashboard, text="Deposit",fg="blue",font=('times new roman',30),width=20,command=deposit).grid(row=3,sticky=N,padx=10,pady=20)
                Button(account_dashboard, text="Withdraw",fg="blue",font=('times new roman',30),width=20,command=withdraw).grid(row=4,sticky=N,padx=10,pady=20)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red", text="Password incorrect!!")
                return
    login_notif.config(fg="red", text="No account found !!")

def deposit():
    #Vars
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file   = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    deposit_screen.geometry("500x500+0+0")
    #Label
    Label(deposit_screen, text="Deposit",fg="#ff00bf", font=('times new roman',40)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen,fg="red", text="Current Balance : $"+details_balance, font=('times new roman',30))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen, text="Amount : ",fg="blue", font=('times new roman',30)).grid(row=2,sticky=W)
    deposit_notif = Label(deposit_screen,fg="blue",font=('times new roman',10))
    deposit_notif.grid(row=4, sticky=N,pady=5)
    #Entry

    Entry(deposit_screen, textvariable=amount,bd=5,fg="blue",font=('times new roman',20,'bold')).grid(row=2,sticky=E,padx=20,pady=10)
    #Button
    Button(deposit_screen,text="Finish",fg="blue",font=('times new roman',30),command=finish_deposit).grid(row=5,sticky=N,pady=5)

def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text='Amount is required!',fg="red")
        return
    if float(amount.get()) <=0:
        deposit_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : $"+str(updated_balance),fg="green")
    deposit_notif.config(text='Balance Updated', fg='green')
 
def withdraw():
     #Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file   = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')
    withdraw_screen.geometry("500x500+0+0")
    #Label
    Label(withdraw_screen, text="Withdraw", fg="#ff00bf",font=('times new roman',40)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_screen,fg="red", text="Current Balance : $"+details_balance, font=('times new roman',30))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen, text="Amount : ",fg="blue", font=('times new roman',30)).grid(row=2,sticky=W)
    withdraw_notif = Label(withdraw_screen,font=('times new roman',10))
    withdraw_notif.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(withdraw_screen,fg="blue",bd=5,font=('times new roman',20,'bold'), textvariable=withdraw_amount).grid(row=2,padx=20,pady=10,sticky=E)
    #Button
    Button(withdraw_screen,fg="blue",bd=5,font=('times new roman',30),text="Finish",command=finish_withdraw).grid(row=5,sticky=N,pady=5)

def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text='Amount is required!',fg="red")
        return
    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]

    if float(withdraw_amount.get()) >float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!', fg='red')
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : $"+str(updated_balance),fg="green")
    withdraw_notif.config(text='Balance Updated', fg='green')
    

def personal_details():
    #Vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]
    #Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    personal_details_screen.geometry("400x500+0+0")
    #Labels
    Label(personal_details_screen, text="Personal Details",fg="green", font=('times new roman',40)).grid(row=0,sticky=N,pady=10,padx=20)
    Label(personal_details_screen, text="Name : "+details_name,fg="red", font=('times new roman',20)).grid(row=1,sticky=W,pady=10,padx=20)
    Label(personal_details_screen, text="Age : "+details_age,fg="red", font=('times new roman',20)).grid(row=2,sticky=W,pady=10,padx=20)
    Label(personal_details_screen, text="Gender : "+details_gender,fg="red", font=('times new roman',20)).grid(row=3,sticky=W,pady=10,padx=20)
    Label(personal_details_screen, text="Balance :$"+details_balance, fg="red",font=('times new roman',20)).grid(row=4,sticky=W,pady=10,padx=20)
def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    login_screen.geometry("650x500+0+0")
    #Labels
    Label(login_screen, text=" Enter your details below to Login ", font=('times new roman',35)).grid(row=0,sticky=W)
    Label(login_screen, text="Username",fg='red', font=('times new roman',25)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", fg='red',font=('times new roman',25)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=('times new roman',12))
    login_notif.grid(row=4,sticky=W)
    #Entry
    Entry(login_screen, textvariable=temp_login_name,bd=5,fg='blue',font=('times new roman',20,'bold')).grid(row=1,padx=20,pady=10,sticky=N)
    Entry(login_screen, textvariable=temp_login_password,show="*",bd=5,fg='blue',font=('times new roman',20,'bold')).grid(row=2,padx=20,pady=10,sticky=N)
    #Button
    Button(login_screen, text="Login", command=login_session,fg="blue",font=('times new roman',25)).grid(row=5,sticky=N,pady=20,padx=10)
    

#Image import
img = Image.open('1..jpg')
img = img.resize((1000,400))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text = "Online Banking ", font=('times new roman',40)).grid(row=0,sticky=N,pady=10)
Label(master, text = "The Most Secure Bank You've Probably Used", font=('times new roman',40)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#Buttons
Button(master, text="Register", font=('times new roman',30),width=25,command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('times new roman',30),width=25,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()

