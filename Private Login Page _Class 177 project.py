from tkinter import *

root=Tk()
root.title("Login Page")
root.geometry("600x600")

label_name=Label(root,text="Name : ")
label_name.place(relx=0.3,rely=0.1,anchor=CENTER)

name_input=Entry(root,)
name_input.place(relx=0.6,rely=0.1,anchor=CENTER)

label_pwd=Label(root,text="Password : ")
label_pwd.place(relx=0.3,rely=0.2,anchor=CENTER)

pwd_input=Entry(root)
pwd_input.place(relx=0.6,rely=0.2,anchor=CENTER)

label_captcha=Label(root,text="Captcha : ")
label_captcha.place(relx=0.3,rely=0.3,anchor=CENTER)

captcha_input=Entry(root)
captcha_input.place(relx=0.6,rely=0.3,anchor=CENTER)


name=Label(root)
name.place(relx=0.3,rely=0.6,anchor=CENTER)

pwd=Label(root)
pwd.place(relx=0.3,rely=0.7,anchor=CENTER)

captcha=Label(root)
captcha.place(relx=0.3,rely=0.8,anchor=CENTER)


class UserDB:
    def __init__(self):
        self.__username="krisha"
        self.__password="krisha123"
        self.captcha="abcdefrfji"
    def showUser(self): 
        name["text"]="name: " + self.__username
        pwd["text"]="password: " + self.__password
        captcha["text"]="captcha: " + self.captcha

obj1=UserDB()
def addUser():
    global obj1
    obj1.username=name_input.get()
    obj1.password=pwd_input.get()
    obj1.captcha=captcha_input.get()
    print("details Updated")
    

btn1=Button(root,text="Update Login Details",command=addUser)
btn1.place(relx=0.3,rely=0.5,anchor=CENTER)

btn2=Button(root,text="Show Profile",command=obj1.showUser)
btn2.place(relx=0.6,rely=0.5,anchor=CENTER)

root.mainloop()
    
    
    