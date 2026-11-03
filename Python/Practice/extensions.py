# file_name = input("File name: ").strip().lower()
# match file_name:
#     case x if ".gif" in file_name:
#         print("image/gif")
#     case x if ".jpg" in file_name:
#         print("image/jpeg")
#     case x if ".jpeg" in file_name:
#         print("image/jpeg")
#     case x if ".png" in file_name:
#         print("image/png")
#     case x if ".pdf" in file_name:
#         print("application/pdf")
#     case x if ".txt" in file_name:
#         print("text/plain")
#     case x if ".zip" in file_name:
#         print("application/zip")
#     case _:
#         print("application/octet-stream")


file_name = input("File name: ").strip().lower()
if ".gif" in file_name:
    print("image/gif")
elif file_name.endswith(("jpg", "jpeg")):
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name:
     print("application/pdf")
elif ".txt" in file_name:
    print("text/plain")
elif ".zip" in file_name:
    print("application/zip")
else:
    print("application/octet-stream")



