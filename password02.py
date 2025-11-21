import sys
script_name =(sys.argv[0])

if len(sys.argv[0]) ==2:
    password =int(map(sys.argv[0]))
    print("Using command line inputs")
else:
    print("No input given using default values")

#Default values
    password = 7677
    confirm_password = 5767

#Confirming the password
    if password == confirm_password:
        print("Match-Confirm password")
    elif password != confirm_password:
        print("Mismatch,try again")
    else:
        print("Reset password")

#Display result
print("password=",password)
print("confirm password=",confirm_password)