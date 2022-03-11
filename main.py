import login

from tkinter import *
import tkinter.messagebox as msg

class MainPage(Tk):
    '''creates log in window'''
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Login')
        self.config(bg='#ffffff')

        # create button that opens different pages

        self.launchLoginButton = Button(self,text='Login',command=self.launchLoginPage)
        self.launchLoginButton.grid(row=5, column=5)

    def launchLoginPage(self):
        loginPage = login.LoginPage()


if __name__ == '__main__':
    myApp = MainPage()
    myApp.mainloop()