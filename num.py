import pyttsx3
import msvcrt
import time
import cprint
import colored
from termcolor import colored ,cprint
engine = pyttsx3.init()
engine.setProperty('rate',100)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("what you want to do")
engine.runAndWait()
engine.say("option one adding the two numbers option two for multiplying the two numbers option three for division of two numbers option four for subtraction of two numbers option five for percentage option six for adding two words option seven for atm transaction")
engine.runAndWait()
engine.say("Enter the option")
engine.runAndWait()
x=eval(input("Enter the option:"))
if x==1:
  engine.say("enter the first number")
  engine.runAndWait()
  a=eval(input("enter the first number:"))
  engine.say("you entered the first value")
  engine.runAndWait()
  engine.say(a)
  engine.runAndWait()
  engine.say("enter the second number")
  engine.runAndWait()
  b=eval(input("enter the second number:"))
  engine.setProperty('rate',100)
  engine.say("you entered the second value")
  engine.runAndWait()
  engine.say(b)
  engine.runAndWait()
  c=a+b
  engine.say("sum is under process")
  engine.runAndWait()
  engine.say("the sum of both your values are ")
  engine.runAndWait()
  engine.say(c)
  engine.runAndWait()
  print("The sum of both your values are:")
  print(c)
if x==2:
  engine.say("enter the first number")
  engine.runAndWait()
  a=eval(input("enter the first number:"))
  engine.say("you entered the first value")
  engine.runAndWait()
  engine.say(a)
  engine.runAndWait()
  engine.say("enter the second number")
  engine.runAndWait()
  b=eval(input("enter the second number:"))
  engine.setProperty('rate',100)
  engine.say("you entered the second value")
  engine.runAndWait()
  engine.say(b)
  engine.runAndWait()
  c=a*b
  engine.say("multiplication is under process")
  engine.runAndWait()
  engine.say("the multiplication of both your values are ")
  engine.runAndWait()
  engine.say(c)
  engine.runAndWait()
  print("The multiplication of both your values are:")
  print(c)
if x==3:
  engine.say("enter the dividend number")
  engine.runAndWait()
  a=eval(input("enter the dividend number:"))
  engine.say("you entered the dividend value")
  engine.runAndWait()
  engine.say(a)
  engine.runAndWait()
  engine.say("enter the divisor number")
  engine.runAndWait()
  b=eval(input("enter the divisor number:"))
  engine.setProperty('rate',100)
  engine.say("you entered the divisor value")
  engine.runAndWait()
  engine.say(b)
  engine.runAndWait()
  c=a//b
  d=a%b
  e=a/b
  engine.say("division is under process")
  engine.runAndWait()
  engine.say("the quotient of both your values are ")
  engine.runAndWait()
  engine.say(c)
  engine.runAndWait()
  print("The quotient of both your values are:")
  print(c)
  engine.say("the remainder of both your values are ")
  engine.runAndWait()
  engine.say(d)
  engine.runAndWait()
  print("The remainder of both your values are:")
  print(d)
  engine.say("the exact quotient of both your values are ")
  engine.runAndWait()
  engine.say(e)
  engine.runAndWait()
  print("The Exact quotient of both your values are:")
  print(e)
if x==4:
  engine.say("enter the first number")
  engine.runAndWait()
  a=eval(input("enter the first number:"))
  engine.say("you entered the first value")
  engine.runAndWait()
  engine.say(a)
  engine.runAndWait()
  engine.say("enter the second number")
  engine.runAndWait()
  b=eval(input("enter the second word:"))
  engine.setProperty('rate',100)
  engine.say("you entered the second value")
  engine.runAndWait()
  engine.say(b)
  engine.runAndWait()
  if a>b:
    c=a-b
  else:
    c=b-a
  engine.say("subtraction is under process")
  engine.runAndWait()
  engine.say("the subtraction of both your values are ")
  engine.runAndWait()
  engine.say(c)
  engine.runAndWait()
  print("The subtraction of both your values are:")
  print(c)
if x==5:
  engine.say("enter the number whom you want percentage")
  engine.runAndWait()
  a=eval(input("enter the number whom you want percentage:"))
  engine.say("you entered the number whom you want percentage is")
  engine.runAndWait()
  engine.say(a)
  engine.runAndWait()
  engine.say("enter the number how much you want percentage")
  engine.runAndWait()
  b=eval(input("enter the number how much you want percentage"))
  engine.setProperty('rate',100)
  engine.say("you entered the second valuenumber how much you want percentage is")
  engine.runAndWait()
  engine.say(b)
  engine.runAndWait()
  c=a*b
  d=c//100
  engine.say("percentage calculation is under process")
  engine.runAndWait()
  engine.say("the percentage of both your values are ")
  engine.runAndWait()
  engine.say(d)
  engine.runAndWait()
  print("The percentage of both your values are:")
  print(d)
if x==6:
  engine.say("enter the first word")
  engine.runAndWait()
  a=input("enter the first word:")
  engine.say("you entered the first word")
  engine.runAndWait()
  engine.say(a)
  engine.runAndWait()
  engine.say("enter the second word")
  engine.runAndWait()
  b=input("enter the second word:")
  engine.setProperty('rate',100)
  engine.say("you entered the second word")
  engine.runAndWait()
  engine.say(b)
  engine.runAndWait()
  c=a+b
  engine.say("sum is under process")
  engine.runAndWait()
  engine.say("the sum of both your words are ")
  engine.runAndWait()
  engine.say(c)
  engine.runAndWait()
  print("The sum of both your words are:")
  print(c)
if x==7:
  engine.say("kindly insert your card")
  engine.runAndWait()
  engine.say("your card is successfully inserted")
  engine.runAndWait()
  print("enter your card pin number:")
  a=msvcrt.getch()
  print("*",end='')
  b=msvcrt.getch()
  print("*",end='')
  c=msvcrt.getch()
  print("*",end='')
  d=msvcrt.getch()
  print("*")
  engine.say("you entered the pin")
  engine.runAndWait()
  engine.say(a)
  engine.runAndWait()
  engine.say(b)
  engine.runAndWait()
  engine.say(c)
  engine.runAndWait()
  engine.say(d)
  engine.runAndWait()
  engine.say("enter the amount you want to transact")
  engine.runAndWait()
  e=eval(input("enter the amount you want to transact:"))
  engine.setProperty('rate',100)
  engine.say("you entered the amount to transact is")
  engine.runAndWait()
  engine.say(e)
  engine.runAndWait()
  print("you entered the amount to transact is:",e)
  cprint("your transaction is under process..please wait!!!!!",'yellow',attrs=['blink'])
  print("take the amount {} with you".format(e))
  cprint("Thank you for using the ATM service",'blue',attrs=['blink'])