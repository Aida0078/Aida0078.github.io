print ("""✖️➗ CALCULATOR ➕➖\n""".rjust(23))

import math
import decimal

def Sum ():
	
	while True:
		a=(input("enter your first number: "))
		try:
			a=decimal.Decimal(a)
			try:
				b=input("enter your second number: ")
				b=decimal.Decimal(b)
				c=a+b
				return c
			except:
				print("invalid input!")
		except:
				print("invalid input!")
				
				
def subtraction ():
	
	while True:
		a=(input("enter your first number: "))
		try:
			a=decimal.Decimal(a)
			try:
				b=input("enter your second number: ")
				b=decimal.Decimal(b)
				d=a-b
				return d
			except:
				print("invalid input!")	
		except:
				print("invalid input!")

	
def multiplication ():
	
	while True:
		a=(input("enter your first number: "))
		try:
			a=decimal.Decimal(a)
			try:
				b=input("enter your second number: ")
				b=decimal.Decimal(b)
				e=a*b
				return e
			except:
				print("invalid input!")
		except:
				print("invalid input!")

	
def division ():
	
	while True:
		a=(input("enter your first number: "))
		try:
			a=decimal.Decimal(a)
			try:
				b=input("enter your second number: ")
				b=decimal.Decimal(b)
				f=a/b
				return f
			except:
				print("invalid input!")
		except:
				print("invalid input!")
	
	
def power ():
	
	while True:
		a=(input("enter your first number: "))
		try:
			a=decimal.Decimal(a)
			try:
				b=input("enter your second number: ")
				b=decimal.Decimal(b)
				g=a**b
				return g
			except:
				print("invalid input!")
		except:
				print("invalid input!")
	
	
def sinus ():
	
	while True:
		a=input ("enter your number: ")
		try:
			a=decimal.Decimal(a)
			h=math.sin(math.radians(a))
			return h
		except:
			print("invalid input!")
			
	
def Factorial ():
	
	while True:
		a=input ("enter your number: ")
		try:
			a=int(a)
			i=math.factorial(a)
			return i
		except:
			print("invalid input!")
			
	
def square ():
	
	while True:
		a=input ("enter your number: ")
		try:
			a=decimal.Decimal(a)
			j=math.sqrt(a)
			return j
		except:
			print("invalid input!")
	
	
while True:
	print ("\n\"Main menu\"".rjust(10))
	print("what operator do you want to use?\n1.sum\n2.subtraction\n3.multiplication\n4.division\n5.power\n6.sinus\n7.factoial\n8.square")
	choice=int(input ('choose: '))
	
	if choice==1:
		print ("\nsum")
		print ("your answer is: ",Sum())
	elif choice==2:
		print ("\nsubtraction ")
		print ("your answer is: ",subtraction())
	elif choice==3:
		print("\nmultiplication")
		print ("your answer is: ",multiplication())
	elif choice==4:
		print("\ndivision")
		print("your answer is: ",division())
	elif choice==5:
		print("\npower")
		print("your answer is: ",power())
	elif choice==6:
		print("\nsinus")
		print ("your answer is: ",sinus())
	elif choice==7:
		print("\nfactorial")
		print ("your answer is: ",Factorial())
	elif choice==8:
		print("\nsquare")
		print ("your answer is: ",square())
		
	else:
		print("\ninvalid input!")
	
		
	question=input ("\nDo you want to continue? (yes/no): ")
	if question=='yes':
		continue
	elif question=='no':
		print ('Have a good day 🤍')
		break 
	else:
		print(" invalid input!")