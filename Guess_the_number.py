from tkinter import * 
import tkinter as tk
import random
import math

class number:
     num_range = 100
     secret_num = 0
     guesses_left = 0
     def __init__(self,root):
        self.root=root      
        self.root.title("GUESS THE NUMBER")
        self.root.geometry("500x420+300+50")
        self.root.resizable(False,False)
        self.root.config(bg='white')

        title=Label(self.root,text='GUESS THE NUMBER',font=("algerian",15),bg="#262626",fg='white').pack(side=TOP,fill=X)

        lbl_url=Label(self.root,text='Select The Range For Starting New Game:',font=("times new roman",15),bg='white').place(x=10,y=50)


        btn_range1=Button(self.root,text='0 to 100',command=self.range100,font=('times new roman',13),bg='red',fg='white').place(x=30,y=80,width=200,height=40)
        btn_range2=Button(self.root,text='0 to 1000',command=self.range1000,font=('times new roman',13),bg='blue',fg='white').place(x=260,y=80,width=200,height=40)

        lbl_number=Label(self.root,text='Enter The Number:',font=("times new roman",15),bg='white').place(x=10,y=130)
        
        self.var_number=StringVar()
        txt_number=Entry(self.root,textvariable=self.var_number,font=("times new roman",13),bg="#d9fcff").place(x=120,y=160,width=340,height=30)

        btn_check=Button(self.root,text='Check',command=self.check,font=('times new roman',13),bg='green',fg='white').place(x=60,y=200,width=150,height=40)
        btn_clear=Button(self.root,text='Clear',command=self.clear,font=('times new roman',13),bg='grey',fg='white').place(x=300,y=200,width=150,height=40)

        self.lbl_guess=Label(self.root,text='',font=("times new roman",15),bg='white')
        self.lbl_guess.place(x=50,y=260)

     def switchbutton():
       if (btn_check['state'] == tk.NORMAL):
        btn_check['state'] = tk.DISABLED
       else:
        btn_check['state'] = tk.NORMAL

     def range100(self):
        self.num_range = 100
        self.guesses_left = 7
        self.secret_num = random.randrange(0, self.num_range)

     def range1000(self):
        self.num_range = 1000
        self.guesses_left = 10
        self.secret_num = random.randrange(0, self.num_range)

     def check(self):
         number=int(self.var_number.get())
         if self.guesses_left<=0:
             self.lbl_guess.config(text=f'Start New Game',fg='red',font=("times new roman",20))
         elif number==self.secret_num:
            self.lbl_guess.config(text=f'You Guessed The Correct Number',fg='green',font=("times new roman",18))
         elif number<self.secret_num:
             self.lbl_guess.config(text=f'You Guessed The Number Less Than Secret Number')
             self.guesses_left=self.guesses_left-1
         elif number>self.secret_num:
             self.lbl_guess.config(text=f'You Guessed The Number Greater Than Secret Number')
             self.guesses_left=self.guesses_left-1

     def clear(self):
         self.var_number.set('')
         self.secret_num=0
         self.guesses_left=0
        










root=Tk()
obj=number(root)
root.mainloop()