try:
    a = int(input("Hello Sir, Please Enter the Passcode to access my web page:  "))

except Exception as e:
    e = ("ERROR!!!! Please enter a valid number")
    print (e)

else:
    print("Thank You for your patience You are allowed to access the web page now!") 
    #this is going to run when theres no error and the program is successful