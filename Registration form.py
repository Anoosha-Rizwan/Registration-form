import tkinter as tk


#importing tkinter
from atexit import register
from ctypes import alignment
from tkinter import *
data=Tk()


#Giving title
data.title("Registration Form")
#Giving background
data.config(bg="white")
#Giving size
data.geometry("600x700")




a=Label(data,text="Registration  form",fg="black",bg="white" ,font="arial 25 bold").grid(row=0, column = 1,pady=20)

#Giving name 
fullname = Label(data,text="   Full name",fg="black",bg="white",font="arial 10 bold")
#Giving email
email = Label(data,text="   Email",fg="black",bg="white",font="arial 10 bold")
#giving size of name
fullname.grid(row=1,column=0, pady=10, sticky='W')
#giving size of email
email.grid(row=2,column=0,ipady=20 ,sticky='W')


#giving box of name
nameentry = entry = Entry(data, textvariable= 2, width = 60)
emailentry = entry = Entry(data, textvariable= 3,width = 60)

nameentry.grid(row=1,column=1,pady=10,padx=10)
emailentry.grid(row=2,column=1,pady=10,padx=10)



#giving gender with  color or writting style
a=Label(data,text= "   Gender",fg="black",bg="white",font="arial 10 bold").grid(row=4 , column = 0 ,sticky='W')

#giving radio  button for male and female
male= Radiobutton( data, text = "Male",value = 1,bg="white")
female= Radiobutton( data, text = "Female",value = 2,bg="white")
#calling radiobutton
male.grid(row=4 , column = 1,sticky='W')
female.grid(row=4 , columnspan =2,ipady=10) 


#Country with styling
Country=Label(data,text="   Country",fg="black",bg="white",font="arial 10 bold").grid(row=8, column = 0,sticky='W',ipady=20)
variable = StringVar(data)

#making a box 
variable.set("Select the country")

#making list of country 
w = OptionMenu(data, variable, "Pakistan", "Canada", "Australia","America" ,"Korea","china" ,"	Afghanistan","Germany ", "Japan")
w.grid(row=8, column = 1,sticky='W',ipady=5,ipadx=20)


#giving programming with styling
ch1=Label(data,text= "   Programming",fg="black",bg="white",font="arial 10 bold").grid(row=9 , column = 0,ipady=20)

#javascipt checkbox
ch1= Checkbutton(data,text = "javascript",bg="white")
ch1.grid(row=9 , column = 1,sticky='W')


#html,css, checkbox
ch2= Checkbutton( data, text = "html,css",bg="white")
ch2.grid(row=9, columnspan=2)

#python  checkbox
ch3= Checkbutton( data, text = "python",bg="white")
ch3.grid(row=10, column =1 ,sticky='W')

#c++ checkbox
ch4= Checkbutton( data, text = "c++",bg="white")
ch4.grid(row=10, columnspan=2)


#giving
MyButton1 = Button(data, text="Submit", width=10,fg="white",bg="red")
MyButton1.grid(row=12, column=0,ipady=2)




data.mainloop()

