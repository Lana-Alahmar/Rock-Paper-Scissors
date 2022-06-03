# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 22:50:36 2022

@author: Classic
"""
import random
while True:
 choices= ["rock", "paper", "scissors"]
 computer= random.choice(choices)
 player= None
 while player not in choices :
      player=input("enter rock, scissors or paper: ").lower()

 if player ==computer:
    print ("player (" , player, ") :", "CPU (" , computer, ")")
    print("Tie")
   
 elif player == "rock":
    if computer == "paper":
        print ("player (" , player, ") :", "CPU (" , computer, ")")
        print("you Lose!")
    if computer == "scissors":
        print ("player (" , player, ") :", "CPU (" , computer, ")")
        print ("you Win!")
 elif player == "paper":
    if computer == "rock":
        print ("player (" , player, ") :", "CPU (" , computer, ")")
        print("you Win!")
    if computer == "scissor":
        print ("player (" , player, ") :", "CPU (" , computer, ")")
        print ("you Lose!")
 elif player == "scissor":
    if computer == "paper":
        print ("player (" , player, ") :", "CPU (" , computer, ")")
        print("you Win!")
    if computer == "rock":
        print ("player (" , player, ") :", "CPU (" , computer, ")")
        print ("you Lose!")
        
    
    
 playagain= input("do you want to play againn? yes/No ").lower()
 if playagain!= "yes":
       break
print("see you later")
    

