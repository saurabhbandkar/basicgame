# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:15:01 2020

@author: 20304834
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
def startgame():
    global canvas
    x=startclick()
    if x==1:
        time.sleep(5)
    messagebox.showinfo('ANSWER','NUMBER OF RED BALLS= '+str(redcount)+
                        '\nNUMBER OF GREEN BALLS= '+ str(greencount))

def startclick():
    global i
    global canvas
    global redcount
    global greencount
    for i in range (1,26):
        m=random.randint(0,10)
        if m==0 or m==5 or m==7 or m==9:
            redcount+=1
        elif m==1 or m==6 or m==8:
            greencount+=1
        try:
            a=random.randint(50,250)
            b=random.randint(50,300)
            canvas.create_oval(a,b,a+50,b+50, outline='white',fill=colours[m], width=2)
            canvas.update()
        except:
            print()    
    return 1


colours=['red','green','blue','cyan','black','red','green','red','green','red']
global i
i=0
global redcount
redcount=0
global greencount
greencount=0
global canvas

root=Tk()
root.title('COUNT THE COLORS')
root.geometry('800x700+20+20')
canvas=Canvas(width=500, height=500, bg='#87ceeb')
canvas.place(x=20,y=20)
w=Label(root,bg='black', fg='yellow',text='CAN YOU COUNT THE NUMBER OF RED AND GREEN COLORED BALLS')
w.place(x=20,y=500)
y=Label(root,bg='white', fg='blue',text='YOU HAVE 10 SECONDS TO ANSWER...PRESS THE START BUTTON TO PLAY')
y.place(x=20,y=550)
b=Button(root,text='START',bg='#e79700',width=20, height=1,
         font=('Open Sans', 13, 'bold'),fg='white',command=startgame)
b.place(x=20,y=600)

root.mainloop()