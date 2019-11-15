# A program to create a gift giving list for everyone at a Christmas party
# Written by Cameron Yeomans November 14 2019
# As a fun personal side project
from random import randint

print("Welcome to the secret santa gift giving list maker")
totalPeople = int(input("Please enter the number of participants: "))
giftGiverList =  []
giftRecieverList = []
giftPairs = dict()
oddParty = False
for i in range(0,totalPeople):
	val2Str = str(i + 1)
	guestName = input("Enter guest number "+ val2Str +"'s name: ")
	giftGiverList.append(guestName)
	giftRecieverList.append(guestName)

#used to to make sure that everyone gets a gift
if(len(giftGiverList) % 2 != 0):
	oddParty = True

for i in range(0,totalPeople):
	potential = randint(0,len(giftRecieverList)-1)
	#prevents guest from giving themselves a gift	
	while(giftRecieverList[potential] == giftGiverList[i]):
		potential = randint(0,len(giftRecieverList)-1)
		if(oddParty):
			if(giftRecieverList[potential] in giftPairs):
				if(giftPairs.get(giftRecieverList[potential],'none') == giftGiverList[i]):
					potential = randint(0,len(giftRecieverList)-1)
	giftPairs[giftGiverList[i]] = giftRecieverList[potential]
	giftRecieverList.remove(giftRecieverList[potential])
	
print("\n")	
for i in giftPairs:    
    print(i + " gives to: "+ giftPairs[i])	

