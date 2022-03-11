from PIL import Image, ImageTk
from tkinter import *

class GamePage(Tk):
    '''creates log in window'''
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Login')
        self.config(bg='#e0e2db')


        #images 

        self.image1 = Image.open('Z:\Dev\working\dice_roll\cardImagesace_of_spades.png')
        self.image1 = self.image1.resize((300,300),Image.ANTIALIAS)
        test = ImageTk.PhotoImage(self.image1)

        label1 = self.tkinter.Label(image=test)
        label1.image = test

        
    


if __name__ == '__main__':
    myApp = GamePage()
    myApp.mainloop()