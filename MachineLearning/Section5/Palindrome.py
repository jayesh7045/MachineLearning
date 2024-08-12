stringtemp = "EAAEA";
def findPalindrom(stringtemp): 
    i = 0;
    j = len(stringtemp)-1;
    while i < j:
        if(stringtemp[i] != stringtemp[j]):
            return False
        i+=1;
        j-=1;
    return True;

if findPalindrom(stringtemp):
    print("Palindrome");
else:
    print("NA")