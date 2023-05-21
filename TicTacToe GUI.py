from tkinter import *
import random
from tkinter import messagebox
import os
import sys

main= Tk()
main.title("Tic Tac toe")
main.configure(bg='#1a334f')
main.geometry('650x650')
main.resizable(False, False)
counter=0

def BAction(b):
    global counter
    global PlayerLetter
    global ComputerLetter
    global buttons
    global Board
    if b['text'] =='':
        if isWinner()==True:
            return
        b.config(text=PlayerLetter)
        for c,i in enumerate(buttons):
            if i==b:
                Board[c+1]=PlayerLetter
                counter=counter+1
                if isWinner()==True:
                    return
                break
        Computerplay()
    else:
        messagebox.showerror('ERROR','this place is taken by the computer')
        
def Computerplay():
    global buttons
    global ComputerLetter
    global Board
    global counter  
    while(True):
        cmpchoice = random.choice(buttons)
        if cmpchoice['text']=='':
            for c,i in enumerate(buttons):
                if i==cmpchoice:
                    Board[c+1]=ComputerLetter
                    counter=counter+1
            cmpchoice.config(text=ComputerLetter)
            
            if isWinner()==True:
                return
            break
def quitGame():
     main.quit()
def restartGame():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def r1Action():
    l2.place(relx=0.2,rely=0.3)
    r3.place(relx=0.3,rely=0.35)
    r4.place(relx=0.3,rely=0.4)
def r2Action():
    l2.place_forget()
    r3.place_forget()
    r4.place_forget()
    b1.place(relx=0.3,rely=0.5)
def r3Action():
    b1.place(relx=0.3,rely=0.5)

def r4Action():
    b1.place(relx=0.3,rely=0.5)
def startGame():
    global ComputerLetter
    global PlayerLetter
    global buttons
    button1.grid(column=0,row=0,padx=7,pady=7)
    button2.grid(column=1,row=0,padx=7,pady=7)
    button3.grid(column=2,row=0,padx=7,pady=7)

    button4.grid(column=0,row=1,padx=7,pady=7)
    button5.grid(column=1,row=1,padx=7,pady=7)
    button6.grid(column=2,row=1,padx=7,pady=7)

    button7.grid(column=0,row=2,padx=5,pady=5)
    button8.grid(column=1,row=2,padx=5,pady=5)
    button9.grid(column=2,row=2,padx=5,pady=5)

    l1.place_forget()
    r1.place_forget()
    l2.place_forget()
    r2.place_forget()
    r3.place_forget()
    r4.place_forget()
    b1.place_forget()

    b2.place(relx=0.3,rely=0.6)
    b3.place(relx=0.3,rely=0.75)
    if v1.get()==1:
        if v2.get()==1:
            l3.config(text='Player: X',font=('Arial',15))
            ComputerLetter='O'
            PlayerLetter='X'
            l4.config(text='Computer: O',font=('Arial',15))
            l3.place(relx=0.5,rely=0.02)
            l4.place(relx=0.5,rely=0.09)
        else:
            l3.config(text='Player: O',font=('Arial',15))
            ComputerLetter='X'
            PlayerLetter='O'
            l4.config(text='Computer: X',font=('Arial',15))
            l3.place(relx=0.5,rely=0.02)
            l4.place(relx=0.5,rely=0.09)
    else:
          lis=['X','O']
          ComputerLetter = random.choice(lis)  #X
          if ComputerLetter=='X':
              PlayerLetter='O'
          else:
              PlayerLetter='X'
          l3.config(text='Computer selected '+ComputerLetter,font=('Arial',15))
          l3.place(relx=0.5,rely=0.02)
          l4.config(text ='Player is: '+PlayerLetter,font=('Arial',15))
          l4.place(relx=0.5,rely=0.09)
          Computerplay()

PlayerLetter=''
ComputerLetter=''
l1= Label(main,text="Welcome to tic tac toe game with the computer.\nPlease select do you want to play first or second",font=('Arial',15))
l1.place(relx=0.20,rely=0.05)
l2= Label(main,text="Select X or O",font=('Arial',15))
v1=IntVar()
v2=IntVar()
r1=Radiobutton(main,text='First',variable=v1,value=1,font=('Arial',15),command=r1Action)
r1.place(relx = 0.3, rely = 0.17)

r2=Radiobutton(main,text='Second',variable=v1,value=2,font=('Arial',15),command=r2Action)
r2.place(relx = 0.3, rely = 0.22)

r3=Radiobutton(main,text='X',variable=v2,value=1,font=('Arial',15),command=r3Action)
r4=Radiobutton(main,text='O',variable=v2,value=2,font=('Arial',15),command=r4Action)

b1=Button(main,text='Play',height=3,width=30,bd=4,command=startGame)
b2 =Button(main,text='Quit',height=3,width=30,bd=4,command=quitGame)
b3 = Button(main,text="Restart",height=3,width=30,bd=4,command=restartGame)
l3=Label(main,text='')

l4=Label(main,text='')

button1=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button1))
button2=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button2))
button3=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button3))
button4=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button4))
button5=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button5))
button6=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button6))
button7=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button7))
button8=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button8))
button9=Button(main,text='',height=5,width=10,activebackground='black',bd=4,command=lambda:BAction(button9))
buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]

Board = {1:'',2:'',3:'',
         4:'',5:'',6:'',
         7:'',8:'',9:''}

def isWinner():
    winner=False
    if (Board[1]==Board[2]==Board[3]==PlayerLetter):
        winner=True
        a=messagebox.showinfo('we have a winner','**Player has won the game!!**')
        print(a)
        return winner
    elif (Board[1]==Board[2]==Board[3]==ComputerLetter):
        winner=True
        a=messagebox.showinfo('we have a winner','**Computer has won the game!!**')
        print(a)
        return winner
    
    elif (Board[4]==Board[5]==Board[6]==PlayerLetter):
        winner=True
        a=messagebox.showinfo('we have a winner','**Player has won the game!!**')
        print(a)
        return winner
    elif (Board[4]==Board[5]==Board[6]==ComputerLetter):
        winner=True
        a=messagebox.showinfo('we have a winner','**Computer has won the game!!**')
        print(a)
        return winner
    
    elif (Board[7]==Board[8]==Board[9]==PlayerLetter):
        winner=True
        a=messagebox.showinfo('we have a winner','**Player has won the game!!**')
        print(a)
        return winner
    elif (Board[7]==Board[8]==Board[9]==ComputerLetter):
        winner=True
        a=messagebox.showinfo('we have a winner','**Computer has won the game!!**')
        print(a)
        return winner
    
    elif (Board[1]==Board[4]==Board[7]==PlayerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Player has won the game!!**')
            print(a)
            return winner
    elif (Board[1]==Board[4]==Board[7]==ComputerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Computer has won the game!!**')
            print(a)
            return winner
    
    elif (Board[2]==Board[5]==Board[8]==PlayerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Player has won the game!!**')
            print(a)
            return winner
    elif (Board[2]==Board[5]==Board[8]==ComputerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Computer has won the game!!**')
            print(a)
            return winner
    
    elif (Board[3]==Board[6]==Board[9]==PlayerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Player has won the game!!**')
            print(a)
            return winner
    elif (Board[3]==Board[6]==Board[9]==ComputerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Computer has won the game!!**')
            print(a)
            return winner
    
    elif (Board[1]==Board[5]==Board[9]==PlayerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Player has won the game!!**')
            print(a)
            return winner
    elif (Board[1]==Board[5]==Board[9]==ComputerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Computer has won the game!!**')
            print(a)
            return winner
    
    elif (Board[3]==Board[5]==Board[7]==PlayerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Player has won the game!!**')
            print(a)
            return winner
    elif (Board[3]==Board[5]==Board[7]==ComputerLetter):
            winner=True
            a=messagebox.showinfo('we have a winner','**Computer has won the game!!**')
            print(a)
            return winner

    elif counter==9 and winner==False:
                messagebox.showinfo('DRAW!','***No winner, Draw***')
                winner=True
                return winner
main.mainloop()