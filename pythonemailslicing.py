
s = input("Enter Your Email: ")
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
if(re.fullmatch(regex, s)):
        print("Valid Email")
else:
    print("Invalid Email")
while True:
        b = s.find('@')
        a = input("For domain name press 1,for username press 2,press 3 to print both and to cancel press 0: ")
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
        
