def main():
    try:
       a = int(input("Hello Sir, Please Enter the Passcode to access my web page:  "))
       print(a)
       return

    except Exception as e:
        e = ("ERROR!!!! Please enter a valid number")
        print (e)
        return
 
    finally:
        print("Thank You for your patience") 
 # fnally is gonna run on any cost, if return has been placed or any other funtion and there is no finally
 # then the above text will not get printed and vice versa   

main()