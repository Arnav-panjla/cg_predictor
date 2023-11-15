# The following code calculates your cg

#------------------------------------V1---------------------------

from tkinter import *

#def photoimage():
    #global py_icon
    #global world_icon
    #py_icon = PhotoImage(file=r"C:\Users\arnav\OneDrive - IIT Delhi\Codes\Python\Python GUI\python logo.png")
    #world_icon = PhotoImage(file=r"C:\Users\arnav\OneDrive - IIT Delhi\Codes\Python\Python GUI\world.png")

def win_ini(x,y):
    global window
    global bgcolor
    window = Tk()# instantiate an instance of a window
    #photoimage()# creating images
    #--------------------Appreance of windows-----------------------
    window.geometry(str(x)+"x"+str(y))# define the geometry of our window
    window.title("CG calcultor & predictor")#windows title
    #window.iconphoto(True,py_icon)
    window.config(background = bgcolor)# backgroud color

def label(X,Y,txt):
    global window
    global txtcolor
    global bgcolor
    label = Label(window,
              text = txt,
              font=("Arial", 20 ,"bold") ,
              fg = txtcolor ,
              bg = bgcolor,
              padx = 10,
              pady = 10,
                )
    #label.pack()
    label.place(x=X , y=Y)

def button(x,y):
    button = Button(window,
                text  = "Calculate",
                command = Processing ,
                font=("Arial", 30 ,"bold"),
                fg = "black",
                bg = "#E6E6FA",
                activeforeground = "black",
                activebackground = "purple",
                state = ACTIVE
                )
    button.place(x=x,y=y)

def entry(x,y,i):
    global window
    global Marks
    Marks[i] = Entry(window,
                font=("Arial",30,"bold"),
                fg = txtcolor,
                bg = bgcolor
                )
    Marks[i].place(x=x,y=y)

def LabelAndEntryCreate():
    global credits
    n=10
    for i in courses:
        label(10,n,i)
        entry(200,n,i)
        n+=70

def VariableAssigner():
    global Marks
    for i in courses:
        Marks[i]=int(Marks[i].get())

def calc():
    global Marks
    global credits_dict
    global credits_list
    global credit_total
    global courses
    VariableAssigner()
    sum = 0 
    for i in courses:
        sum+=(Marks[i]*credits_dict[i])
    cg = (sum/credits_total)
    return cg  

def Processing():
    cg = round(calc()*1000)/1000 # rounds off to 3 decimal places
    txt = "Your expected cg is : "+str(cg)
    label(900,100,txt)

#variable declaration
Marks = {} #decalaring a dictionary
credits_list = [4,4,4,2,2,2]
credits_total = sum(credits_list)
courses = ['mtl100','apl100','cml101','mcp100','mcp101','cmp101']
bgcolor = "black"
txtcolor = "white"
credits_dict = dict(zip(courses,credits_list))#making a dictionary


# main code 
win_ini(1500,700)

LabelAndEntryCreate()

button(50,600)

window.mainloop()
