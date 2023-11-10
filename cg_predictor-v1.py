# The following code calculates your cg



from tkinter import *

def calc(marks):
    global credits
    sum = 0
    n = 0 
    for i in marks:
        sum = sum +(i*credits[n])
        n+=1
    cg = sum/18
    return cg 

def photoimage():
    global py_icon
    global world_icon
    #py_icon = PhotoImage(file=r"C:\Users\arnav\OneDrive - IIT Delhi\Codes\Python\Python GUI\python logo.png")
    #world_icon = PhotoImage(file=r"C:\Users\arnav\OneDrive - IIT Delhi\Codes\Python\Python GUI\world.png")

def win_ini(x,y):
    global window
    global bgcolor
    window = Tk()# instantiate an instance of a window
    photoimage()# creating images
    #--------------------Appreance of windows-----------------------
    window.geometry(str(x)+"x"+str(y))# define the geometry of our window
    window.title("CG calcultor & predictor")#windows title
    #window.iconphoto(True,py_icon)
    window.config(background = bgcolor)# backgroud color

def label(X,Y,course):
    global window
    global txtcolor
    global bgcolor
    label = Label(window,
              text = course,
              font=("Arial", 20 ,"bold") ,
              fg = txtcolor ,
              bg = bgcolor,
              padx = 10,
              pady = 10,
                )
    #label.pack()
    label.place(x=X , y=Y)

def labelcreate():
    global credits
    n=10
    for i in courses:
        label(10,n,i)
        n+=70

def button(x,y):
    button = Button(window,
                text  = "Calculate",
                command = calc ,
                font=("Arial", 30 ,"bold"),
                fg = "black",
                bg = "#E6E6FA",
                activeforeground = "black",
                activebackground = "purple",
                state = ACTIVE,

                )
    button.place(x=x,y=y)

marks = []
credits = [4,4,4,2,2,2]
courses = ['mtl100','apl100','cml101','mcp100','mcp101','cmp101']
bgcolor = "black"
txtcolor = "white"

win_ini(1500,700)

labelcreate()

button(50,600)

window.mainloop()


""""
print("This program calculates your expected cg")
for i in range(0,6):
    a=input(courses[i]+" Score:")
    marks.append(int(a))

print(calc(marks))
"""