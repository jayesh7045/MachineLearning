class Error(Exception):
    pass
class dobException(Exception):
    pass

try:
    dob = int(input("Enter your dob here\n"))
    if (dob <= 20):
        raise dobException
    else:
        print("You can apply for licensing")
except dobException:
    print("Please try again after some Years")
    