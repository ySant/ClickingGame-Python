#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A clicking game.
One hundred buttons numbered from 0 to 99 to be clicked sequentially. The positions of the buttons are scrambled. There is a time limit using a timer. 
-
This is a clone from a similar game I found in the Internet. 
(https://www.sporcle.com/games/RobPro/1-100-click-me)
Here is an implementation in Python3 with Tkinter.
- 
Author: Yudi Santoso
Version: 1.01
Date: May 2017
"""
import tkinter as tk
import numpy as np

def startGame():
   com['text'] = "Start clicking!"
   com['fg'] = 'green'
   cnum[0]=0
   hint['text'] = cnum[0]
   global time_left
   time_left = 300
   startButton.config(text="ReStart")
   global so
   so = np.random.permutation(100)
   print(so)
   for i in range(100):
      buttons[i]["text"] = so[i]
      buttons[i]["state"] = 'normal'
      buttons[i]["command"] = lambda x=so[i], xi=i, cnum=cnum: clicked(x,xi,cnum)
   pauseButton.config(state="normal")
   cancel_timer()
   countdown()


def pauseGame():
#   print(so)
   if (pauseButton['text'] == 'Pause'):
      com['text'] = "Game paused."
      com['fg'] = 'yellow'
      cancel_timer()
      for i in range(100):
         buttons[i].config(state ='disabled', text ="")
      pauseButton.config(text="Resume")
   else:
      com['text'] = "Continue"
      com['fg'] = 'green'
      for i in range(100):
         buttons[i].config(text =so[i])
         if so[i] >= cnum[0]:
            buttons[i].config(state ='normal')
      countdown()
      pauseButton.config(text="Pause")

def clicked(n, j, cnum):
   print(n, j, cnum)
   # button disabled
   if (n == cnum[0]): 
      buttons[j].config(state="disabled")
      cnum[0] += 1
      hint['text'] = cnum[0]
      if (n == 3):
         com['text'] = ""
      if (n == 99):
         com['text'] = "Congratulation! You win!"
         cancel_timer()
         pauseButton.config(state="disabled")

def countdown():
   global time_left
   global job
#   print(cnum[0])
   if time_left == 0:
      com['text'] = "Time's up! Score: "+str(cnum[0])
      com['fg'] = 'red'
      cancel_timer()
      for i in range(100):
         buttons[i].config(state ='disabled')
      pauseButton.config(state="disabled")
   else:  
      time_left -= 1
      tsec = time_left % 60
      if tsec < 10:
         sec = '0' + str(tsec)
      else:
         sec = str(tsec)
      timer.config(text=str(time_left//60) + " : " + sec)
      job = timer.after(1000, countdown)

def cancel_timer():     
# to stop tkinter .after 
   global job
   if job is not None:
      root.after_cancel(job)
      job = None


# The Tk and vars:
root = tk.Tk()
root.title("Clicking Game")
com = tk.Label(root, text="Click Start to begin.", font=('Arial', 12, 'bold'), fg='blue')
cnum = [0]    # have to make cnum mutable, so use list with single element
hint = tk.Label(root, text=cnum[0], font=('Arial', 12, 'bold'), fg='blue', bg='yellow')

global job 
job = None

# The Buttons:
buttons = []
numbers = np.array(100)
global so
so = []
for i in range(100):
   bt = tk.Button(root, text="", height=2, width=2, relief=tk.RAISED, state=tk.DISABLED)
   buttons.append(bt)

# the timer:
timer = tk.Label(root, fg="red", text="5 : 00", font=('Arial', 12, 'bold') )

# the Command buttons:
startButton = tk.Button(root, text="Start", command=startGame)
pauseButton = tk.Button(root, text="Pause", command=pauseGame, state = 'disabled')
quitButton = tk.Button(root, text="Quit", command=quit)


# lay out in grid:
com.grid(row=0, column=0, columns=6, ipady=5, padx=5, pady=5)
#  layout choice: 1 or 2
lc = 1
if lc == 1:     #  layout 1
   num_row = 5
   num_col = 20
else:           #  layout 2
   num_row = 10
   num_col = 10
# buttons:
for i in range(num_row):
  for j in range(num_col):
     buttons[num_col*i+j].grid(row=i+1, column=j, ipadx=4, ipady=4, padx=2, pady=2)
# Timer and hint:
hint.grid(row=0, column=(int)(0.75*num_col), columns=1, ipady=5, padx=5, pady=5)
timer.grid(row=0, column=(int)(0.85*num_col), columns=3, ipady=5, padx=5, pady=5)
# Command buttons:
startButton.grid(column=(int)(0.4*num_col), columns=3, row=num_row+2, padx=5, pady=20, ipadx=5, ipady=5)
pauseButton.grid(column=(int)(0.6*num_col), columns=3, row=num_row+2, padx=5, pady=20, ipadx=5, ipady=5)
quitButton.grid(column=(int)(0.9*num_col), columns=3, row=num_row+2, padx=5, pady=20, ipadx=5, ipady=5)


# the main loop:
root.mainloop()



