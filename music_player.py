from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from turtle import right
from pygame import mixer
import os

#creatinga a root window
root=Tk()
root.title('Music player by Jayant')
root.geometry("920x670+290+85")
root.configure(bg= "#0f1a2b")
root.resizable(False, False)
mixer.init()

#creating function for player
def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdire(path)
 
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
 
def Play_Music():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

#icon
Icon_Image = PhotoImage(file="C:/Users/user/Downloads/music-logo-png-2342.png")
root.iconphoto(False, Icon_Image)

Top_Image = PhotoImage(file="C:\\Users\\user\\Downloads\\music-logo-png-2348.png")
Label(root, image=Top_Image, bg="#0f1a2b").place(x=350, y=50)
 
#logo
logo_Image = PhotoImage(file="C:\\Users\\user\\Downloads\\music-logo-png-2342.png")
Label(root, image=logo_Image, bg="#0f1a2b").place(x=65, y=115)

# Button
Button_Play = PhotoImage(file="C:\\Users\\user\\Downloads\\pngwing.com.png").subsample(6) 
Button(root, image=Button_Play, bg="#0f1a2b", bd=0, command=Play_Music).place(x=100, y=400)
 
Button_Stop = PhotoImage(file="C:\\Users\\user\\Downloads\\pngwing.com (1).png").subsample(6)  # Resizing by a factor of 2
Button(root, image=Button_Stop, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=100, y=500)

 


Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=360, y=390, width=500, height=200)
 
Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="Black", bg="#21b3de", command= Add_Music).place(x=360, y=340)
 
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
 
root.mainloop()

