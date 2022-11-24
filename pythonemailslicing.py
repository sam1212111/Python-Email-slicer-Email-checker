
s = input("Enter Your Email: ")
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
if(re.fullmatch(regex, s)):
        print("Valid Email")
else:
    print("Invalid Email")
print(">Press 1 to Print Username: ")
print(">Press 2 to Print Domain name: ")
print(">Press 3 to Print Both: ")
print(">Press 0 to Exit: ")      
while True:
        b = s.find('@')
        
        a = input("Enter Your Input:  ")
        c = s[b+1:len(s)+1].upper()


        if a=="1":
                print("User Name:"+c)   
        elif a=="2":
                print("Domain Name:"+s[:b])
        elif a=="3":
                print("User Name:"+c,"  Domain Name:"+s[:b])
        elif a=="0":
                break
        else:
                print("Input error")
        
