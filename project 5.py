from bdb import Breakpoint

while True:
    actual_username="abbas"
    actual_password="456"
    username=input("enter the user name")
    password=input("enter the password")
    if (username==actual_username) and (password==actual_password):
           print("succesfully loged in")
           break
    else:
           print("invalid credentiols")