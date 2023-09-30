# Massa Belal
# CS 100 2021F Section 035
# HW 12, December 9, 2021

#1
def safeOpen(file):
    try:
        return(open(file, "r"))
    except FileNotFoundError:
        return (None)
print(safeOpen("file.txt"))
#2

def safeFloat(x):
    try:
        return float(x)
    except ValueError:
        return 0.0

print(safeFloat('abc'))
#3
def averageSpeed():
    i=0
    while True:
        file = input("Enter file name: ")
        if safeOpen(file)==None:
            if i>=1:
                print("File not found. Yet another human error. Goodbye")
                return
            print("File not found. Please try again.")
            i+=1  
        else:
            content = open(file).read()
            content = content.replace(" ", "\n")
            content = content.split("\n")
            average = 0
            nums = 0
            for number in content:
                if safeFloat(number)>2:
                    nums+=1
                    average+= float(number)
            average=average/nums
            print("average speed is "+ str(average) +" miles per hour.")
            return

averageSpeed()