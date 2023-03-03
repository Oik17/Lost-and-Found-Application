import mysql.connector as sqltor
from tkinter import *
from tkinter import messagebox
from tkinter.font import *

db0 = sqltor.connect(host="localhost", user='root', passwd='pass', database='test')

cursor = db0.cursor()


root= Tk()
root.configure(bg='black')
#root.resizable(height=1000, width= 500)
root.geometry('600x255')
def login():

    top3=Toplevel()
    top3.configure(bg='black')
    #top3.resizable(height=1000, width= 500)
    top3.geometry('600x255')
    mainpage = Label(top3, text = '''Welcome to Lost and Found''', bg="black", fg="white")
    nameLabel= Label(top3, text= "Email ID ", bg="black", fg="white")
    nameLabel.place(x=150, y=40)
    phoneLabel= Label(top3, text= "Password", bg="black", fg="white")
    phoneLabel.place(x=150, y=70)

    mainpage.pack()
    nameinput = Entry(top3,bg="#212221", fg="#90b4fc")
    phoneinput = Entry(top3,bg="#212221", fg="#90b4fc")

    nameinput.place(x=260, y=40)
    phoneinput.place(x=260, y=70)


    def step1():
        name=nameinput.get()
        num=phoneinput.get()
        if name == "" or num == "" :
                messagebox.showinfo("Invalid Entry", "Please enter all fields.")
                print(type(num))

        else:
            top = Toplevel()
            top.configure(bg='black')
            top.geometry('600x100')
            intend = Label(top, text="Have you lost or found an item?",bg="black", fg="white")
            intend.pack()

            intend = Label(top, text="       ", bg="black", fg="white")
            intend.pack()

            def lost():
                top1 = Toplevel()
                top1.configure(bg='black')
                top1.geometry('300x300')
                intend = Label(top1, text="Please enter what type of item you have lost.", bg="black", fg="white")
                intend.pack()
                lostitem = Entry(top1, bg="#212221", fg="#90b4fc")
                lostitem.place(x=80, y=30)


                def lost1():
                    lostt=lostitem.get()
                    str1='select * from lost;'
                    cursor.execute(str1)
                    lst= list(cursor.fetchall())
                    count=0
                    count1=0
                    intend2 = Label(top1, text="We found the following possible matches: ", bg="black", fg="white")
                    intend2.place(x=40, y=100)
                    for i in lst:
                        if i[0].lower()==lostt.lower():
                            intend2 = Label(top1, text=i[1], bg="black", fg="white")
                            intend2.place(x=70,y=120+count1)
                            intend3 = Label(top1, text=i[0].capitalize(), bg="black", fg="white")
                            intend3.place(x=40, y=120 + count1)
                            count+=1
                        count1+=10
                    if count==0:
                        intend1 = Label(top1, text="No available items", bg="black", fg="white")
                        intend1.place(x=70,y=120)


                myButton1 = Button(top1, text="Go", command=lost1, bg="#90b4fc", fg="black")
                myButton1.place(x=130,y=60)
            def found():
                top2 = Toplevel()
                top2.configure(bg='black')
                top2.geometry('300x100')
                intend = Label(top2, text="Please enter a brief description of the item.", bg="black", fg="white")
                intend.pack()
                founditem = Entry(top2, bg="#212221", fg="#90b4fc")
                founditem.place(x=80, y=30)

                def found1():
                    find= founditem.get()
                    name=nameinput.get()
                    str="insert into lost values('{}','{}');".format(find,name)
                    cursor.execute(str)
                    db0.commit()
                    top2.destroy()

                myButton1 = Button(top2, text="Go", command=found1, bg="#90b4fc", fg="black")
                myButton1.place(x=130,y=60)
            myButton = Button(top, text="Lost", command=lost, bg="#90b4fc", fg="black")
            myButton.pack()

            myButton1 = Button(top, text="Found", command=found, bg="#90b4fc", fg="black")
            myButton1.pack()

    mainbutton = Button(top3, text="Login", command=step1, bg="#90b4fc", fg="black")
    mainbutton.place(x=260, y=120)

def signup():
    top4=Toplevel()
    top4.configure(bg='black')
    # top3.resizable(height=1000, width= 500)
    top4.geometry('600x255')
    mainpage = Label(top4, text='''Welcome to Lost and Found''', bg="black", fg="white")
    nameLabel = Label(top4, text="Name ", bg="black", fg="white")
    nameLabel.place(x=150, y=40)
    rno = Label(top4, text="Reg. Number", bg="black", fg="white")
    rno.place(x=150, y=70)
    phoneLabel = Label(top4, text="Phone Number", bg="black", fg="white")
    phoneLabel.place(x=150, y=100)
    email = Label(top4, text="Email ID", bg="black", fg="white")
    email.place(x=150, y=130)
    password = Label(top4, text="Password", bg="black", fg="white")
    password.place(x=150, y=160)

    mainpage.pack()

    nameinput = Entry(top4, bg="#212221", fg="#90b4fc")
    rnoinput = Entry(top4, bg="#212221", fg="#90b4fc")
    phoneinput = Entry(top4, bg="#212221", fg="#90b4fc")
    emailinput = Entry(top4, bg="#212221", fg="#90b4fc")
    passinput = Entry(top4, bg="#212221", fg="#90b4fc")

    nameinput.place(x=260, y=40)
    rnoinput.place(x=260, y=70)
    phoneinput.place(x=260, y=100)
    emailinput.place(x=260, y=130)
    passinput.place(x=260, y=160)

    def go():
        name = nameinput.get()
        phone = phoneinput.get()
        email = emailinput.get()
        rno = rnoinput.get()
        passw = passinput.get()

        str6= "insert into user values('{}','{}',{},'{}','{}');".format(name,rno,phone,email,passw)
        cursor.execute(str6)
        db0.commit()
        success = Label(top4, text="Successfully Updated", bg="black", fg="white")
        success.place(x=230, y=230)
    button4 = Button(top4, text="go", command=go, bg="#90b4fc", fg="black")
    button4.place(x=260, y=200)


mainbutton = Button(root, text="Login", command=login, bg="#90b4fc", fg="black")
mainbutton.place(x=260, y=120)


mainbutton1 = Button(root, text="SignUp", command=signup, bg="#90b4fc", fg="black")
mainbutton1.place(x=260, y=160)
root.mainloop()
