from Tkinter import *
from PIL import ImageTk, Image
import os
import subprocess

def webcam_call():
	subprocess.call("python webcamtest.py", shell=True)

def sign_check():
	subprocess.call("python tester.py", shell=True)


	lbl.configure(text="Good job, that's correct!")


#create the window
root = Tk()

#modify root window
root.title("AceASL")
root.geometry("500x500")#Width x Height

img = ImageTk.PhotoImage(Image.open("/home/ahalyamandana/sign_language_project/tf_files/sign_photos/Y.jpg"))
panel = Label(root, image = img)
panel.pack(side="top", fill = "both", expand = "yes")

app = Frame(root)
app.pack(side='bottom',pady=50)
button1 = Button(app, text = "Click here to record your Y sign!",font=("Garamond", 16), command=webcam_call,bg='#ffa64d')
button1.pack()
button2 = Button(app, text = "Check if you got it right!",font=("Garamond", 16),command=sign_check,bg='#ff3333')
button2.pack()
lbl = Label(app,text="",font=("Garamond", 16))
lbl.pack()
#---------------------------------------------------------


#Start the event loop
root.mainloop()
