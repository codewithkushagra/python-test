# importing only those functions 
# which are needed 
from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window 
root = Tk() 
  
# Adding widgets to the root window 
Label(root, text = 'GeeksforGeeks', font =('Verdana', 15)).pack() 
  
# Creating a photoimage object to use image 
photo = PhotoImage(file = r"C:\Users\Kushagra Agarwal\OneDrive\Desktop\Python test\ha.png") 
  
# here, image option is used to 
# set image on button 
Label(root, image = photo).pack() 
  
mainloop() 
