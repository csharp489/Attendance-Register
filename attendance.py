from tkinter import Tk, StringVar, ttk
from tkinter import*
import time;
import datetime

root=Tk()
root.title("Attendance Register")
root.geometry('1350x650+0+0')
root.configure(background='black')

#_ _ _ _ _ _ _ _ _ _ _ Frames _ _ _ _ _ _ __ _ __  _ _ __ __ ____ _ _
LeftMayFrame=Frame(root,width=1000,height=650,bd=8,relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame=Frame(root,width=350,height=630,bd=8,relief="raise")
RightMayFrame.pack(side=RIGHT)

LeftMayFrame1=Frame(LeftMayFrame,width=1000,height=350,bd=8,relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2=Frame(LeftMayFrame,width=1000,height=600,bd=8,relief="raise")
LeftMayFrame2.pack(side=TOP)

RightMayFrame1=Frame(RightMayFrame,width=350,height=215,bd=8,relief="raise")
RightMayFrame1.pack(side=TOP)
RightMayFrame2=Frame(RightMayFrame,width=350,height=415,bd=8,relief="raise")
RightMayFrame2.pack(side=TOP)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ __ _  __

cont1=Canvas(RightMayFrame2,width=350,height=425,bg="black",)
cont1.grid(row=0,column=0)
image5=PhotoImage(file="school01.png")
cont1.create_image(200,200,image=image5)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _  __

cont=Canvas(RightMayFrame1,width=350,height=215)
cont.grid(row=0,column=0)
image1=PhotoImage(file="img01.png")
image=cont.create_image(200,200,image=image1)
def pic1():
      image=cont.create_image(200,200,image=image1)

image2=PhotoImage(file="img02.png")

def pic2():
      image=cont.create_image(200,200,image=image2)

image3=PhotoImage(file="img03.png")
def pic3():
      image=cont.create_image(200,200,image=image3)

image4=PhotoImage(file="img04.png")
def pic4():
      image=cont.create_image(200,200,image=image4)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _  __



DateofOrder=StringVar()
value0=StringVar()
value1=StringVar()
value2=StringVar()
value3=StringVar()
value4=StringVar()
value5=StringVar()
value6=StringVar()
value7=StringVar()
value8=StringVar()
value9=StringVar()

def Mark_Register():
    if value0.get()=="/":
        value1.set("/")
        value2.set("/")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")
        value8.set("/")
        value9.set("/")
        
    elif (value0.get()=="O"):
        value1.set("O")
        value2.set("O")
        value3.set("O")
        value4.set("O")
        value5.set("O")
        value6.set("O")
        value7.set("O")
        value8.set("O")
        value9.set("O")
        
    elif (value0.get()=="S"):
        value1.set("S")
        value2.set("S")
        value3.set("S")
        value4.set("S")
        value5.set("S")
        value6.set("S")
        value7.set("S")
        value8.set("S")
        value9.set("S")
        
    elif (value0.get()=="A"):
        value1.set("A")
        value2.set("A")
        value3.set("A")
        value4.set("A")
        value5.set("A")
        value6.set("A")
        value7.set("A")
        value8.set("A")
        value9.set("A")
        
    elif (value0.get()=="L"):
        value1.set("L")
        value2.set("L")
        value3.set("L")
        value4.set("L")
        value5.set("L")
        value6.set("L")
        value7.set("L")
        value8.set("L")
        value9.set("L")
        
    elif (value0.get()==" "):
        value1.set(" ")
        value2.set(" ")
        value3.set(" ")
        value4.set(" ")
        value5.set(" ")
        value6.set(" ")
        value7.set(" ")
        value8.set(" ")
        value9.set(" ")
        

def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    
    
def qExit():
      qExit = messagebox.askyesno("Exit System","Do you want to quit?")
      if qExit > 0:
            root.destroy()
            return

#____ _ _ _ _ _ _ _  _ _ __ _ _ Components _ _ _ _ __ _ _ __ __ _ __ __ _ __ 
DateofOrder.set(time.strftime("%d/%m/%Y"))
#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame1 _ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame1,font=('arial',10,'bold'),text="No.",bd=16)
lblNo.grid(row=0,column=0,sticky=W)
lblStudentNo=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Student No.",bd=16)
lblStudentNo.grid(row=0,column=1,sticky=W)
lblStudentName=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Student Name",bd=16)
lblStudentName.grid(row=0,column=2,sticky=W)
lblCourseCode=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Course Code",bd=16)
lblCourseCode.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame1,textvariable=value0,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=0,column=4)
btnArrow=Button(LeftMayFrame1, text='Fill', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=Mark_Register).grid(row=0,column=5)
btnReset=Button(LeftMayFrame1,text='Reset',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=Reset).grid(row=0,column=6)
btnExit=Button(LeftMayFrame1,text='Exit',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=qExit).grid(row=0,column=7)
lblDateofOrder=Label(LeftMayFrame1,font=('arial',10,'bold'),textvariable=DateofOrder,padx=2,
                     pady=2, bd=2,fg="black",bg='white',relief='sunken')
lblDateofOrder.grid(row=0,column=8,sticky=W)
#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row1 _ _ _ __ _ _ _ _ __ __ __ __  __

lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1",bd=16)
lblNo.grid(row=0,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1232",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=0,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="karishma gupta",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=0,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value1,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=0,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic1).grid(row=0,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic2).grid(row=0,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic3).grid(row=0,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=0,column=8)
#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row2_ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="2",bd=16)
lblNo.grid(row=1,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1432",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=1,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Sheetal",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=1,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=1,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value2,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=1,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic4).grid(row=1,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic1).grid(row=1,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic2).grid(row=1,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=1,column=8)
#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row3_ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="3",bd=16)
lblNo.grid(row=2,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1532",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=2,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Mehak",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=2,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=2,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value3,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=2,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic2).grid(row=2,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic3).grid(row=2,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic1).grid(row=2,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=2,column=8)
#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row4_ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="4",bd=16)
lblNo.grid(row=3,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1632",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=3,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Poorva",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=3,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1003",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=3,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value4,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=3,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic1).grid(row=3,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic4).grid(row=3,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic3).grid(row=3,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=3,column=8)
#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row5_ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="5",bd=16)
lblNo.grid(row=4,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1732",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=4,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Sarika",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=4,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=4,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value5,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=4,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic1).grid(row=4,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic3).grid(row=4,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic4).grid(row=4,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=4,column=8)


#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row6_ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="6",bd=16)
lblNo.grid(row=5,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="2732",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=5,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Muskan",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=5,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=5,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value6,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=5,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic1).grid(row=5,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic4).grid(row=5,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic3).grid(row=5,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=5,column=8)

#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row7_ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="7",bd=16)
lblNo.grid(row=6,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="3732",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=6,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Nidhi",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=6,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=6,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value7,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=6,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic3).grid(row=6,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic2).grid(row=6,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic1).grid(row=6,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=6,column=8)

#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row8_ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="8",bd=16)
lblNo.grid(row=7,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="3712",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=7,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Ritika",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=7,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=7,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value8,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=7,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic4).grid(row=7,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic3).grid(row=7,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic2).grid(row=7,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic1).grid(row=7,column=8)

#__ _ _ _ _ _ _ _ _ _ _ _ _ _LeftMayFrame2 row9_ _ _ __ _ _ _ _ __ __ __ __  __
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="9",bd=16)
lblNo.grid(row=8,column=0,sticky=W)
lblStudent_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="3792",padx=2,
                      pady=2,bd=2,fg="black",width=18)
lblStudent_No_1.grid(row=8,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Payal",padx=2,
                      pady=2,bd=2,fg="black",width=12)
lblStudent_Name.grid(row=8,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,
                     pady=2,bd=2,fg="black",width=12)
lblCourse_Code.grid(row=8,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value9,state='readonly')
box['values']=('','/','L','O','A','S')
box.current(0)
box.grid(row=8,column=4)

btnSpace=Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                font=('arial',10,'bold'), width=12,height=1,command=pic4).grid(row=8,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic2).grid(row=8,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",
                font=('arial',10,'bold'), width=11,height=1,command=pic3).grid(row=8,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2, bd=2,fg="black",
                font=('arial',10,'bold'),width=11,height=1,command=pic1).grid(row=8,column=8)




root.mainloop()
