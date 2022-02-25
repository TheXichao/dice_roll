from tkinter import *
from tkinter import messagebox
import json

def displayloginWindow():
    loginWindow = Tk()
    loginWindow.title("Login")
    loginWindow.geometry("300x200")

    # creating login label and entry

    loginLabel = Label(loginWindow, text="Username: ")
    loginLabel.grid(row=0, column=0)

    loginEntry = Entry(loginWindow)
    loginEntry.grid(row=0, column=1)

    # create password label and entry

    passwordLabel = Label(loginWindow, text="Password: ")
    passwordLabel.grid(row=1, column=0)

    passwordEntry = Entry(loginWindow)
    passwordEntry.grid(row=1, column=1)

    # get the username and password from the entry
    username = loginEntry.get()
    password = passwordEntry.get()

    # create login button

    loginButton = Button(loginWindow, text="Login", command=verifyLogin(username, password))
    loginButton.grid(row=2, column=1)

    # create register button

    registerButton = Button(loginWindow, text="Register", command=DisplayRegisterWindow)
    registerButton.grid(row=2, column=0)

    loginWindow.mainloop()


# login function
def verifyLogin(username, password):
    loginSucessful = False
    # read from users.json and check if the username and password are correct
    with open("users.json", "r") as file:
        users = json.load(file)
        if username in users:
            if users[username] == password:
                messagebox.showinfo("Login", "Login successful")
                loginSucessful = True
            else:
                messagebox.showerror("Login", "Incorrect password")
        else:
            messagebox.showerror("Login", "Incorrect username")
    return loginSucessful



# create register function
def DisplayRegisterWindow():

    registerWindow = Tk()
    registerWindow.title("Register")
    registerWindow.geometry("300x200")

    # create username label and entry
    usernameLabel = Label(registerWindow, text="Username: ")
    usernameLabel.grid(row=0, column=0)

    usernameEntry = Entry(registerWindow)
    usernameEntry.grid(row=0, column=1)

    # create password label and entry
    passwordLabel = Label(registerWindow, text="Password: ")
    passwordLabel.grid(row=1, column=0)

    passwordEntry = Entry(registerWindow)
    passwordEntry.grid(row=1, column=1)
    
    username = usernameEntry.get()
    password = passwordEntry.get()

    # create register button
    signupButton = Button(registerWindow, text="Sign up", command=signUp(username, password))
    
# create sign up button and when clicked it will add the username and password to the users.json file if the username is not already in the file

def signUp(username, password):

    with open("users.json", "r") as file:
        users = json.load(file)
        if username in users:
            messagebox.showerror("Sign up", "Username already exists")
        else:
            users[username] = password
            with open("users.json", "w") as file:
                json.dump(users, file)
                messagebox.showinfo("Sign up", "Sign up successful")
                


displayloginWindow()