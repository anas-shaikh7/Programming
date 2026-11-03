def http_status(status):
     match status:
          case 200:
             return "OK" 
          case 404:
             return "Server not found"
          case 500:
              return "Internal Server Error"
          case _: # indicates any other number
             return "Unknown status" 



 # Usage
print(http_status(404)) 