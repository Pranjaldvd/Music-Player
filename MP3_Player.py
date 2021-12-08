import tkinter as tk
import os
import fnmatch
import pygame
from pygame import mixer

#Initialized The Tkinter And Geometry Of The Canvas
canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x500")
canvas.config(bg='black')

#Initialized Mixer
mixer.init()

#Created Root Path For The MP3 Files
rootpath = "C:\\Users\hp\Desktop\Python Project\Songs"
pattern = "*.mp3"

#Assigned Icons 
prev_img = tk.PhotoImage(file = "prev_img.png")
next_img = tk.PhotoImage(file = "next_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")

#Method For Selecting A Song And Playing It
def selectAndPlaySong():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

#Method For Stopping A Song
def stopSong():
    mixer.music.stop()
    listBox.select_clear('active')

#Method For Playing The Next Song
def playNextSong():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

#Method For Playing The Previous Song
def playPrevSong():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text = prev_song_name)

    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

#Method For Pausing The Current Song
def pauseSong():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"
    
#Initialized The ListBox For Displaying The Songs List
listBox = tk.Listbox(canvas, fg="pink", bg="black", width=100, font=('ds-digital', 15))
listBox.pack(padx=15, pady=15)

#Initialized The Space For Displaying The Current Song Name
label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('ds-digital', 18))
label.pack(pady=15)

#Initialized The Body Of The Canvas
top = tk.Frame(canvas , bg='black')
top.pack(padx=10 , pady= 5, anchor= 'center')

#Initialized The Prev Button
prevButton = tk.Button(canvas, text= "Prev", image = prev_img , bg = 'black', borderwidth = 0, command = playPrevSong)
prevButton.pack(pady=15 , in_= top , side="left")

#Initialized The Stop Button
stopButton = tk.Button(canvas, text= "Stop", image = stop_img , bg = 'black', borderwidth = 0, command = stopSong)
stopButton.pack(pady=15, in_= top , side="left")

#Initialized The Next Button
nextButton = tk.Button(canvas, text= "Next", image = next_img , bg = 'black', borderwidth = 0, command = playNextSong)
nextButton.pack(pady=15, in_= top , side="left")

#Initialized The Play Button
playButton = tk.Button(canvas, text= "Play", image = play_img , bg = 'black', borderwidth = 0, command = selectAndPlaySong)
playButton.pack(pady=15, in_= top , side="left")

#Initialized The Pause Button
pauseButton = tk.Button(canvas, text= "Pause", image = pause_img , bg = 'black', borderwidth = 0, command = pauseSong)
pauseButton.pack(pady=15, in_= top , side="left")

#Fetching The Files From The Directory By Using The Rootpath
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
