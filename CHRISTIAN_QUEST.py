import PySimpleGUI as sg
import numpy as np
from PIL import Image
import pylab as plt
from matplotlib.pyplot import imread
#-------------------------------------------
answer_yes = ["yes", "y", "Yes", "Y", "YES"]
answer_no = ["no", "n", "No", "N", "NO"]
print("CHRISTIAN's QUEST !!! ")
print(" ######## ###  ###  #####    #### #####  ######### ###  ###      ##      ##")
print(" ##       ###  ###  ##  ##    ##  ##        ###    ##   ## #     ####    ##")
print(" ##       ########  ## ##     ##    ##      ###    ##   ##  #    ##  ##  ##")
print(" ##       ###  ###  ######    ##     ##     ###    ##   #######  ##   ## ##")
print(" ######## ###  ###  ##   ##  ###  #####     ###   ###   ##    ## ##    ####")
print("--------------------------------------------------------------------------")
print(" ########  ##   ##   #####   ####  ###########")
print(" #      #  ##   ##   #      ##         ##     ")
print(" #   #  #  ##   ##   ####    ##        ##     ")
print(" #    # #  #######   #        ##       ##     ")
print(" ########   #####    #####  ####       ##     ")
print("        #    ")
print("--------------------------------------------------------------------------")
print('choose your quest: ')
print('-------------------')
print('| 1. Moon Base    |')
print('| 2. BLANK        |')
print('-------------------')
i=Image.open('moonbase.jpeg')
a1=input(">>")
if a1 =='1' or 'Moon Base':
    print(" you're now on the moon, it is spooky and quiet"+'\n'+
    " oh look, an owl, on the moon. ")
    i.show()
    print(" behold the moonbase! ! !!")
    input("continue?"+'\n'+ 'press any button to continue')
print(" a stranger approaches")
i=Image.open('goblin1.jpeg')
i.show()
print("----------------")
print("EYEYYE"+'\n'+
'who goes there???'+'\n'+
'----------------')
a2=input("do you respond with your name?"+'\n'+'>>')
if a2 in answer_yes:
    name=input("Tell the goblin your name: ")
    print("----------------"+"\n"+"AH,"+ name + " is such a stupid name."+'\n'+
    "you fucking suck, fuck youuuuuuuUu!"+'\n'+
    '----------------')
elif a2 in answer_no:
    print(" You won't tell me your name. YOu are a fucking"+'\n'+
    "!!!!CUCK!!!!")
else:
    print("that's not a yes or no answer."*100)
