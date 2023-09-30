def enterNewPassword():
    while True:
        userPassword = input("Enter a password between 8 and 15 characters with at least one digit:")
        digits="1234567890"
        lengthState = False
        numState = False
        if len(userPassword) < 8:
            print("Length is not between 8 and 15 characters")
        elif len(userPassword) > 15:
            print("Length is not between 8 and 15 characters")
        if 8<= len(userPassword) <=15:
            lengthState = True
        for digit in digits:
            if digit in userPassword:
                numState=True
            if numState and lengthState:
                return userPassword
        if numState == False:
            print("Does not contain at least 1 digit")
        

print(enterNewPassword())
    
    
