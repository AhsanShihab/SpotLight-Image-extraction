# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:34:08 2019

@author: Shihab
"""
# Importing libraries
import os
from getpass import getuser
from shutil import copyfile
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog


# Getting the username
user = getuser()

# setting the directory of the spotlight images
src='C:/Users/'+user+'/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'

# setting directory to save the jpeg files
try:
    with open('prefered directory', 'r') as filehandle:
        dist = filehandle.read()
except:
    dist = 'C:/Users/'+user+'/Desktop/SpotLight Wallpaper'
    if not os.path.exists(dist):
        os.mkdir(dist)



# Take the list of all images so far (has to come from memory)
all_img_list=[]
try:
    with open('listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            all_img_list.append(currentPlace)
except:
    pass

img_serial = len(all_img_list)
def check_new_img():
    global new_img_list
    # listing the current files in src dir that are larger than 200KB
    curr_img_list = []
    file_list = os.listdir(src)
    for file in file_list:
        if os.path.getsize(src+'/'+file)>204800:
            curr_img_list.append(file)
    
    # Form a list of new imgs
    new_img_list = []
    new_file_exist = False
    for img in curr_img_list:
        if img not in all_img_list:
            new_img_list.append(img)
            all_img_list.append(img)
            new_file_exist = True
    if new_file_exist:
        return True
    else:
        False
# Copying the files to the jpeg directory 
def extract():
    global img_serial
    new_file_exist = check_new_img()
    if new_file_exist:
        i= img_serial + 1
        count=0
        for img in new_img_list:
            new_dist = dist+'/img_'+str(i)+'.jpeg'
            duplicate = 0
            while os.path.exists(new_dist):
                if duplicate==0:
                    new_dist = new_dist[:-5]+ '_(' + str(duplicate) + ').jpeg'
                else:
                    new_dist = new_dist[:-8]+ '(' + str(duplicate) + ').jpeg'
                duplicate+=1
            copyfile(src+'/'+img, new_dist)
            i+=1
            count+=1
        
        with open('listfile.txt', 'w') as filehandle:
            for listitem in all_img_list:
                filehandle.write('%s\n' % listitem)
        messagebox.showinfo("Complete","Done! {} images are extracted".format(count))
        
        img_serial = i-1
    else:
        messagebox.showinfo("No new Images!", "No new Images!\n(If you think that's a mistake, try resetting the program")
        
def reset():
    global all_img_list
    global img_serial
    with open('listfile.txt', 'w') as filehandle:
        filehandle.write('')
    all_img_list=[]
    img_serial = len(all_img_list)
    messagebox.showinfo("Reset!", "Program memory was reset")
    
def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global dist
    temp = filedialog.askdirectory()
    if not temp == '':
        dist = temp
    distTK.set(dist)
    with open('prefered directory', 'w') as filehandle:
        filehandle.write(dist)

# Making GUI
## Making the main window
WIDTH, HEIGTH = 700, 500
root = Tk()
root.title("Windows SpotLight Image Extractor")
root.geometry('{}x{}'.format(WIDTH, HEIGTH))
root.resizable(False, False)

## Background image
C = Canvas(root, bg="blue")
try:
    original = Image.open('background.png')
    resized = original.resize((WIDTH, HEIGTH),Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    background_label = Label(root, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    lbl9 = Label(root, text="(background image missing)")
    lbl9.grid(column=0, row=0)
    lbl9.place(x= WIDTH/2, y= 100, anchor="center")

## Greeting the user
lbl1 = Label(root, text="Welcome, "+str(user)+'!', font=("Arial Bold", 20))
lbl1.grid(column=0, row=0)
lbl1.place(x= WIDTH/2, y= 50, anchor="center")

## Describing the APP
msg1= "Click the button to start extracting"
msg2 = "Click browse to change the saving directory"
lbl2 = Label(root, text=msg1+"\n"+msg2, font=("Arial", 12), background='silver')
lbl2.grid(column=0, row=0)
lbl2.place(x= WIDTH/2, y= HEIGTH-150, anchor="center")

## Button for Extracting
btn = Button(root,text='Start Exporting',borderwidth=0,command=extract)
btn.grid(column=0,row=0)
btn.place(x= WIDTH/2, y= HEIGTH-100, anchor="center")
try:
    img = PhotoImage(file="button_start-extracting.png") # make sure to add "/" not "\"
    btn.config(image=img)
except:
    lbl9 = Label(root, text="(button image missing)")
    lbl9.grid(column=0, row=0)
    lbl9.place(x= WIDTH/2, y= HEIGTH-80, anchor="center")
    btn.config(borderwidth=2)
    
## Button for resetting
btn2 = Button(root,text='Reset',borderwidth=0,command=reset)
btn2.grid(column=0,row=0)
btn2.place(x= WIDTH/2, y= HEIGTH-50, anchor="center")

## Label for showing saving dir
distTK = StringVar()
distTK.set(dist)
lbl3 = Label(master=root,textvariable=distTK)
lbl3.grid(row=1, column=0)
lbl3.place(x= 10, y= HEIGTH-10, anchor="sw")

## Button for Browsing directory
btn3 = Button(text="Browse", command=browse_button)
btn3.grid(row=0, column=0)
btn3.place(x= WIDTH - 10, y= HEIGTH-10, anchor="se")

## GUI loop for refreshing
root.mainloop()
