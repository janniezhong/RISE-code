# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:21:58 2018

@author: charl
"""

"""
Plays a list of songs. Input a number to choose.
1. Michigan fight song
2. Intro to Sweet Child of Mine
3. Mario Theme Song

Uses notes.py, an add-on library that simplifies buzzer song creation.
Thanks to Justas Sadvecius for the library!

The Finch is a robot for computer science education. Its design is the result
of a four year study at Carnegie Mellon's CREATE lab.

http://www.finchrobot.com
"""

from finchsim import FinchSim
# from finch import Finch
from time import sleep
import notes

#Main function for the music player example program"""

#Initialize the finch    
finch = FinchSim()
#finch = Finch()

quarter = 1.35
sixteen = 0.25
eighth = 1.35/2

finch.wheels(1, 0.2)


#songList = ['A3 B3 D4  ']

finch.buzzer(sixteen, 220) #A3
finch.buzzer(sixteen, 247) #B3
finch.buzzer(eighth, 293)  #D4
finch.sleep(sixteen)
finch.buzzer(sixteen, 220)
finch.buzzer(sixteen, 247)
finch.buzzer(eighth, 293)
finch.sleep(sixteen)
finch.buzzer(0.40, 329)
finch.buzzer(sixteen, 293)
finch.buzzer(sixteen, 247)

finch.led(255,0,0)

finch.buzzer(sixteen, 220)
finch.buzzer(sixteen, 247)
finch.buzzer(eighth, 293)
finch.sleep(sixteen)
finch.buzzer(sixteen, 220)
finch.buzzer(sixteen, 247)
finch.buzzer(eighth, 293)
finch.sleep(sixteen)
finch.buzzer(0.40, 293) #D4
finch.buzzer(sixteen, 329) #E4
finch.buzzer(sixteen, 370) #F4

finch.led(255,128,0)

finch.buzzer(sixteen, 220) #A3
finch.buzzer(sixteen, 247) #B3
finch.buzzer(eighth, 293)  #D4
finch.sleep(sixteen)
finch.buzzer(sixteen, 220)
finch.buzzer(sixteen, 247)
finch.buzzer(eighth, 293)
finch.sleep(sixteen)
finch.buzzer(0.40, 329)
finch.buzzer(sixteen, 293)
finch.buzzer(sixteen, 247)

finch.led(255, 255, 0)

finch.buzzer(sixteen, 220)
finch.buzzer(sixteen, 247)
finch.buzzer(eighth, 293)
finch.sleep(sixteen)
finch.buzzer(sixteen, 220)
finch.buzzer(sixteen, 247)
finch.buzzer(eighth, 293)
finch.sleep(sixteen)
finch.buzzer(0.40, 293) #D4
finch.buzzer(sixteen, 329) #E4
finch.buzzer(sixteen, 370) #B3

finch.led(0, 255, 0)

#Ling Chao
finch.buzzer(0.45, 247) #B3
finch.buzzer(1, 247) #B3
finch.sleep(sixteen)
finch.buzzer(sixteen, 247) #B3
finch.buzzer(sixteen, 247) #B3
finch.buzzer(sixteen, 247) #B3
finch.sleep(sixteen)
finch.buzzer(1, 247) #B3
finch.sleep(sixteen)

finch.led(0, 0, 255)

finch.buzzer(sixteen, 220)
finch.buzzer(sixteen, 220)
finch.sleep(sixteen)
finch.buzzer(sixteen, 220)
finch.sleep(sixteen)
finch.buzzer(0.45, 247)
finch.buzzer(sixteen, 185) 
finch.buzzer(1, 220)
finch.sleep(0.45)

finch.led(102, 0, 102)

finch.buzzer(0.45, 247) #B3
finch.buzzer(1, 247) #B3
finch.sleep(sixteen)
finch.buzzer(sixteen, 247) #B3
finch.buzzer(sixteen, 247) #B3
finch.buzzer(sixteen, 247) #B3
finch.sleep(sixteen)
finch.buzzer(1, 247) #B3
finch.sleep(sixteen)

finch.led(255, 0, 0)

finch.buzzer(sixteen, 220)
finch.buzzer(sixteen, 220)
finch.sleep(sixteen)
finch.buzzer(sixteen, 220)
finch.sleep(sixteen)
finch.buzzer(0.45, 247)
#finch.sleep(sixteen)
finch.buzzer(0.45, 220) 
finch.buzzer(1, 220)

finch.led(255, 128, 0)

#Mingjun

finch.buzzer(0.45, 220) #A3
finch.buzzer(0.45, 277) #C#4
finch.buzzer(sixteen, 277)
finch.buzzer(sixteen, 247) #B3
finch.buzzer(1.2, 247)
finch.sleep(eighth)

finch.led(255, 255, 0)

finch.buzzer(0.20, 247) 
finch.buzzer(0.4, 247) #######************************tempo problem
finch.buzzer(0.4, 293)
finch.buzzer(sixteen, 293)
finch.buzzer(sixteen, 277)
finch.buzzer(1, 277)
finch.sleep(sixteen)

finch.led(0, 255, 0)

#Ling Chaoze
finch.buzzer(sixteen, 220)
finch.buzzer(0.45, 220)
finch.buzzer(0.45, 247)
finch.buzzer(1, 247)
finch.sleep(sixteen)

finch.led(0, 0, 255)

finch.buzzer(sixteen, 247)
finch.buzzer(sixteen, 247)
finch.buzzer(0.45, 247)
finch.buzzer(1, 247)
finch.sleep(sixteen)

finch.led(102, 0, 102)

finch.buzzer(sixteen, 220)
finch.buzzer(0.45, 220)
finch.buzzer(0.45, 220)
finch.buzzer(0.45, 247)
finch.buzzer(sixteen, 293)
finch.buzzer(1, 329)
finch.sleep(eighth)

finch.led(255, 0, 0)

#Lin Yanjun
finch.buzzer(0.45, 370)
finch.buzzer(0.45, 329)
finch.buzzer(0.45, 293)
finch.buzzer(0.45, 220)
finch.buzzer(0.3, 293)
finch.buzzer(0.6, 329)
finch.buzzer(0.45, 293)
finch.buzzer(0.85, 220)

finch.led(255, 128, 0)

finch.buzzer(0.45, 329)
finch.buzzer(0.45, 329)
finch.buzzer(0.55, 329)
finch.buzzer(0.3, 293)
finch.buzzer(1, 329)
finch.sleep(eighth)

finch.sleep(255, 255, 0)

finch.buzzer(0.45, 370)
finch.buzzer(0.45, 329)
finch.buzzer(0.45, 293)
finch.buzzer(0.45, 220)
finch.buzzer(0.3, 293)
finch.buzzer(0.6, 329)
finch.buzzer(0.45, 293)
finch.buzzer(0.85, 220)

finch.led(0, 255, 0)

finch.buzzer(0.45, 329)
finch.buzzer(0.45, 329)
finch.buzzer(0.55, 329)
finch.buzzer(0.3, 293)
finch.buzzer(1, 329)

finch.led(0, 0, 255)

#Chen Linong

finch.buzzer(0.45, 370)
finch.buzzer(0.45, 370)
finch.buzzer(0.45, 392)
finch.buzzer(0.45, 370)
finch.buzzer(0.45, 329)
finch.buzzer(0.25, 293)
finch.buzzer(1, 247)

finch.led(102, 0, 102)

finch.buzzer(0.45, 370)
finch.buzzer(0.45, 370)
finch.buzzer(0.45, 392)
finch.buzzer(0.45, 370)
finch.buzzer(0.45, 329)
finch.buzzer(0.25, 293)
finch.buzzer(1.3, 277)
finch.sleep(sixteen)

finch.led(255, 0, 0)

finch.buzzer(0.45, 329)
finch.buzzer(0.40, 329)
finch.buzzer(0.35, 329)
finch.buzzer(0.55, 293)
finch.buzzer(0.45, 329)
finch.buzzer(0.45, 370)
finch.buzzer(0.45, 277)
finch.buzzer(0.45, 293)

finch.led(255, 128, 0)

finch.buzzer(0.45, 329)
finch.buzzer(0.40, 329)
finch.buzzer(0.35, 329)
finch.buzzer(0.55, 293)
finch.buzzer(0.45, 329)
finch.buzzer(0.45, 370)
finch.buzzer(0.45, 277)
finch.buzzer(0.45, 293)

finch.led(255, 255, 255)

finch.sleep(2)
finch.close()

timeList = [0.07]
#notes.sing(finch, songList[song -1],timeList[song-1])



