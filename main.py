import login

from tkinter import *
import tkinter.messagebox as msg


"""
colours:

purple #A4036F
blue #048BA8
teal #16DB93
yellow #EFEA5A
orange #F29E4C
"""
class MainPage(Tk):
    '''creates log in window'''
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Login')
        self.config(bg='#000000')

        # create button that opens different pages

        self.launchLoginButton = Button(self,text='Login',command=self.launchLoginPage)
        self.launchLoginButton.place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.6)

    def launchLoginPage(self):
        loginPage = login.LoginPage()


if __name__ == '__main__':
    myApp = MainPage()
    myApp.mainloop()