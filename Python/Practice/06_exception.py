try:
    a = int(input("Hello Sir, Please Enter the Passcode to access my web page:  "))
except ValueError as v:
    print(v)
    print("Please Try Again!!")
except Exception as e:
    e = ("ERROR!!!! Please enter a valid number")
    print (e)

print("Thank you for your patience")