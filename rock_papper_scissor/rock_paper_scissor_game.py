import random 
print ("\t🪨📄✂️Rock Paper Scissor✂️📄🪨\n")
user_total=0
computer_total=0
for i in range (3):
	computer=random.randint(1,3)
	user=int(input ("1.rock 2.paper 3.scissor ,choose: "))
	
	if computer==user:
		print ("user: ", user,"computer",computer)
		print ("equal🤝🏻\n")
		
	elif computer==1 and user==2:
		print ("user: ", user,"computer",computer)
		print ("you win🎉\n")
		user_total+=1
		
	elif computer==1 and user==3:
		print ("user: ", user,"computer",computer)
		print ("you lost❗\n")
		computer_total+=1
		
	elif computer==2 and user==1:
		print ("user: ", user,"computer",computer)
		print ("you lost❗\n")
		computer_total+=1
		
	elif computer==user:
		print ("user: ", user,"computer",computer)
		print ("equal🤝🏻\n")
		
	elif computer==2 and user==3:
		print ("user: ", user,"computer",computer)
		print ("you win🎉\n")
		user_total+=1
		
	elif computer==3 and user==1:
		print ("user: ", user,"computer",computer)
		print ("you win🎉\n")
		user_total+=1
		
	elif computer==3 and user==2:
		print ("user: ", user,"computer",computer)
		print ("you lost❗\n")
		computer_total+=1
		
	elif computer==user:
		print ("user: ", user,"computer",computer)
		print ("equal🤝🏻\n")

if user_total>computer_total:
	print("🎉you win the game🎉") 
	
else:
		print("I'm sorry you lost😔")
		
	