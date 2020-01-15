from tkinter import *
import threading
import random
import pygame
from tkinter import messagebox
import os
import sys

colo = "#add8e6"
csco = 0
score = 0
prevx = 200
prevy = 200
tey = "ducky.png"
x = 200
y = 200
user = ""

def encrypt(s):
    return bin(int(s))

def decrypt(s):
    return int(s, 2)

os.system('clear')
try:
    tr = open("user.txt", "r").read()
    pos = tr.index("\n")
    for i in range(pos):
        user += tr[i]

    score = int(decrypt(tr.replace(user, "")))
except:
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("Welcome To The Duck Game, made by Abhay Tripathi. Please Read The Game Instructions Below Then Kindly Enter Your Desired Username.")
    print()
    print("Game Instructions:")
    print()
    print("1. To Earn Points, Click On The Moving Duck. 1 Click = 1 Point.")
    print("2. When You Click The Duck, A Ping Sound Will Confirm Your Click And The Point Will Be Recorded.")
    print("3. High Score Of Every User Is Maintained.")
    print("4. Enjoy The Game!!!")
    print()
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print()
    wr = open("user.txt", "w")
    user = input("Kindly Enter Your Desired Username: ")
    wr.write(user + "\n" + encrypt("0"))
    wr.close()

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.attributes("-fullscreen", True)
root.configure(background = colo)
f = Frame(root)

width = 178
height = 0
photon = PhotoImage(file = "plant.png")
while width < screen_width:
    l = Label(root, image = photon, bg = colo)
    l.place(x = width, y = height)
    width += 178
else:
    height += 140
    width -= 178
    while height < screen_height:
        l = Label(root, image = photon, bg = colo)
        l.place(x = width, y = height)
        height += 140
    else:
        height -= 140
        while width > -20:
            l = Label(root, image = photon, bg = colo)
            l.place(x = width, y = height)
            width -= 178
        else:
            width += 178
            while height > 0:
                l = Label(root, image = photon, bg = colo)
                l.place(x = width, y = height)
                height -= 140

lkx = Label(root, text = user, font = "Helvetica 37 bold", bg = "yellow", fg = "blue")
lkx.place(x = 0, y = 0)
if score == 1:
    pts = "Point"
else:
    pts = "Points"

if csco == 1:
    ptsg = "Point"
else:
    ptsg = "Points"
lk = Label(root, text = "High Score: " + str(score) + " " + pts + "  " + "\n" + "Current Score: " + str(csco) + " " + ptsg + "  ", font = "Helvetica 11 bold", bg = "yellow", fg = "brown")
lk.place(x = 0, y = 60)

lks = Label(root, text = "Duck Game", font = "Helvetica 60 bold", bg = "#9ccd8e", fg = "red")
lks.place(x = (screen_width // 2.5), y = 0)

lksc = Label(root, text = "by\nAbhay Tripathi", font = "Helvetica 20 bold", bg = "#9ccd8e", fg = "blue", justify = CENTER)
lksc.place(x = (screen_width // 2.5) + 120, y = 80)

lksc = Label(root, text = "Catch The Duck By Clicking It. 1 Click = 1 Point.", font = "Helvetica 15 bold", bg = "#ffc0cb", fg = "#013220")
lksc.place(x = 0, y = screen_height - 25)

pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound('Water.wav'), loops = -1)

def action():
    global csco
    global score
    pygame.mixer.init()
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('button.wav'))
    csco += 1
    if csco > score:
        fw = open("user.txt", "w")
        fw.write(user + "\n" + encrypt(str(csco)))
        fw.close()
        score = csco

    if score == 1:
        ptsx = "Point"
    else:
        ptsx = "Points"

    if csco == 1:
        ptsgx = "Point"
    else:
        ptsgx = "Points"

    lk.config(text = "High Score: " + str(score) + " " + ptsx + "  " + "\n" + "Current Score: " + str(csco) + " " + ptsgx + "  ")

photo = PhotoImage(file = "ducky.png")
b = Button(root, image = photo, borderwidth = 0, highlightthickness = 0, bg = colo, command = action)
b.place(x = 200, y = 200)
b.config(activebackground = b.cget('background'))
def position():
    global x
    global y
    global prevx
    global prevy

    if prevx != x:
        global tey
        if prevx > x:
            if tey != "duckyr.png":
                tey = "duckyr.png"
                photoxc = PhotoImage(file = tey)
                b.config(image = photoxc)
                b.image = photoxc
            if prevx - 9 < x:
                prevx -= prevx - x
            else:
                prevx -= 9

        elif prevx < x:
            if tey != "ducky.png":
                tey = "ducky.png"
                photox = PhotoImage(file = tey)
                b.config(image = photox)
                b.image = photox
            if prevx + 9 > x:
                prevx += x - prevx
            else:
                prevx += 9


    if prevy != y:
        if prevy > y:
            if prevy - 9 < y:
                prevy -= prevy - y
            else:
                prevy -= 9

        elif prevy < y:
            if prevy + 9 > y:
                prevy += y - prevy
            else:
                prevy += 9

    b.place(x = prevx, y = prevy)
    threading.Timer(0.0000001, position).start()
position()

def Quack():
    pygame.mixer.init()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('duck.wav'))
    threading.Timer(5, Quack).start()
Quack()


def motion(event):
    global x
    global y
    global prevx
    global prevy
    xco, yco = event.x, event.y
    if abs(y - yco) < 300:
        if abs(x - xco) < 300:
            x = random.randint(250, screen_width - 250)
            y = random.randint(230, screen_height - 230)

root.bind('<Motion>', motion)

def on_closing():
    if messagebox.askokcancel("Duck Game", "Do you want to quit?"):
        root.destroy()
        pygame.mixer.stop()
        os.system('clear')
        print("Thank You For Playing! We hope you enjoyed playing the Duck Game!")
        os.system("pkill -f duckgame.py")

eb = Button(root, text = "EXIT GAME", command = on_closing, font = "Helvetica 20 bold", bg = "#ffe5b4", fg = "purple", justify = CENTER)
eb.place(x = screen_width - 162, y = screen_height - 40)

root.protocol("WM_DELETE_WINDOW", on_closing)
f.pack()
f.mainloop()
