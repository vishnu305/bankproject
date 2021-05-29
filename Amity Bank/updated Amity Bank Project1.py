import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
import sqlite3
import os
import datetime as dt
import time



def ok():
    name=fn.get()
    address=ad.get()
    phone=pn.get()
    govt=gid.get()
    acc=var.get()
    email=gd.get()
    password=pin.get()
    amount=am.get()
    accountno=ac.get()
    branch1=branch.get()
    ifsc1=ifsc.get()
    nom=nomination.get()
    ins=insurance.get()
    mode3=mode.get()
    dob1=dob.get()
    sex1=sex.get()
    confirm1=confirm.get()
    path2=path.get()
    file1=file
    if mode3=="Joint":
        name=fn.get()+" & "+name2.get()
    all_accounts=os.listdir()
    for acc_check in all_accounts:
        if accountno==acc_check:
            messagebox.showinfo("Amity Bank","Account Already Created")
            break
        else:
            new_file=open(accountno,"w")
            new_file.write(name+'\n')
            new_file.write(address+'\n')
            new_file.write(phone+'\n')
            new_file.write(govt+'\n')
            new_file.write(acc+'\n')
            new_file.write(email+'\n')
            new_file.write(password+'\n')
            new_file.write(amount+'\n')
            new_file.write(accountno+'\n')
            new_file.write(branch1+'\n')
            new_file.write(ifsc1+'\n')
            new_file.write(nom+'\n')
            new_file.write(ins+'\n')
            new_file.write(mode3+'\n')
            new_file.write(dob1+'\n')
            new_file.write(sex1+'\n')
            new_file.write(confirm1+'\n')
            if confirm1=="Yes":
                if file1=="":
                    new_file.write(path2+'\n')
                else:
                    new_file.write(file1+'\n')
            new_file.write('0')
            new_file.close()
            messagebox.showinfo("Amity Bank","Account Created Successfully")
            break

def create(window):
    global fn,ad,pn,gid,var,gd,pin,am,ac,branch,ifsc,nomination,insurance,mode,name2,dob,sex,confirm,path,file
    fn=StringVar()
    ad=StringVar()
    pn=StringVar()
    gid=StringVar()
    var=StringVar()
    gd=StringVar()
    pin=StringVar()
    am=StringVar()
    ac=StringVar()
    branch=StringVar()
    ifsc=StringVar()
    nomination=StringVar()
    insurance=StringVar()
    mode=StringVar()
    dob=StringVar()
    sex=StringVar()
    name2=StringVar()
    window1=Toplevel(window)
    window1.title("Creating an Bank Account")
    window1.geometry("1000x650")
    
    label_0=Label(window1,text="Amity Bank",bg="white",fg="blue",relief="solid").pack()
    label_1=Label(window1,text="Enter Your Name:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=50)
    entry_1=Entry(window1,textvar=fn).place(x=350,y=50)
    label_2=Label(window1,text="Enter Your Address:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=100)
    entry_2=Entry(window1,textvar=ad).place(x=350,y=100)
    label_3=Label(window1,text="Enter Your Phone Number:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=150)
    entry_3=Entry(window1,textvar=pn).place(x=350,y=150)
    label_4=Label(window1,text="Enter Your Pan Card Number:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=200)
    entry_4=Entry(window1,textvar=gid).place(x=350,y=200)
    label_5=Label(window1,text="Account Type:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=250)
    #entry_5=Entry(window1,textvar=var).place(x=350,y=250)
    list1=["savings account","current account"]
    droplist=OptionMenu(window1,var,*list1)
    var.set("Account Type")
    droplist.config(width=14)
    droplist.place(x=350,y=246)
    label_6=Label(window1,text="Enter email ID:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=300)
    entry_6=Entry(window1,textvar=gd).place(x=350,y=300)
    label_7=Label(window1,text="Enter New Password:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=350)
    entry_7=Entry(window1,textvar=pin,show="*").place(x=350,y=350)
    label_8=Label(window1,text="Enter Amount to be Deposited:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=400)
    entry_8=Entry(window1,textvar=am).place(x=350,y=400)
    label_9=Label(window1,text="Enter Account Number:",bg="brown",fg="white",relief="solid",width=30).place(x=40,y=450)
    entry_9=Entry(window1,textvar=ac).place(x=350,y=450)
    label_01=Label(window1,text="Bank Details",bg="white",fg="blue",relief="solid",width=20).place(x=670,y=150)
    label_10=Label(window1,text="Enter Branch Name:",bg="brown",fg="white",relief="solid",width=30).place(x=500,y=200)
    list2=["Noida","Lucknow","Hyderbad"]
    droplist1=OptionMenu(window1,branch,*list2)
    branch.set("Select Branch")
    droplist1.config(width=14)
    droplist1.place(x=800,y=194)
    label_11=Label(window1,text="Enter IFSC Code:",bg="brown",fg="white",relief="solid",width=30).place(x=500,y=250)
    entry_11=Entry(window1,textvar=ifsc).place(x=800,y=250)
    label_12=Label(window1,text="Nomination:",bg="brown",fg="white",relief="solid",width=30).place(x=500,y=300)
    list3=["Registered","Not Registered"]
    droplist2=OptionMenu(window1,nomination,*list3)
    nomination.set("Select")
    droplist2.config(width=14)
    droplist2.place(x=800,y=294)
    label_13=Label(window1,text="Personal Accident Insurance :",bg="brown",fg="white",relief="solid",width=30).place(x=500,y=350)
    r1=Radiobutton(window1,text="Required",variable=insurance,value="Required").place(x=790,y=350)
    r2=Radiobutton(window1,text="Not Required",variable=insurance,value="Not Required").place(x=880,y=350)
    label_14=Label(window1,text="Mode Of Operation:",bg="brown",fg="white",relief="solid",width=30).place(x=500,y=400)
    c1=Radiobutton(window1,text="Self",variable=mode,value="Self").place(x=790,y=400)
    c2=Radiobutton(window1,text="Joint",variable=mode,value="Joint").place(x=880,y=400)
    label_15=Label(window1,text="Enter Your Date Of Birth",bg="brown",fg="white",relief="solid",width=30).place(x=500,y=50)
    entry_15=Entry(window1,textvar=dob).place(x=800,y=50)
    label_16=Label(window1,text="Select Your Gender",bg="brown",fg="white",relief="solid",width=30).place(x=500,y=100)
    r3=Radiobutton(window1,text="Male",variable=sex,value="Male").place(x=790,y=100)
    r4=Radiobutton(window1,text="Female",variable=sex,value="Female").place(x=880,y=100)
    Label(window1,text="Enter the Second Name \n if you selected mode of operation as Joint:",bg="brown",fg="white",relief="solid",width=35,font=("calibri",10,"bold")).place(x=500,y=450)
    Entry(window1,textvar=name2).place(x=800,y=450)
    Label(window1,text="Do you Want to add Profile Picture:",bg="brown",fg="white",relief="solid",width=30).place(x=250,y=500)
    confirm=StringVar()
    y=Radiobutton(window1,text="Yes",variable=confirm,value="Yes").place(x=500,y=500)
    n=Radiobutton(window1,text="No",variable=confirm,value="No").place(x=590,y=500)
    Label(window1,text="If you Selected YES then enter the photo path :",bg="brown",fg="white",relief="solid",width=40).place(x=150,y=550)
    path=StringVar()
    Entry(window1,textvar=path).place(x=450,y=550)
    def exit2():
        window1.destroy()
    exit_button=Button(window1,text="To Exit",width=10,relief="solid",bg="grey",fg="white",command=exit2).place(x=550,y=600)
    file=""
    def openFile():
        global file
        file = askopenfilename(defaultextension=".png",filetypes=[("All Files", "*.*")])
        path.set(file)
    login_button=Button(window1,text="Sign in",width=10,relief="solid",bg="grey",fg="white",command=ok).place(x=350,y=600)
    Label(window1,text=" OR ").place(x=600,y=550)
    Button(window1,text="Click Here to Upload Photo",width=20,bg="yellow",fg="black",command=openFile).place(x=650,y=546)
    
    
def login_session(window2):
    global login_accno,tf_accno
    all_accounts=os.listdir()
    login_accno=ac1.get()
    login_password=pass1.get()
    login_ifsc=ac1.get()+"Amity"
    my_data=ac1.get()+"Lucknow"
    dep=StringVar()
    dep1=StringVar()
    password1=StringVar()
    password2=StringVar()
    attoa=StringVar()
    atbt=StringVar()
    reason=StringVar()
    for acc_check in all_accounts:
        if acc_check==login_accno:
            file=open(acc_check,"r")
            file_data=file.read()
            file_data=file_data.split("\n")
            password=file_data[6]
            name=file_data[0]
            def personal_details(window3):
                file=open(login_accno,"r")
                file_data=file.read()
                user_details=file_data.split("\n")
                user_name=user_details[0]
                user_address=user_details[1]
                user_phone=user_details[2]
                user_id=user_details[3]
                user_type=user_details[4]
                user_email=user_details[5]
                user_password=user_details[6]
                user_amount=user_details[7]
                user_accno=user_details[8]
                user_branch=user_details[9]
                user_ifsc=user_details[10]
                user_nom=user_details[11]
                user_insurance=user_details[12]
                user_mode=user_details[13]
                user_dob=user_details[14]
                user_sex=user_details[15]
                user_con=user_details[16]
                window4=Toplevel()
                window4.title("Personal Details")
                window4.geometry("600x750")
                Label11=Label(window4,text="Name = "+user_name,font=("calibri",12)).place(x=10,y=240)#.grid(row=1,sticky=W)
                Label12=Label(window4,text="Adress = "+user_address,font=("calibri",12)).place(x=10,y=270)#.grid(row=2,sticky=W)
                Label13=Label(window4,text="Phone Number = "+user_phone,font=("calibri",12)).place(x=10,y=300)#.grid(row=3,sticky=W)
                Label14=Label(window4,text="Pan Card Number = "+user_id,font=("calibri",12)).place(x=10,y=330)#.grid(row=4,sticky=W)
                Label15=Label(window4,text="Account type = "+user_type,font=("calibri",12)).place(x=10,y=360)#.grid(row=5,sticky=W)
                Label16=Label(window4,text="Email = "+user_email,font=("calibri",12)).place(x=10,y=390)#.grid(row=6,sticky=W)
                Label17=Label(window4,text="Password = "+user_password,font=("calibri",12)).place(x=10,y=420)#.grid(row=7,sticky=W)
                Label18=Label(window4,text="Account Balence = "+user_amount,font=("calibri",12)).place(x=10,y=450)#.grid(row=8,sticky=W)
                Label19=Label(window4,text="Account NO = "+user_accno,font=("calibri",12)).place(x=10,y=480)#.grid(row=9,sticky=W)
                Label20=Label(window4,text="Branch = "+user_branch,font=("calibri",12)).place(x=10,y=510)#.grid(row=10,sticky=W)
                Label21=Label(window4,text="IFSC CODE = "+user_ifsc,font=("calibri",12)).place(x=10,y=540)#.grid(row=11,sticky=W)
                Label22=Label(window4,text="Nomination = "+user_nom,font=("calibri",12)).place(x=10,y=570)#.grid(row=12,sticky=W)
                Label23=Label(window4,text="Insurance = "+user_insurance,font=("calibri",12)).place(x=10,y=600)#.grid(row=13,sticky=W)
                Label24=Label(window4,text="Mode Of Operation = "+user_mode,font=("calibri",12)).place(x=10,y=630)#.grid(row=14,sticky=W)
                Label25=Label(window4,text="Date Of Birth = "+user_dob,font=("calibri",12)).place(x=10,y=660)#.grid(row=15,sticky=W)
                Label26=Label(window4,text="Sex = "+user_sex,font=("calibri",12)).place(x=10,y=690)#.grid(row=16,sticky=W)
                if user_con=="Yes":
                    path11=user_details[17]
                    path1=str(path11)
                    image22=Image.open(path11)
                    photo22=ImageTk.PhotoImage(image22)
                    lab111=Label(window4,image=photo22).place(x=150,y=0,height=220,width=220)#.grid(row=0,column=6)
                    #Label["image"]=photo22
                    #lab111.place(x=300,y=40)
                    #lab111.grid(row=0,column=2)
                    
                def exit4():
                    window4.destroy()
                Button(window4,text="To exit",width=10,relief="solid",bg="brown",fg="white",command=exit4).place(x=500,y=690)#.grid(row=17,sticky=N,pady=10)
                window4.mainloop()
                
            def finish_deposit(window5,amtn):
                if amtn == '':
                    messagebox.showinfo("Amity Bank","Amount is required")
                elif float(amtn)<=0:
                    messagebox.showinfo("Amity Bank","Negitive Amount is not Accepeted")
                else:
                    file2=open(login_accno,'r+')
                    file2_data=file2.read()
                    details=file2_data.split('\n')
                    current_balence=details[7]
                    updated_balance=current_balence
                    updated_balance= float(updated_balance)+float(amtn)
                    file2_data = file2_data.replace(current_balence,str(updated_balance))
                    file2.seek(0)
                    file2.truncate(0)
                    file2.write(file2_data)
                    file2.close()
                    messagebox.showinfo("Amity Bank","Balence Updated")
                    messagebox.showinfo("Amity Bank","current Balence is Rs"+str(updated_balance))
                    file5=open(login_ifsc,"a")
                    file5.write( str(dt.datetime.now()))
                    file5.write("         Self Deposit                                              ")
                    file5.write(amtn)
                    file5.write("                 "+str(updated_balance)+'\n')
                    file5.close()
                    dbase1=sqlite3.connect(my_data)
                    dbase1.execute('''CREATE TABLE IF NOT EXISTS data_base(DATE TEXT NOT NULL, PARTICULARS TEXT NOT NULL, WITHDRAWLS TEXT NOT NULL, DEPOSITS TEXT NOT NULL, BALANCE TEXT NOT NULL)''')
                    dbase1.execute('''INSERT INTO data_base(DATE,PARTICULARS,WITHDRAWLS,DEPOSITS,BALANCE)VALUES(?,?,?,?,?)''',(str(dt.datetime.now()),"Self Deposit",'',str(amtn),str(updated_balance)))
                    dbase1.commit()
                    login_session(window5)
            def finish_withdrawl(window6,amnt):
                global user_amount
                if amnt == '':
                    messagebox.showinfo("Amity Bank","Amount is required")
                file3=open(login_accno,'r+')
                file3_data=file3.read()
                details1=file3_data.split('\n')
                current_balence1=details1[7]
                if float(amnt) >= float(current_balence1):
                    messagebox.showinfo("Amity Bank","Amount Must be less than Balance")
                else:
                    updated_balance1=current_balence1
                    updated_balance1= float(updated_balance1)-float(amnt)
                    file3_data = file3_data.replace(current_balence1,str(updated_balance1))
                    file3.seek(0)
                    file3.truncate(0)
                    file3.write(file3_data)
                    file3.close()
                    messagebox.showinfo("Amity Bank","Balence withdrawl successfully")
                    messagebox.showinfo("Amity Bank","current Balence is Rs"+str(updated_balance1))
                    file4=open(login_ifsc,"a")
                    file4.write( str(dt.datetime.now()))
                    file4.write("         Cash With Drawl         ")
                    file4.write(amnt)
                    file4.write("                                              "+str(updated_balance1)+'\n')
                    file4.close()
                    dbase2=sqlite3.connect(my_data)
                    dbase2.execute('''CREATE TABLE IF NOT EXISTS data_base(DATE TEXT NOT NULL, PARTICULARS TEXT NOT NULL, WITHDRAWLS TEXT NOT NULL, DEPOSITS TEXT NOT NULL, BALANCE TEXT NOT NULL)''')
                    dbase2.execute('''INSERT INTO data_base(DATE,PARTICULARS,WITHDRAWLS,DEPOSITS,BALANCE)VALUES(?,?,?,?,?)''',(str(dt.datetime.now()),"Cash Withdrawl",str(amnt),'',str(updated_balance1)))
                    dbase2.commit()
                    login_session(window6)
            def deposit(window3):
                window3.destroy()
                file1=open(login_accno,"r")
                file1_data=file1.read()
                user1_details=file1_data.split("\n")
                amount1=user1_details[7]
                window5=Tk()
                window5.title("Amount Deposit")
                window5.geometry("500x300")
                Label(window5,text="Current Balence = Rs"+amount1,font=("calibri",12)).place(x=40,y=50)
                Label(window5,text="Enter the Amount To be deposit",font=("calibri",12)).place(x=40,y=100)
                dep=StringVar()
                dep=Entry(window5)
                dep.place(x=350,y=100)
                Button(window5,text="Deposit",width=10,relief="solid",bg="brown",fg="white",command=lambda: finish_deposit(window5,dep.get())).place(x=40,y=150)
                def again1(window5):
                    
                    login_session(window5)
                Button(window5,text="Back",width=10,relief="solid",bg="brown",fg="white",command=lambda: again1(window5)).place(x=40,y=180)
                
                
            def withdrawl(window3):
                window3.destroy()
                file3=open(login_accno,"r")
                file3_data=file3.read()
                user3_details=file3_data.split('\n')
                amount3=user3_details[7]
                window6=Tk()
                window6.title("Amount WithDrawl")
                window6.geometry("500x300")
                Label(window6,text="Current Balence = Rs"+amount3,font=("calibri",12)).place(x=40,y=50)
                Label(window6,text="Enter the Amount to be WithDrawl",font=("calibri",12)).place(x=40,y=100)
                dep1=StringVar()
                dep1=Entry(window6)
                dep1.place(x=350,y=100)
                Button(window6,text="WithDrawl",width=10,relief="solid",bg="brown",fg="white",command=lambda: finish_withdrawl(window6,dep1.get())).place(x=40,y=150)
                def again2(window6):
                    login_session(window6)
                Button(window6,text="Back",width=10,relief="solid",bg="brown",fg="white",command=lambda: again2(window6)).place(x=40,y=180)
                
            def change_password(window7,psw,pswd):
                file2=open(login_accno,'r+')
                file2_data=file2.read()
                details=file2_data.split('\n')
                current_password=details[6]
                if current_password != psw :
                    messagebox.showinfo("Amity Bank","old password is not correct")
                
                updated_password= pswd
                file2_data = file2_data.replace(current_password,updated_password)
                file2.seek(0)
                file2.truncate(0)
                file2.write(file2_data)
                file2.close()
                messagebox.showinfo("Amity Bank","password changed successfully")
                login_session(window7)
            def change(window3):
                window3.destroy()
                window7=Tk()
                window7.title("Amount WithDrawl")
                window7.geometry("500x300")
                Label(window7,text="Enter Old Password = ",font=("calibri",12)).place(x=40,y=50)
                password1=StringVar()
                password1=Entry(window7,show="*")
                password1.place(x=350,y=50)
                Label(window7,text="Enter new password = ",font=("calibri",12)).place(x=40,y=100)
                password2=StringVar()
                password2=Entry(window7,show="*")
                password2.place(x=350,y=100)
                Button(window7,text="Change Password",width=15,relief="solid",bg="brown",fg="white",command=lambda: change_password(window7,password1.get(),password2.get())).place(x=40,y=150)
                def again3(window7):
                    login_session(window7)
                Button(window7,text="Back",width=10,relief="solid",bg="brown",fg="white",command=lambda: again3(window7)).place(x=40,y=180)
            def passbook():
                window10=Tk()
                window10.title("Pass Book Entries")
                #window10.geometry("600x800")
                #scrollbar=Scrollbar(window10).pack(fill=Y,side=RIGHT)
                
                Label(window10,text="|Date|                                           |Particulars|             |WithDrawls|        |Deposits|        |Balance|",font=("calibri",12),relief="solid",bg="white",fg="blue").grid(row=0,sticky=W)
                file10=open(login_ifsc,"r")
                file_data10=file10.read()
                user_entries=file_data10.split("\n")
                j=1
                for i in user_entries:
                    Label(window10,text=i,font=("calibri",12)).grid(row=j,sticky=W)
                    j=j+1
                window10.mainloop()
            def Tf(window11,attoa,atbt,reason):
                tf_accno=attoa
                all_accounts=os.listdir()
                k=0
                for acc_check in all_accounts:
                    if tf_accno!=acc_check:
                        k=k+1
                if atbt == '':
                    messagebox.showinfo("Amity Bank","Amount is required")
                if k==len(all_accounts):
                    messagebox.showinfo("Amity Bank","Account Not Found")
                else:
                    file11=open(login_accno,'r+')
                    file11_data=file11.read()
                    details11=file11_data.split('\n')
                    current_balence11=details11[7]
                    if float(atbt) >= float(current_balence11):
                        messagebox.showinfo("Amity Bank","Amount Must be less than Balance")
                    else:
                        updated_balance11=current_balence11
                        updated_balance11= float(updated_balance11)-float(atbt)
                        file11_data = file11_data.replace(current_balence11,str(updated_balance11))
                        file11.seek(0)
                        file11.truncate(0)
                        file11.write(file11_data)
                        file11.close()
                        messagebox.showinfo("Amity Bank","Amount Transfered successfully")
                        messagebox.showinfo("Amity Bank","current Balence is Rs"+str(updated_balance11))
                        file12=open(tf_accno,'r+')
                        file12_data=file12.read()
                        user12_entries=file12_data.split("\n")
                        current11_balance=user12_entries[7]
                        updated11_balance=current11_balance
                        updated11_balance=float(updated11_balance)+float(atbt)
                        file12_data=file12_data.replace(current11_balance,str(updated11_balance))
                        file12.seek(0)
                        file12.truncate(0)
                        file12.write(file12_data)
                        file12.close()
                        file13=open(login_ifsc,"a")
                        file13.write( str(dt.datetime.now()))
                        file13.write("         {}                ".format(reason))
                        file13.write(atbt)
                        file13.write("                                               "+str(updated_balance11)+'\n')
                        file13.close()
                        file14=open(tf_accno+"Amity","a")
                        file14.write( str(dt.datetime.now()))
                        file14.write("         Transfer From Another Account               ")
                        file14.write(atbt)
                        file14.write("                 "+str(updated11_balance)+'\n')
                        file14.close()
                        dbase3=sqlite3.connect(my_data)
                        dbase3.execute('''CREATE TABLE IF NOT EXISTS data_base(DATE TEXT NOT NULL, PARTICULARS TEXT NOT NULL, WITHDRAWLS TEXT NOT NULL, DEPOSITS TEXT NOT NULL, BALANCE TEXT NOT NULL)''')
                        dbase3.execute('''INSERT INTO data_base(DATE,PARTICULARS,WITHDRAWLS,DEPOSITS,BALANCE)VALUES(?,?,?,?,?)''',(str(dt.datetime.now()),str(reason),str(atbt),'',str(updated_balance11)))
                        dbase3.commit()
                        hi=tf_accno+"Lucknow"
                        dbase4=sqlite3.connect(hi)
                        dbase4.execute('''CREATE TABLE IF NOT EXISTS data_base(DATE TEXT NOT NULL, PARTICULARS TEXT NOT NULL, WITHDRAWLS TEXT NOT NULL, DEPOSITS TEXT NOT NULL, BALANCE TEXT NOT NULL)''')
                        dbase4.execute('''INSERT INTO data_base(DATE,PARTICULARS,WITHDRAWLS,DEPOSITS,BALANCE)VALUES(?,?,?,?,?)''',(str(dt.datetime.now()),"Transfered from Account No."+str(ac1.get()),'',str(atbt),str(updated11_balance)))
                        dbase4.commit()
                        login_session(window11)
            def Transfer(window3):
                window3.destroy()
                window11=Tk()
                window11.title("Amount Transfer to other Accounts")
                window11.geometry("650x330")
                Label(window11,text="Amity Bank",font=("calibri",12,"bold"),width=15,relief="solid",bg="white",fg="blue").place(x=200,y=50)
                Label(window11,text="Enter Account No to which the money have to be transfered:",font=("calibri",12),width=50,relief="solid",bg="brown",fg="white").place(x=40,y=100)
                attoa=StringVar()
                attoa=Entry(window11)
                attoa.place(x=500,y=100)
                Label(window11,text="Enter Amount to be Transfered:",font=("calibri",12),width=50,relief="solid",bg="brown",fg="white").place(x=40,y=150)
                atbt=StringVar()
                atbt=Entry(window11)
                atbt.place(x=500,y=150)
                Label(window11,text="Give Reason why are you Transfering:",font=("calibri",12),width=50,relief="solid",bg="brown",fg="white").place(x=40,y=200)
                reason=StringVar()
                list11=["Tuition Fees","Income Tax  ","Payment     ","Transfer    ","Donation    ","Others      "]
                #droplist11=OptionMenu(window11,reason,*list11)
                #reason.set("Select Reason")
                #droplist11.config(width=15)
                #droplist11.place(x=500,y=196)
                reason=ttk.Combobox(window11,value=list11,width=15)
                reason.set("Select Reason")
                reason.place(x=500,y=196)
                #reason=StringVar()
                #reason=Entry(window11)
                #reason.place(x=500,y=196)
                Button(window11,text="Click Here to Transfer",width=30,relief="solid",bg="blue",fg="white",command=lambda: Tf(window11,attoa.get(),atbt.get(),reason.get())).place(x=250,y=250)
                def again4(window11):
                    login_session(window11)
                Button(window11,text="Back",width=10,relief="solid",bg="brown",fg="white",command=lambda: again4(window11)).place(x=293,y=285)
                
                window11.mainloop()
            def passbook1():
                window20=Toplevel()
                window20.title("Pass Book")
                window20.geometry("1220x600")
                #table_frame=Frame(window20,bd=4,relief=RIDGE,bg="white").place(x=0,y=0,width=1200,height=590)
                #scroll_x=Scrollbar(table_frame,orient=HORIZONTAL).pack(fill=X,side=BOTTOM)
                #scroll_y=Scrollbar(table_frame,orient=VERTICAL).pack(fill=Y,side=RIGHT)
                
                student_table=ttk.Treeview(window20,columns=("DATE","PARTICULARS","WITHDRAWLS","DEPOSITS","BALANCE"))
                Scroll = Scrollbar(student_table)
                Scroll.pack(side=RIGHT,  fill=Y)
                Scroll.config(command=student_table.yview)
                student_table.config(yscrollcommand=Scroll.set)
                #scroll_y.config(command=student_table.yview)
                #student_table.config(yscroll=window20.set)
                student_table.heading("DATE",text="DATE")
                student_table.heading("PARTICULARS",text="PARTICULARS")
                student_table.heading("WITHDRAWLS",text="WITHDRAWLS")
                student_table.heading("DEPOSITS",text="DEPOSITS")
                student_table.heading("BALANCE",text="BALANCE")
                student_table['show']='headings'
                student_table.pack(fill=BOTH,expand=1)
                dbase=sqlite3.connect(my_data)
                cursor=dbase.cursor()
                data=cursor.execute(''' SELECT DATE,PARTICULARS,WITHDRAWLS,DEPOSITS,BALANCE FROM data_base''')
                x=data.fetchall()
                if len(x)!=0:
                    for row in x:
                        student_table.insert('',END,values=row)
                    dbase.commit()
                dbase.close()
                def clear(window20):

                    window20.destroy()
                    window21=Tk()
                    window21.title("Pass Book")
                    window21.geometry("1000x600")
                    #table_frame=Frame(window20,bd=4,relief=RIDGE,bg="white").place(x=0,y=0,width=1000,height=600)
                    #scroll_x=Scrollbar(window21,orient=HORIZONTAL).pack(fill=X,side=BOTTOM)
                    #scroll_y=Scrollbar(window21,orient=VERTICAL).pack(fill=Y,side=RIGHT)
                
                    student_table=ttk.Treeview(window21,columns=("DATE","PARTICULARS","WITHDRAWLS","DEPOSITS","BALANCE"))#,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                    Scroll = Scrollbar(student_table)
                    Scroll.pack(side=RIGHT,  fill=Y)
                    Scroll.config(command=student_table.yview)
                    student_table.config(yscrollcommand=Scroll.set) 
                #scroll_x.config(command=student_table.xview)
                #scroll_y.config(command=student_table.yview)
                    student_table.heading("DATE",text="DATE")
                    student_table.heading("PARTICULARS",text="PARTICULARS")
                    student_table.heading("WITHDRAWLS",text="WITHDRAWLS")
                    student_table.heading("DEPOSITS",text="DEPOSITS")
                    student_table.heading("BALANCE",text="BALANCE")
                    student_table['show']='headings'
                    student_table.pack(fill=BOTH,expand=1)
                    dbase=sqlite3.connect(my_data) 
                    dbase.execute('''DELETE from data_base''')
                    dbase.commit()
                    dbase.close()
                    dbase1=sqlite3.connect(my_data)
                    cursor1=dbase1.cursor()
                    data1=cursor1.execute(''' SELECT DATE,PARTICULARS,WITHDRAWLS,DEPOSITS,BALANCE FROM data_base''')
                    x1=data1.fetchall()
                    if len(x1)!=0:
                        for row in x1:
                            student_table.insert('',END,values=row)
                    dbase1.commit()
                    dbase1.close()
                    menu=Menu(window21)
                    window21.config(menu=menu)
                    submenu=Menu(window21)
                    menu.add_cascade(label="Opitions",menu=submenu)
                    submenu.add_command(label="Clear Entries",command=clear)
                    
                
                menu=Menu(window20)
                window20.config(menu=menu)
                submenu=Menu(window20)
                menu.add_cascade(label="Opitions",menu=submenu)
                submenu.add_command(label="Clear Entries",command=lambda:  clear(window20))
                window20.mainloop()
            if login_password==password:
                window2.destroy()
                window3=Tk()
                window3.title("Amity Bank")
                window3.geometry("1500x1000")
                window3.config(bg="orange")
                Label(window3,text="Amity Bank",font=("arial",120,"bold"),bg="black",fg="white",width=100).pack()
                Label(window3,text="Welcome  "+name,font=("times new roman",30,"bold"),bg="white",fg="blue").pack()
                Label(window3,text="TIME:",font=("arial",18,"bold"),bg="orange",fg="blue").place(x=10,y=150)
                clock = Label(window3, font=('times', 20, 'bold'), bg='orange',fg='blue')
                clock.place(x=110,y=150)
                def tick():
                    time1 = ''
                    # get the current local time from the PC
                    time2 = time.strftime('%H:%M:%S')
                    # if time string has changed, update it
                    if time2 != time1:
                        time1 = time2
                    clock.config(text=time2)
                    # calls itself every 200 milliseconds
                    # to update the time display as needed
                    # could use >200 ms, but display gets jerky
                    clock.after(200, tick)
                tick()
                Button(window3,text="Personal Details",font=("arial",15,"bold"),bd=6,bg="brown",fg="white",command=lambda: personal_details(window3)).place(x=50,y=620)
                depim=Image.open('deposit.jpg')
                depimg=ImageTk.PhotoImage(depim)
                d1=Button(window3,image=depimg,command=lambda: deposit(window3))
                d1.place(x=30,y=300)
                d1.image=depimg
                withim=Image.open('withdrawl.jpg')
                withimg=ImageTk.PhotoImage(withim)
                w1=Button(window3,image=withimg,command=lambda: withdrawl(window3))
                w1.place(x=310,y=300)
                w1.image=withimg
                Button(window3,text="Change Password",font=("arial",15,"bold"),bd=6,bg="brown",fg="white",command=lambda: change(window3)).place(x=550,y=620)
                Button(window3,text="Bank Pass Book Entries",font=("arial",15,"bold"),bd=6,bg="brown",fg="white",command=passbook).place(x=1070,y=620)
                traim=Image.open('transfer2.jpg')
                traimg=ImageTk.PhotoImage(traim)
                t1=Button(window3,image=traimg,command=lambda: Transfer(window3))
                t1.place(x=850,y=300)
                t1.image=traimg
                passim=Image.open('passbook.jpg')
                passimg=ImageTk.PhotoImage(passim)
                p1=Button(window3,image=passimg,command=passbook1)
                p1.place(x=570,y=300)
                p1.image=passimg
                i=Image.open('logout.jpg')
                i1=ImageTk.PhotoImage(i)
                def exit5():
                    messagebox.showinfo("Amity Bank","You are Successfully Logged out")
                    window3.destroy()
                    main_window()
                but=Button(window3,image=i1,command=exit5)
                but.image=i1
                but.place(x=1100,y=300)
            else:
                messagebox.showinfo("Amity Bank","Password Incorrect")
                break
def openn(window):
    global ac1,pass1
    window.destroy()
    window2=Tk()
    window2.title("Amity Bank , Your Account ")
    window2.geometry("500x300")
    ac1=StringVar()
    pass1=StringVar()
    label00=Label(window2,text="Amity Bank",bg="white",fg="blue",relief="solid").pack()
    label11=Label(window2,text="Enter your Account Number",bg="grey",fg="white",relief="solid",width=35).place(x=40,y=50)
    entry11=Entry(window2,textvar=ac1).place(x=350,y=50)
    label22=Label(window2,text="Enter your Password",bg="grey",fg="white",relief="solid",width=30).place(x=40,y=100)
    entry22=Entry(window2,textvar=pass1,show="*").place(x=350,y=100)
    def exit3():
        window2.destroy()
        main_window()
    exit1button=Button(window2,text="To Exit",width=10,relief="solid",bg="grey",fg="white",command=exit3).place(x=200,y=200)
    login_button=Button(window2,text="login",width=10,relief="solid",bg="grey",fg="white",command=lambda: login_session(window2)).place(x=200,y=150)



def main_window():
    window=Tk()
    window.geometry("580x450")
    window.config(bg="yellow")
    window.title("Amity Bank")
    image2=Image.open('pile1.gif')
    photo2=ImageTk.PhotoImage(image2)
    lab1=Label(image=photo2)
    lab1.pack()
    image=Image.open('banklogo.jpg')    
    photo=ImageTk.PhotoImage(image)
    lab=Button(window,image=photo)
    lab.image=photo
    lab.place(x=180,y=0)
    label1=Label(window,text="Amity Bank",bg="white",fg="blue",relief="solid").place(x=265,y=250)
    label2=Label(window,text="Create New Account in Amity Bank:",bg="grey",fg="white",relief="solid",width=30).place(x=40,y=300)
    button1=Button(window,text="Click Here to Create",width=20,bd=3,bg="brown",fg="white",command=lambda: create(window)).place(x=350,y=297)
    label3=Label(window,text="To check the existing Bank Account:",bg="grey",fg="white",relief="solid",width=30).place(x=40,y=350)
    button2=Button(window,text="Click Here to Open your Account",width=30,bd=3,bg="brown",fg="white",command=lambda: openn(window)).place(x=350,y=347)
    label4=Label(window,text="To exit:",bg="grey",width=30,fg="white",relief="solid").place(x=40,y=400)
    def exit1():
        window.destroy()
        exit()
    button3=Button(window,text="Click Here to Exit",width=20,bd=3,bg="brown",fg="white",command=exit1).place(x=350,y=397)
    #window.wm_iconbitmap(banklogo.jpg) 
    window.mainloop()
main_window()
