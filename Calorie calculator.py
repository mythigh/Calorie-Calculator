from tkinter import *
import tkinter.messagebox
screen = Tk()
screen.title("Calorie Calculator")

def help_win():
    global lb2
    global bt2
    top = Toplevel()
    top.title("Instructions")
    lb2 = Label(top,text="The calorie calculator is used to calculate the number \n"
                         "of calories a person must consume each day. "
                         "\n\nUsers must input all details to calculate their daily calorie intake.\n\n"
                         "Your calorie intake will vary depending on a persons Activity level.", anchor = W).pack(side = TOP,pady = 5,padx = 5, fill="both")
    bt2 = Button(top,text="Close Window", command = top.destroy).pack(side= BOTTOM, pady=5)

mainmenu = Menu(screen)
screen.config(menu = mainmenu)
submen= Menu(mainmenu)
mainmenu.add_command(label = "Help", command = help_win)
toolbar = Frame(screen, bg ="grey").grid(row=0,column=0, sticky=W)


Maintain  = Button(toolbar,text = "Maintenance", command = lambda: type(100)).grid(row=0,column=0, sticky=W)
weightloss = Button(toolbar,text = "Weight Loss", command = lambda: type(81)).grid(row=0,column=1, sticky=W)
exweightloss = Button(toolbar,text = "Extreme Weight Loss", command = lambda: type(62)).grid(row=0,column=2, sticky=W)



tit =""
#title

globals()
label1= Label(screen, text = "Calorie Calculator")
label1.grid(row = 1,column = 0, columnspan =3, pady = 2)


#Gender option

gender = ["Male",
          "Female"]

sex = StringVar()
sex.set("Male")

# gender radio buttons
check_m = Radiobutton(screen,text="Male", variable=sex, value = "male").grid(row=2, column = 0, pady=3,sticky=W)
check_f = Radiobutton(screen,text="Female", variable=sex, value="female").grid(row=2, column=1, pady=3,sticky=W)


# Age Entry
age = Entry(screen, width = 5, borderwidth = 5)
label2= Label(screen, text = "Enter Your Age:")
label2.grid(row = 3,column = 0,sticky=W,columnspan =2)
age.grid(row = 3,column = 2,sticky=W,columnspan =2)

# Height Entry
height = Entry(screen, width = 5, borderwidth = 5)
label3= Label(screen, text = "Enter Your Height (cm):")
label3.grid(row = 4,column = 0,sticky=W,columnspan =2)
height.grid(row = 4,column = 2,sticky=W,columnspan =2)
# Weight Entry
weight = Entry(screen, width = 5, borderwidth = 5)
label4= Label(screen, text = "Enter Your Weight (kg):")
label4.grid(row = 5,column = 0,sticky=W,columnspan =2)
weight.grid(row = 5,column = 2,sticky=W,columnspan =2)

#Activity Drop down
label5 = Label(screen,text = "Exercise Level")




#list of options
options = [ "Little/no exercise",
            "Light: 1-3 times a week",
            "Moderate: 4-5 times a week",
            "Active: 6-7 times a week",
            "Intense daily excercise \nor physical job",
           ]

clicked = StringVar()
clicked.set("--Activity Level--")


drop = OptionMenu(screen,clicked, *options).grid(row = 7,column = 0, columnspan =3)

label5.grid(row = 6,column = 0, columnspan =2)
def type(percent):
    if percent == 100:
        tit = "Maintenance: "
        label1 = Label(screen, text=tit + "Calorie Calculator")
        label1.grid(row=1, column=0, columnspan=3, pady=2)
    elif percent == 81:
        tit = "Weight Loss: "
        label1 = Label(screen, text=tit + "Calorie Calculator")
        label1.grid(row=1, column=0, columnspan=3, pady=2)
    elif percent == 62:
        tit = "Extreme Weight Loss: "
        label1 = Label(screen, text=tit + "Calorie Calculator")
        label1.grid(row=1, column=0, columnspan=3, pady=2)

    def chose():
        try:
            if float(age.get())<=0 or float(age.get())>99:
                error = tkinter.messagebox.showwarning("", "Invalid Age!\n\n Must be 1-99.")
            if clicked.get() == "Little/no exercise":
                calculate(1.2)
            elif clicked.get() == "Light: 1-3 times a week":
                calculate(1.375)
            elif clicked.get() == "Moderate: 4-5 times a week":
                calculate(1.55)
            elif clicked.get() == "Active: 6-7 times a week":
                calculate(1.725)
            elif clicked.get() == "Intense daily excercise \nor physical job":
                calculate(1.9)
        except ValueError:
            error = tkinter.messagebox.showwarning("", "Invalid Input!\n\n Please enter numbers only.")


    # Mifflin-St Jeor Equation:
    # For men: BMR = 10W + 6.25H - 5A + 5
    # For women: BMR = 10W + 6.25H - 5A - 161
    def calculate(act):
        if sex.get() == "male":
            BMR = 5 + (10*float(weight.get()))+(6.25*float(height.get()))-(5*float(age.get()))
            men = BMR*act
            percentage = (percent / 100) * round(men)
            choice = Label(screen, text="Daily calories intake is: " + str(round(percentage))+ " cal")
        elif sex.get() == "female":
            BMR= 447.93 + (9.247 *float(weight.get()))+(3.098*float(height.get()))-(4.330*float(age.get()))
            wmen = BMR*act
            percentage = (percent / 100) * round(wmen)
            choice = Label(screen, text="Daily calories intake is: " + str(round(percentage)) + " cal")

        choice.grid(row=9,column=0, columnspan= 3)

    butt1 = Button(screen, text = "Calculate", command =chose)
    butt1.grid(row=8,column=0, columnspan= 3, pady= 3)

screen.mainloop()

