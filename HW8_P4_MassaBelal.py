from random import randint

def guessNumber():
    randomNum = randint(0,50)
    print(randomNum)
    count=0
    while True:
        count += 1
        num = int(input("Guess "+str(count)+"?"))
        if num == randomNum:
            print("you are right! I was thinking of"+str(randomNum)+ "!")
            break
        if num < randomNum:
            print(str(num)+ " is too low")
        if num > randomNum:
            print(str(num)+ " is too high")
        if count == 5:
            print("The number was "+str(randomNum))
            break
    return num
print(guessNumber())
    
           
           
        
    
