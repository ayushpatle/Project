from tkinter import *

from tkinter import messagebox

import mysql.connector as mc

import tkinter.messagebox as tm

import tkinter as tk

from tkinter.ttk import Combobox

import requests

import json

from tkinter import *

import smtplib

from tkinter import messagebox



window=Tk()

send_email=StringVar()

send_pass=StringVar()

recv_email=StringVar()



msg_body=None





def msg_box():

    messagebox.showinfo("Email Info","Mail Sent")



def instruct():

    messagebox.showinfo("Instruction","switch 'allow less secure apps' to ON from\nhttps://myaccount.google.com/u/0/security?hl=en&pli=1#connectedapps\nbefore using the app!!")



def about():

    messagebox.showinfo("About","This app is for only educational purpose\nCreated by Ayush patle")



def mail():

    try:

        if send_email.get()=="" or send_pass.get()=="" or recv_email.get()=="":

            messagebox.showerror("Error","Please enter the complete details.")

         

        else:

            server=smtplib.SMTP('smtp.gmail.com',587)

            server.starttls()

            a=send_email.get()

            b=send_pass.get()

            c=msg_body.get('1.0',END)

            d=recv_email.get()

            server.login(a,b)

            server.sendmail(a,d,c)

            server.close()

            msg_box()

    except Exception as e:

        print(e)

        a=messagebox.askokcancel("Error","Read instructions")

     

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):

    pmno = mno.get()

    pmsg = msg.get()

    req_params = {

                'apikey':"Enter ur api key",

                'secret':"enter ur secretKey",

                'usetype':"stage",

                'phone': str(pmno),

                'message':str(pmsg),

                'senderid':"Ur sender ID"

                }

    return requests.post(reqUrl, req_params)

def sms():

    response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )

    messagebox.showinfo("SMS Info","SMS Sent")



"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""

# print response if you want

   # print ("respons")



def put(*args):



    pname=name.get()

    pdob=dob.get()

    ppost=post.get()

    pmno = mno.get()

    pemail =email.get()





    cn = mc.connect(host = "localhost", user = "root",passwd = "ur data base password",database = "bday")

    cur = cn.cursor()

    cur.execute("insert into bdayinfo(name,dob,post,mno,email)values('"+str(pname)+"','"+str(pdob)+"','"+str(ppost)+"','"+str(pmno)+"','"+str(pemail)+"')")

    cur.execute("commit")

    top = Tk()

    top.geometry("100x100")

    var = StringVar()

    msg = Message( top, text = "Successful Inserted")

    msg.pack()

    cn.close()



def show():

    pname=name.get()

    pmno = mno.get()



    cn = mc.connect(host = "localhost", user = "root",passwd = "ur data base password",database = "bday")

    cur = cn.cursor()



    cur.execute("select * from bdayinfo where name='"+str(pname)+"' or mno='"+str(pmno)+"'")



    records = cur.fetchall()



  #  print("Total number of rows in Laptop is: ", cur.rowcount)

   # print("\nPrinting each laptop record")

    countb = cur.rowcount



    if countb > 0:

        for row in records:

            name.set(row[0])

            dob.set(row[1])

            post.set(row[2])

            mno.set(row[3])

            email.set(row[4])

            recv_email.set(row[4])

            mnomy=str(mno.set(row[3]))

        '''def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey':"Enter Ur API key",
                'secret':"Enter ur secret key",
                'usetype':"stage",
                'phone': mno.set(row[3]),
                'message':"hii how are you Successful 333",
                'senderid':"Ur  Sender Id"
                }
            return requests.post(reqUrl, req_params)
     
        def sms():
            response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
            print ("respons")
        btn1= Button(window, text="Send Greeting",width=15,height=0,font=('Times New Roman Bold', 25),command=sms)
        btn1.place(x=220, y=620)
'''

    else:

        top = Tk()

        top.geometry("100x100")

        msg = Message( top, text = "Not found any recored !")

        msg.pack()

    top = Tk()

    top.geometry("100x100")

    var = StringVar()

   # msg = Message( top, print(row[0]))

   # msg.pack()

    cn.close()

def clear_text():

        nameEntry.delete(0, END)

        dobEntry.delete(0, END)

        cb.delete(0, END)

        mnoEntry.delete(0, END)

        emailEntry.delete(0, END)



name=StringVar()

dob=StringVar()

post=StringVar()

mno=StringVar()

email=StringVar()

msg=StringVar()



menuBar=Menu(window)

menuBar.add_command(label="Instructions",command=instruct)

menuBar.add_command(label="About",command=about)

window.config(menu=menuBar)



lbl=Label(window, text="Welcome to Birthday Greeting Application \n Dr. Babasaheb Ambedkar Technological University,Lonere", fg='#03a5fc', font=("Times New Roman", 28))

lbl.place(x=60, y=10)

#lbl2=Label(window, text="Computer Engineering", fg='#fc5203', font=("Times New Roman", 28))

#lbl2.place(x=340, y=140)



btn1= Button(window, text="SMS",width=7,height=0,font=('Times New Roman Bold', 25),command=sms)

btn1.place(x=220, y=620)



'''btn5 = Button(window, text="EMAIL",width=7,height=0,font=('Times New Roman Bold', 25),command=layout)
btn5.place(x=380, y=620)
'''



btn2 = Button(window, text="Add Details",width=15,height=0,font=('Times New Roman Bold', 25),command=put)

btn2.place(x=550, y=620)



btn3 = Button(window, text="Clear Details",width=15,height=0,font=('Times New Roman Bold', 25),command=clear_text)

btn3.place(x=220, y=700)



btn4 = Button(window, text="Show Details",width=15,height=0,font=('Times New Roman Bold', 25),command=show)

btn4.place(x=550, y=700)





btn4 = Button(window, text="Show Details",width=15,height=0,font=('Times New Roman Bold', 25),command=show)

btn4.place(x=550, y=700)



#lbl3=Label(window, text="Ayush Suresh Patle (10303320191124510002)", fg='#03fc67', font=("Times New Roman", 28))

#lbl3.place(x=110, y=700)



namel =Label(window, text='FullName : ', width=15, height=0, font=('Times New Roman Bold', 20))

namel.place(x=100, y=120)

nameEntry =Entry(window, width=40,font=('Times New Roman Bold', 20),textvariable=name)

nameEntry.place(x=350, y=120)



dobl=Label(window, text='DOB : ', width=15, height=0, font=('Times New Roman Bold', 20))

dobl.place(x=100, y=160)



'''data = ("1", "2", "3", "4")
data2 = ("Jan", "Feb", "May", "Apr")
data3 = ("1997", "1998", "1999", "2000")
cb = Combobox(self.frame, values=data,textvariable=dob)
cb.place(x=60, y=150)
cb.pack()
cb1 = Combobox(self.frame, values=data2)
cb1.place(x=60, y=150)
cb1.pack()
cb2 = Combobox(self.frame, values=data3)
cb2.place(x=60, y=150)
cb2.pack()'''

dobEntry =Entry(window, width=40,font=('Times New Roman Bold', 20),textvariable=dob)

dobEntry.place(x=350, y=160)



postl=Label(window, text='Post : ', width=15, height=0, font=('Times New Roman Bold', 20))

postl.place(x=100, y=200)

data4 = ("Student","Alumini","Faculty")

cb = Combobox(window, values=data4,font=('Times New Roman Bold', 20),textvariable=post)

cb.place(x=350, y=200)

     

'''postl=Label(window, text='Post : ', width=15, height=0, font=('Times New Roman Bold', 20))
postl.place(x=100, y=360)
postEntry =Entry(window, width=40,font=('Times New Roman Bold', 20),textvariable=post)
postEntry.place(x=350, y=360)
'''

mnol =Label(window, text='Mobile : ', width=15, height=0, font=('Times New Roman Bold', 20))

mnol.place(x=100, y=240)

mnoEntry =Entry(window, width=40,font=('Times New Roman Bold', 20),textvariable=mno)

mnoEntry.place(x=350, y=240)



emaill =Label(window, text='Email : ', width=15, height=0, font=('Times New Roman Bold', 20))

emaill.place(x=100, y=280)

emailEntry =Entry(window, width=40,font=('Times New Roman Bold', 20),textvariable=email)

emailEntry.place(x=350, y=280)







msgl =Label(window, text='MSG : ', width=15, height=0, font=('Times New Roman Bold', 20))

msgl.place(x=100, y=320)

msgEntry =Entry(window, width=40,font=('Times New Roman Bold', 20),textvariable=msg)

msgEntry.place(x=350, y=320)







sender_email=Label(window,text="Sender's Gmail ID: ", font=('Times New Roman Bold', 16))

sender_email.place(x=1000, y=50)

sender_entry=Entry(window,textvariable=send_email,width=27,font=('Times New Roman Bold', 16),bd=3)

sender_entry.place(x=1180, y=50)



sender_pass=Label(window,text="Sender Gmail Pass: ",font=('Times New Roman Bold', 16))

sender_pass.place(x=1000, y=90)



sender_passentry=Entry(window,show='*',textvariable=send_pass,width=27,font=('Times New Roman Bold', 16),bd=3)

sender_passentry.place(x=1180, y=90)



receiver_email=Label(window,text="Receiver's Email: ",font=('Times New Roman Bold', 16))

receiver_email.place(x=1000, y=130)



receiver_entry=Entry(window,textvariable=recv_email,width=27,font=('Times New Roman Bold', 16),bd=3)

receiver_entry.place(x=1180, y=130)



msg_label=Label(window,text='Message',font=('Times New Roman Bold', 16))

msg_label.place(x=1000, y=170)



msg_body=Text(window,height=5,width=27,font=('Times New Roman Bold', 16),bd=3)

msg_body.place(x=1180, y=170)



send=Button(window,text='Send',width=15,command=mail,font=('Times New Roman Bold', 16),bd=3)

send.place(x=1000, y=330)



'''cancel=Button(window,text='Cancel',width=15,command=destroy,font=('Times New Roman Bold', 16),bd=3)
cancel.place(x=1300, y=330)
'''



window.title('Computer Department')

window.geometry("1500x780+10+5")



#window.after(5000, window.destroy)

window.mainloop()
