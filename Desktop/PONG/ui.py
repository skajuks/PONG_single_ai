import client
from tkinter import *
from tkinter import colorchooser
import pygame
import random, time, math, re
from colormap import rgb2hex
root = Tk()
def start():
    root.quit()


def create_widgets():
    color = colorchooser.askcolor(title="Select color : ")
    p1c = Canvas(TopFrame, width= "10", height='10', bg=color[1])
    p1c.pack(side='left')
    return color
TopFrame = Frame(root)
BottomFrame = Frame(root)
TopFrame.pack() 
BottomFrame.pack()
posIndex= 0
txm = int(round(time.time() * 1000)) / 3  # bigger the divider the slover is radian
lr = math.sin(math.radians(0   + 360 / len(root.size()) * posIndex + txm)) * 127.5 + 127.5
lg = math.sin(math.radians(120 + 360 / len(root.size()) * posIndex + txm)) * 127.5 + 127.5      # draws background color using radians
lb = math.sin(math.radians(240 + 360 / len(root.size()) * posIndex + txm)) * 127.5 + 127.5
posIndex = posIndex + 1

player1col = Button(TopFrame, text="Player 1 color", command = create_widgets, fg = 'red')
player2col = Button(TopFrame, text="Player 2 color", command = start, fg= 'blue')

#player2colbox = Frame(TopFrame, fg=player1col)
#color_result_rgb = ' '.join(str(int(x)) for x in rgb_tuple) 
#print(player1col)
#def colorEncode(color):

color = (str(player1col))
color = color.rsplit(',',1)[0]
color = re.split('()', color)
#return color
print(color)    
player1col.pack(side = "left")
player2col.pack(side = "left")  
root.geometry("300x300")
test = rgb2hex(int(lr),int(lg),int(lb))
root.configure(bg=test) 
root.title("PONG GAME")      
root.mainloop()