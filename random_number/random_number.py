import random
 
print ("="*45)
print("let's play a little game!".rjust(33))
print ("\ninstruction: I pick a number in my mind\nyou have to guess that number\n\nTHere are 3 levels:\n1.easy: you have 3 shots (1 to 10)  \n2.medium: you have 5 shots (1 to 100) \n3.hard: you have 10 shots (1 to 1000)\n".rjust(100))
print ("programmed by AIDA HASANZADEH ")
print ("="*45)

def easy():
	computer=random.randint(1,3)
	for i in range (3):
		user=int(input ("\npick a number from 1 to 10: "))
		
		if user<computer:
			print ("Think about a bigger one")
		
		elif user>computer:
			print ("Think about a smaller one")
		
		elif user==computer:
			print ("\ncongrats,you win!")
			break 
			
	else:
		print("\nI'm sorry you lost! my number was",computer)
		
		
def medium():
	computer=random.randint(1,100)
	for i in range (5):
		user=int(input ("\npick a number from 1 to 100: "))
		
		if user<computer:
			print ("Think about a bigger one")
		
		elif user>computer:
			print ("Think about a smaller one")
		
		elif user==computer:
			print ("\ncongrats,you win!")
			break
			
	else:
		print("\nI'm sorry you lost! my number was",computer)
		
		
def hard():
	computer=random.randint(1,1000)
	for i in range (10):
		user=int(input ("\npick a number from 1 to 1000: "))
		
		if user<computer:
			print ("Think about a bigger one")
		
		elif user>computer:
			print ("Think about a smaller one")
		
		elif user==computer:
			print ("\ncongrats,you win!")
			break
			
	else:
		print("\nI'm sorry you lost! my number was",computer)
			

choose=int(input("choose your level\n1.easy 2.medium 3.hard: "))
if choose==1:
	easy()
	
elif choose==2:
		medium()
		
elif choose==3:
		hard()
		
		
	
	