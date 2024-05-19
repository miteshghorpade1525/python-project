#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibbonacci():
    print ('welocome to the fibbonacci no.')
    num=int(input ('Enter number here: '))
    a=0
    b=1
    for i in range (num):
        print (a)
        c=a+b
        a=b
        b=c

def addition():
    i=1
    while i<=5:
        print('mitesh')
        i=i+1




def password():
    num=int(input("Enter no of chs of password: "))
    if num>=8 and num<15:
        password=" "
        if num>=8 and num<15:
            for i in range(num):
                import random 
                password=password+(random.choice('abcdefghijklmnopqrstuvwxyz123456789'))
        print("Your genrated password is : ",password)
    else:
        print("Enter valid no.")

def gk():
    print ("welcome to gk quiz")
    user_name=input("Enter your name here")
    print("hello",user_name.title())
    score=0
    user_quest_1=input("who is prime minister of india : ")
    if user_quest_1.lower()==("narendra modi"):
        print("Yes you are right")
    else:
        print("Your ans is wrong")


def timer():
    from countdown import countdown
    user_min=int(input("Enter your min:  "))
    user_sec=int(input("enter your seec: "))
    countdown(mins=user_min,secs=user_sec)



def welcome_bot():
    #NetTech Welcome Bot

    print('Welcome to netTech classes!')
    User_Name=input('Enter your Name here:')
    print('hello',User_Name)
    Phone_Number=input('Enter your Phone numbere here:')
    print('Thank you! Phone Number:',Phone_Number)
    Email_id=input('Enter your Email_id:')
    print('Thank you! Email_id:',Email_id)
    Course=input('Enter course Name:')
    print('Thank you! Course Name:',Course)
    Location=input('Enter Location Name:')
    print('Thank you! Location:',Location)

def dice_game():
    print("welcome to the dice game")
    user_input=int(input("please choose the no between 1 to 6  "))
    print("you choose",user_choice)
    dice=(random.chice('123456'))
    print("Dice result", dice )
    if user_input==dice:
        print("you win")
    else:
        print("you win")
    print('*'*30)  

def gk_quiz():
    print('welcome to GK Quiz!')
    score=0

    user_ans_1=int(input('what is the jersy number of Rohit sharma='))
    if user_ans_1==45:
        print('Yes! You are correct!')
        score=score+10
    else:
        print('sorry! You are incorrect!')
        score=score-10
    print('Your Final Score is',score)

    user_ans_2=int(input('what is the jersy number of virat kholi='))
    if user_ans_2==18:
        print('Yes! You are correct!')
        score=score+20
    else:
        print('sorry! You are incorrect!')
        score=score-15
    print('Your Final Score is',score)
    
    
    

def biker_hub():
    print ("welcome to the  BIKERHUB ")
    print("hello sir,Madam")
    user_choice=input(" what kind of Two wheeler you want")
    if user_choice=='scooty':
        print ("ok fine!, we have multiple scoty" )
        print ("like activa 6G, Dio, Access 125, Jupitor",)
        budget_segment=int(input("Enter your budget"))  
        if budget_segment>=110000:
            print("Go fo the Activa 6G")
        elif budget_segment>=100000:
            print("Go for the Dio")
        elif budget>=90000:
            print("go for the Jupitor")

        else:
            print('no opt avbl')
    elif user_choice=='bike':
        print ("ok fine!, we have multiple bike under 150 CC" )
        print ("like Shine,Hornet,Unicorn,pulsar")
        budget_segment=int(input("Enter your budget"))  
        if budget_segment>=130000:
            print("Go fo the Hornet")
        elif budget_segment>110000:
            print("Go for the shine")
        elif budget_segment>100000:
            print("Go for the shine")
        else:
            print("sorry! you Go for the scooty ")


    else:
        print('no opt avbl')
    print("Thank you! visit again")





#import library
import tkinter as tk

#create window
window=tk.Tk()

#window title
window.title('python project')


#window size
window.geometry('600x500')


#label
tk.Label(window,text="PYTHON PROJECT",font=("Helvetica",20)).place(x=190,y=30)



#button
tk.Button(window,text='biker hub',width=20, height=3,command=biker_hub).place(x=30,y=120)
tk.Button(window,text='gk quiz',width=20, height=3,command=gk_quiz).place(x=225,y=120)
tk.Button(window,text='dice game',width=20, height=3,command=dice_game).place(x=420,y=120)

tk.Button(window,text='welcome bot',width=20, height=3,command=welcome_bot).place(x=30,y=240)
tk.Button(window,text='timer',width=20, height=3,command=timer).place(x=225,y=240)
tk.Button(window,text='fibbonacci',width=20, height=3,command=fibbonacci).place(x=420,y=240)

tk.Button(window,text='addition',width=20, height=3,command=addition).place(x=30,y=360)
tk.Button(window,text='password',width=20, height=3,command=password).place(x=225,y=360)
tk.Button(window,text='gk',width=20, height=3,command=gk).place(x=420,y=360)
#show window
window.mainloop()



# In[ ]:





# In[ ]:




