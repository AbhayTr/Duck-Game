#FILE/SCRIPT NAME: DUCKGAME.PY.
#NAME OF CODER/STUDENT: ABHAY TRIPATHI, XI - J, ROLL NO. 4.
#ALL RESOURCES ARE ATTACHED WITH THE SCRIPT i.e. SAME FOLDER.
#KINDLY IGNORE SPELLING AND GRAMMAR MISTAKES IN CODE EXPLAINING COMMENTS.
#START OF CODE
try:
    from tkinter import *                                                                                   #import graphics (frame, button, etc.).
    from tkinter import messagebox                                                                          #confirmation dialog box that whether to exit the game or not. Imported seperately for conveneince.
except:
    print("Please Install Tkinter Module To Play The Game By The Following Command")                        #install tkinter module for graphics (i.e. module not installed).
    print()                                                                                                 #for cmd neatness.
    print("pip install tkinter")                                                                            #line required to be executed to install the module.
    print()                                                                                                 #for cmd neatness.
    exit()                                                                                                  #close the app.

import threading                                                                                            #required for scheduling position check of the duck.
import random                                                                                               #required for giving random co-ordinates for the duck to escape when user about to click the duck.
try:
    import pygame                                                                                           #required for all the audio effects.
except:
    print("Please Install Pygame Module To Play The Game By The Following Command")                         #install pygame for audio (i.e. module not installed).
    print()                                                                                                 #for cmd neatness.
    print("pip install pygame")                                                                             #line required to be executed to install the module.
    print()                                                                                                 #for cmd neatness.
    exit()                                                                                                  #close the app.

import os                                                                                                   #required for clearing the cmd and killing all the threads scheduled.
import sys                                                                                                  #required for getting the operating system on which the script is running to execute respective commands.

colo = "#add8e6"                                                                                            #background color (color of water i.e. light blue).
csco = 0                                                                                                    #current score of the user i.e. during the current session of game.
score = 0                                                                                                   #high score of the user i.e. the highest score achieved by the user during all played sessions of the game.
prevx = 200                                                                                                 #the x - co-ordinate of the duck before random generation of the new x - co-ordinate.
prevy = 200                                                                                                 #the y - co-ordinate of the duck before random generation of the new y - co-ordinate.
plat = sys.platform                                                                                         #the system on which the game is running.
tey = "ducky.png"                                                                                           #the image file of the duck.
x = 200                                                                                                     #the x - co-ordinate of the duck which keeps getting updated by random.
y = 200                                                                                                     #the y - co-ordinate of the duck which keeps getting updated by random.
user = ""                                                                                                   #name of the player entered at the first run of the game by the user.

def encrypt(s):                                                                                             #basic encryption of score so that user can't edit the score directly in the txt file.
    return bin(int(s))                                                                                      #int to bin (basic encryption which only computer science students can decrypt).

def decrypt(s):                                                                                             #decryption for getting the score from encrypted score received from the text file.
    return int(s, 2)                                                                                        #bin to int (reverse of int to bin).

if plat == "linux":                                                                                         #different commands to clear cmd in windows and linux. Clearing to remove pygame credits.
    os.system("clear")
else:
    os.system("cls")

try:
    tr = open("user.txt", "r").read()                                                                       #opening txt file containing user's name and his/her score.
    pos = tr.index("\n")                                                                                    #format of txt file is user's name \n user's encrypted score.
    for i in range(pos):                                                                                    #all text before \n i.e. user's name.
        user += tr[i]                                                                                       #adding each charecter to get user's name.

    score = int(decrypt(tr.replace(user + "\n", "")))                                                       #removing user's name and \n will only leave user's encrypted score which is decrypted with decrypt function.
    if plat == "linux":                                                                                     #different commands to clear cmd in windows and linux. Clearing to remove pygame credits.
        os.system("clear")
    else:
        os.system("cls")
except:                                                                                                     #first time run or txt file corrupted. Does not matter as all data will be overwritten with the new data.
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
    wr = open("user.txt", "w")                                                                              #creating user.txt file to store new data. if old file was corrupted, it will be removed and made again.
    user = input("Kindly Enter Your Desired Username: ")                                                    #taking the name of the user as an input from the user.
    wr.write(user + "\n" + encrypt("0"))                                                                    #writting user's name and user's encrypted score in the format user's name \n user's encrypted score.
    wr.close()                                                                                              #close the file.

root = Tk()                                                                                                 #inisitialising the tkinter graphics.
screen_width = root.winfo_screenwidth()                                                                     #getting screen width for co-ordinates and border purposes.
screen_height = root.winfo_screenheight()                                                                   #getting screen height for co-ordinates and border purposes.
root.attributes("-fullscreen", True)                                                                        #going fullscreen.
root.configure(background = colo)                                                                           #settting water background defined above.
f = Frame(root)                                                                                             #assigning graphics to frame.

width = 178                                                                                                 #starting the process of making the plants border. width not 0 for giving space to user and score details.
height = 0                                                                                                  #height is 0 as first making the top border.
photon = PhotoImage(file = "plant.png")                                                                     #plant image file.
while width < screen_width:                                                                                 #loop for adding plant image to top border until width of screen is covered.
    l = Label(root, image = photon, bg = colo)                                                              #making the plant image placable.
    l.place(x = width, y = height)                                                                          #placing the plant image in the top border with it's respective x - co-ordinates.
    width += 178                                                                                            #adding width of plant image in pixels to existing width to fill border from left to right.
else:                                                                                                       #once top border made, then: (ignore the small error in aligning of the last plant in the top border).
    height += 140                                                                                           #now making right hand border.
    width -= 178                                                                                            #correction of width as in the last run of the top border loop, width exceeded the screen width.
    while height < screen_height:                                                                           #loop for adding plant image to the right hand border until height of screen is covered.
        l = Label(root, image = photon, bg = colo)                                                          #making the plant image placable.
        l.place(x = width, y = height)                                                                      #placing the plant image in the right hand border with it's respective y - co-ordinates.
        height += 140                                                                                       #adding height of plant image in pixels to existing height to fill border from top to bottom.
    else:                                                                                                   #once right hand border made, then: (ignore the small error in aligning of the last plant in the right hand border).
        height -= 140                                                                                       #correction of height as in the last run of the right hand border loop, height exceeded the screen height.
        while width > -20:                                                                                  #now making bottom border (loop for adding plant image to the bottom border until width is -20 (to allow last plant to be filled)).
            l = Label(root, image = photon, bg = colo)                                                      #making the plant image placable.
            l.place(x = width, y = height)                                                                  #placing the plant image in the bottom border with it's respective x - co-ordinates.
            width -= 178                                                                                    #substracting width of plant image in pixels to existing width to fill border from right to left.
        else:                                                                                               #once bottom border made, then:
            width += 178                                                                                    #correction of width as in the last run of the bottom border loop, width went below -20.
            while height > 0:                                                                               #now making left hand border (loop for adding plant image to the left hand border until height is 0 (to not allow last plant to be filled)).
                l = Label(root, image = photon, bg = colo)                                                  #making the plant image placable.
                l.place(x = width, y = height)                                                              #placing the plant image in the left hand border with it's respective y - co-ordinates.
                height -= 140                                                                               #substracting height of plant image in pixels to existing height to fill border from bottom to top leaving one space for user's name and score details.
                                                                                                            #border complete!!!
lkx = Label(root, text = user, font = "Helvetica 37 bold", bg = "yellow", fg = "blue")                      #user's name details label.
lkx.place(x = 0, y = 0)                                                                                     #positioning above label with respective x and y co-ordinates.
if score == 1:                                                                                              #if 1 Point, then showing 1 'Point', else shwing score 'Points'.
    pts = "Point"
else:
    pts = "Points"

if csco == 1:                                                                                               #if 1 Point, then showing 1 'Point', else shwing score 'Points'.
    ptsg = "Point"
else:
    ptsg = "Points"
lk = Label(root, text = "High Score: " + str(score) + " " + pts + "  " + "\n" + "Current Score: " + str(csco) + " " + ptsg + "  ", font = "Helvetica 11 bold", bg = "yellow", fg = "brown") #user's current and high score details label.
lk.place(x = 0, y = 60)                                                                                     #positioning above label with respective x and y co-ordinates.

lks = Label(root, text = "Duck Game", font = "Helvetica 60 bold", bg = "#9ccd8e", fg = "red")               #game name heading (for style).
lks.place(x = (screen_width // 2.5), y = 0)                                                                 #positioning in center of screen with respect to screen width.

lksc = Label(root, text = "by\nAbhay Tripathi", font = "Helvetica 20 bold", bg = "#9ccd8e", fg = "blue", justify = CENTER) #showing off my coding skills and taking credit for my hard work with this label.
lksc.place(x = (screen_width // 2.5) + 120, y = 80)                                                         #positioning above label w.r.t the game name heading such that positons in center.

lksc = Label(root, text = "Catch The Duck By Clicking It. 1 Click = 1 Point.", font = "Helvetica 15 bold", bg = "#ffc0cb", fg = "#013220") #how to play label.
lksc.place(x = 0, y = screen_height - 25)                                                                   #positioning above label to bottom left of the screen.

pygame.mixer.init()                                                                                         #inisitialising the pygame audio player.
pygame.mixer.Channel(0).play(pygame.mixer.Sound('Water.wav'), loops = -1)                                   #playing moving water sound on channel 0 (to play multiple sounds together) with infinite repeat on.

def action():                                                                                               #function to be performed on the click of the duck.
    global csco                                                                                             #local to global.
    global score                                                                                            #local to global.
    pygame.mixer.init()                                                                                     #inisitialising the pygame audio player.
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('button.wav'))                                          #playing the ping sound to confirm the duck click at channel 2 (for playing multiple sounds together).
    csco += 1                                                                                               #updating the current score.
    if csco > score:                                                                                        #checking if current score is greater than high score or not. If greater than updating high score of user.
        fw = open("user.txt", "w")
        fw.write(user + "\n" + encrypt(str(csco)))                                                          #encrypting before updating.
        fw.close()
        score = csco                                                                                        #updating high score to current score as current score is greater than high score.

    if score == 1:                                                                                          #if 1 Point, then showing 1 'Point', else shwing score 'Points'.
        ptsx = "Point"
    else:
        ptsx = "Points"

    if csco == 1:                                                                                           #if 1 Point, then showing 1 'Point', else shwing score 'Points'.
        ptsgx = "Point"
    else:
        ptsgx = "Points"

    lk.config(text = "High Score: " + str(score) + " " + ptsx + "  " + "\n" + "Current Score: " + str(csco) + " " + ptsgx + "  ") #updating the current and high score details label.

photo = PhotoImage(file = "ducky.png")                                                                     #photo file of the duck.
b = Button(root, image = photo, borderwidth = 0, highlightthickness = 0, bg = colo, command = action)      #inisitialising the duck.
b.place(x = 200, y = 200)                                                                                  #placing the duck on its initial values i.e. the position of the duck on start of a new game.
b.config(activebackground = b.cget('background'))                                                          #removing button effects to make good graphics.
def position():                                                                                            #function scheduled to make smooth movement of duck to new random co-ordinates whenever required.
    global x                                                                                               #local to global.
    global y                                                                                               #local to global.
    global prevx                                                                                           #local to global.
    global prevy                                                                                           #local to global.

    if prevx != x:                                                                                         #check if new x - co-ordinate has been generated.
        global tey                                                                                         #local to global.
        if prevx > x:                                                                                      #check if the new x - co-ordinate is smaller than the current x - co-ordinate i.e. backward motion of duck.
            if tey != "duckyr.png":                                                                        #check if duck's image file is configured to reverse motion of duck image file or not i.e. mirrior image of duck's image file.
                tey = "duckyr.png"                                                                         #if not, then configuring it.
                photoxc = PhotoImage(file = tey)                                                           #updating image on duck image mapped to duck button.
                b.config(image = photoxc)                                                                  #updating duck button.
                b.image = photoxc                                                                          #saving an instance/reference for garbage collectors.
            if prevx - 9 < x:                                                                              #checking if x component of velcoity of movement of duck will land it a little backward to the new x - co-ordinates or not.
                prevx -= prevx - x                                                                         #if landing it backward, then reduce velocity and make it just enough to land it on the right x - co-ordinate.
            else:
                prevx -= 9                                                                                 #else move with regular velocity i.e. -9 pixels/0.0000001 seconds (- representing backward motion of duck).

        elif prevx < x:                                                                                    #check if the new x - co-ordinate is greater than the current x - co-ordinate i.e. forward motion of duck.
            if tey != "ducky.png":                                                                         #check if duck's image file is configured to forward motion of duck image file or not i.e. actual image of duck's image file.
                tey = "ducky.png"                                                                          #if not, then configuring it.
                photox = PhotoImage(file = tey)                                                            #updating image on duck image mapped to duck button.
                b.config(image = photox)                                                                   #updating duck button.
                b.image = photox                                                                           #saving an instance/reference for garbage collectors.
            if prevx + 9 > x:                                                                              #checking if x component of velcoity of movement of duck will land it a little forward to the new x - co-ordinates or not.
                prevx += x - prevx                                                                         #if landing it forward, then reduce velocity and make it just enough to land it on the right x - co-ordinate.
            else:
                prevx += 9                                                                                 #else move with regular velocity i.e. +9 pixels/0.0000001 seconds (+ representing forward motion of duck).


    if prevy != y:                                                                                         #check if new y - co-ordinate has been generated.
        if prevy > y:                                                                                      #check if the new y - co-ordinate is smaller than the current y - co-ordinate i.e. upward motion of duck.
            if prevy - 9 < y:                                                                              #checking if y component of velcoity of movement of duck will land it a little upward to the new y - co-ordinate or not.
                prevy -= prevy - y                                                                         #if landing it upward, then reduce velocity and make it just enough to land it on the right y - co-ordinate.
            else:
                prevy -= 9                                                                                 #else move with regular velocity i.e. +9 pixels/0.0000001 seconds (+ representing upward motion of duck).

        elif prevy < y:                                                                                    #check if the new y - co-ordinate is larger than the current y - co-ordinate i.e. downward motion of duck.
            if prevy + 9 > y:                                                                              #checking if y component of velcoity of movement of duck will land it a little downward to the new y - co-ordinate or not.
                prevy += y - prevy                                                                         #if landing it downward, then reduce velocity and make it just enough to land it on the right y - co-ordinate.
            else:
                prevy += 9                                                                                 #else move with regular velocity i.e. -9 pixels/0.0000001 seconds (- representing downward motion of duck).

    b.place(x = prevx, y = prevy)                                                                          #moving the duck by updating the co-ordinates received by the above algorithms.
    threading.Timer(0.0000001, position).start()                                                           #scheduling all above checks at rate of 0.0000001 seconds for smooth motion of duck and setting the velcoity of the duck.
position()                                                                                                 #starting the check.

def Quack():                                                                                               #function to make quack sound after every 5 seconds for GUI enhancement (to get the ducky feeling).
    pygame.mixer.init()                                                                                    #inisitialising the pygame audio player.
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('duck.wav'))                                           #playing the quack sound at channel 1 (for playing multiple sounds together).
    threading.Timer(5, Quack).start()                                                                      #scheduling it to play after every 5 seconds.
Quack()                                                                                                    #start the quacking!


def motion(event):                                                                                         #function to get co-ordinates of mouse pointer whenever the mouse moves and to take action according to the closeliness of the pointer to the duck.
    global x                                                                                               #local to global.
    global y                                                                                               #local to global.
    global prevx                                                                                           #local to global.
    global prevy                                                                                           #local to global.
    xco, yco = event.x, event.y                                                                            #getting x and y co-ordinates of mouse pointer on movement of mouse.
    if abs(y - yco) < 300:                                                                                 #check if mouse pointer's height is almost equal to height of duck (first sign of user's attempt to click it).
        if abs(x - xco) < 300:                                                                             #check if mouse pointer's x - co-ordinate is almost equal to x - co-ordinate of duck (if yes, then the duck is in danger and has to move to a safe location).
            x = random.randint(250, screen_width - 250)                                                    #if yes, then generate random x - co-ordinate between 250 and (screen_width - 250) (250 to (screen_width - 250) so that duck does not land on the plant border).
            y = random.randint(230, screen_height - 230)                                                   #if yes, then generate random y - co-ordinate between 230 and (screen_height - 230) (230 to (screen_height - 230) so that duck does not land on the plant border).

#now the position() function, scheduled at 0.0000001 seconds, will immediately pick up the new co-ordinates and move the duck to the new co-ordinates smoothly just in the time where user cannot click it (unless user is very fast).

root.bind('<Motion>', motion)                                                                              #attaching mouse movement listener function motion(event) to the tkinter graphics handler for movement responses and triggering of the function.

def on_closing():                                                                                          #function responsible for handling the closure/exit of the game.
    global plat                                                                                            #local to global.
    if messagebox.askokcancel("Duck Game", "Do you want to quit?"):                                        #check if user replies yes to quitting the game via the do you want to quit the game popup box.
        root.destroy()                                                                                     #if yes, then close fullscreen window.
        pygame.mixer.stop()                                                                                #destroy all pygame audio players.
        if plat == "linux":                                                                                #different commands to clear cmd in windows and linux.
            os.system("clear")
        else:
            os.system("cls")
        print("Thank You For Playing! We hope you enjoyed playing the Duck Game!")                         #thanking the user for playing my game.
        os._exit(0)                                                                                        #performing a total cleanup/killing the script i.e. killing all threads (scheduled functions) and deleting all references/instances.

eb = Button(root, text = "EXIT GAME", command = on_closing, font = "Helvetica 20 bold", bg = "#ffe5b4", fg = "purple", justify = CENTER) #providing a formal way i.e. a button for closing the game. Have declared it here so that can use on_closing() function for exiting the game.
eb.place(x = screen_width - 162, y = screen_height - 40)                                                   #positioning the exit button on the bottom right side of the screen.

root.protocol("WM_DELETE_WINDOW", on_closing)                                                              #attaching on_closing() function to closure of tkinter graphics handler i.e. exit of the game so that it calls the on_closing() function at the time of closing of the game.
f.pack()                                                                                                   #tkinter graphic handler is implementing all positioning, referencing and mapping of functions to graphic objects declared in the script.
f.mainloop()                                                                                               #starting of all the scheduler threads and showing of the game in front of the user.
#END OF CODE
#COMPUTER SCIENCE PROJECT 2019 - 2020 BY ABHAY TRIPATHI.
