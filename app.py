import tkinter as tk                            #Tkinter will help in creating GUI
from tkinter import END, filedialog, Listbox  #filedialog will help in picking apps. Text will help to  display text in different forms
import os
       #to run the apps we are going to add

root=tk.Tk()

apps=[] #A list to store the location of all apps opened 

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps=f.read()
        tempApps=tempApps.split(',')       
        apps=[x for x in tempApps if x.strip()]

def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()    #To start new with each new file opened and delete all the previous memory
    
    filename= filedialog.askopenfilename(initialdir="/", filetypes=(("executables", "*.exe"),("All files","*.*"))) #Describing the type of file to be opened "askopenfilename"
    apps.append(filename) #Adding files to the list
    print(filename)
    for app in apps:
        label=tk.Label(frame, text=app) #Displaying label of the app opened on the frame 
        label.pack()

def openApp():
    
    for app in apps:
        os.startfile(app)

canvas=tk.Canvas(root,bg="#293462", height="750", width="1000") #Canvas is the main bg on which we can add other graphics, text, widgets etc
canvas.pack()

frame=tk.Frame(root, bg="#D4F6CC")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #setting relative height, width and other parameters of frame wrt canvas

openFile=tk.Button(root, text="Open File", padx=10, pady=4, fg="white", bg="#293462", command=addApp)
openFile.pack(padx=5, pady=5, side=tk.LEFT)

openApps=tk.Button(root, text="Run Apps", padx=10, pady=4, fg="white", bg="#293462", command=openApp)
openApps.pack(padx=5, pady=10, side=tk.RIGHT)

for app in apps:
    label=tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f: #to add a text file which stores file names which have been recently added to the apps[]
    for app in apps:
        f.write(app + ',')