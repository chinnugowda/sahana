import random#import random command can initiate the program
count=0#to make sure the program is starting
while count<=100:#its the condition
    roll=input("press r to roll a dice")#giving an input
    if roll=='r':#rolling of dice
        r=random.randint(1,6)#giving the range of the dice
        count=count+r#getting the valueof count+random dice value
        print("r is",r)#printing the random dice value
        print("count is",count)#total count value
        input("press any key to exit")#any key can exit the game
        if count==8:
            count=37
            print("you have climbed the ladder to 37")
            print("your count is",count)
        if count==11:
            count=2
            print("you have been biten by a snake, go to 2")
            print("your count is",count)
        if count==13:
            scount=34
            print("yov have climbed the ladder to 34")
            print("yourcount is",count)
        if count==25:
            count=4
            print("you have been bitten by a snake, go to 4")
            print("your count is",count)
        if count==38:
            count=9
            print("you have been bitten by a snake, go to 9")
            print("yourcount is",count)
        if count==40:
            count=68
            print("you have climbed the ladder to 68")
            print("yourcount is",count)
        if count==52:
            count=81
            print("you have climbed the ladder to 81")
            print("yourcount is",count)
        if count==65:
            count=46
            print("you have been bitten by a snake, go to 46")
            print("yourcount is",count)
        if count==76:
            count=97
            print("you have climbed the ladder to 97")
            print("yourcount is",count)
        if count==89:
            count=70
            print("you have been bitten by a snake, go to 70")
            print("yourcount is",count)
        if count==93:
            count=64
            print("you have been bitten by a snake, go to 64")
            print("yourcount is",count)
        if count>99:
            count=100
            print("you won, CONGRATULATIONS")
            print("yourcount is",count)
	if count>100:
	    count=count-r
	    print ("your count is exceeding 100, try again")
	if count==100:
	    print("u won")
	    break
	
   
