#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
from time import strftime
import os
#creating instance of TK
root=Tk()

root.configure(background="white")

def function1():
    
    os.system("python Capture_Images.py")
    
def function2():
    
    os.system("python Train_Dataset.py")

def function3():

    os.system("python Recognizer.py")
   
def function6():
    root.destroy()

def attend():
    date = strftime("%d-%m-%Y")
    cmd = '"C:\\Program Files\\LibreOffice\\program\\soffice.exe" -o Attendance_sheet_of_%s.csv'%date
    os.system(cmd)

#stting title for the window
root.title("ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="#ff3333",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Capture Images",font=("times new roman",20),bg="#33adff",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#33adff",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize",font=('times new roman',20),bg="#1aa3ff",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#1aa3ff",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="#ff3333",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()