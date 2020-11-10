from tkinter import*

me = Tk()
me.geometry("354x460")
me.title("KALKULATOR")
melabel = Label(me,text="KALKULATOR",bg="white",font=("Times",30,"bold"))
melabel.pack(side=TOP)
me.config(background="Grey")

textin = StringVar()
operator=""


def clickbut(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)

def equalbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator = " "

def equalbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator = " "

def equalbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator = " "

def equalbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator = " "

def equalbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator = " "

def clrbut():
    textin.set(" ")

metext = Entry(me,font=("Arial",12,"bold"),textvar=textin,width=25,bd=5,bg="powder blue")
metext.pack()

but1 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(1),text="1",font=("Arial",15,"bold"))
but1.place(x=10,y=100)

but2 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(2),text="2",font=("Arial",15,"bold"))
but2.place(x=10,y=170)

but3 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(3),text="3",font=("Arial",15,"bold"))
but3.place(x=10,y=240)

but4 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(4),text="4",font=("Arial",15,"bold"))
but4.place(x=75,y=100)

but5 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(5),text="5",font=("Arial",15,"bold"))
but5.place(x=75,y=170)

but6 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(6),text="6",font=("Arial",15,"bold"))
but6.place(x=75,y=240)

but7 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(7),text="7",font=("Arial",15,"bold"))
but7.place(x=140,y=100)

but8 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(8),text="8",font=("Arial",15,"bold"))
but8.place(x=140,y=170)

but9 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(9),text="9",font=("Arial",15,"bold"))
but9.place(x=140,y=240)

but0 = Button(me,padx=14,pady=14,bd=4,bg="white",command=lambda:clickbut(0),text="0",font=("Arial",15,"bold"))
but0.place(x=10,y=310)

butdot = Button(me,padx=49,pady=14,bd=4,bg="white",command=lambda:clickbut("."),text=".",font=("Arial",15,"bold"))
butdot.place(x=75,y=310)

butpl = Button(me,padx=14,pady=14,bd=4,bg="white",text="+",command=lambda:clickbut("+"),font=("Arial",15,"bold"))
butpl.place(x=205,y=100)

butsub = Button(me,padx=16,pady=14,bd=4,bg="white",text="-",command=lambda:clickbut("-"),font=("Arial",15,"bold"))
butsub.place(x=205,y=170)

butml = Button(me,padx=16,pady=14,bd=4,bg="white",text="*",command=lambda:clickbut("*"),font=("Arial",15,"bold"))
butml.place(x=205,y=240)

butdiv = Button(me,padx=17,pady=14,bd=4,bg="white",text="/",command=lambda:clickbut("/"),font=("Arial",15,"bold"))
butdiv.place(x=205,y=310)

butclear = Button(me,padx=14,pady=119,bd=4,bg="white",text="CE",command=clrbut,font=("Arial",15,"bold"))
butclear.place(x=270,y=100)

butequal = Button(me,padx=151,pady=14,bd=4,bg="white",command=equalbut,text="=",font=("Arial",15,"bold"))
butequal.place(x=10,y=380)

me.mainloop()


