from tkinter import *
import tkinter.messagebox as msg
import game

class LoginPage(Tk):
    """
    creates log in window
    """

    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Login')
        self.config(bg='#f60349')

        # creating login label and entry

        self.loginLabel = Label(self, text="Username: ")
        self.loginLabel.grid(row=0, column=0)

        self.loginEntry = Entry(self)
        self.loginEntry.grid(row=0, column=1)

        # create password label and entry

        self.passwordLabel = Label(self, text="Password: ")
        self.passwordLabel.grid(row=1, column=0)

        self.passwordEntry = Entry(self)
        self.passwordEntry.grid(row=1, column=1)

        # get the username and password from the entry
        self.username = self.loginEntry.get()
        self.password = self.passwordEntry.get()

        # create login button

        self.loginButton = Button(self, text="Login", command=self.verifyLogin)
        self.loginButton.grid(row=2, column=1)

        # create register button

        self.registerButton = Button(self, text="Register", )
        self.registerButton.grid(row=2, column=0)

    # login function
    def verifyLogin(self):
        if self.username == '' or self.password == '':
            msg.showwarning('empty field', 'please fill in all the options')
        else:
            gamePage = game.GamePage()

if __name__ == '__main__':
    myApp = LoginPage()
    myApp.mainloop()
