stringtemp = "A man a plan a canal panama";
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
    
def EffPalin(stringtemp):
    stringtemp = stringtemp.lower().replace(" ", "");
    return stringtemp == stringtemp[::-1]
if EffPalin(stringtemp):
    print("Palindrome Yes");
else:
    print("No")