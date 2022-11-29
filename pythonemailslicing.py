print("----------------------------------------------------------------------EMAIL SLICER------------------------------------------------------------------------------")
print("-----------------------------------------THIS IS A PROGRAM WHERE YOU CAN SEPERATE A EMAIL INTO USERNAME AND DOMAIN NAME-----------------------------------------")
z=1
n = 0
import re
while n<3:
        s = input("Enter your Email: ")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, s)):
                print("Valid Email")
                break
        else:
            print("Invalid Email")
            print("Enter again")
            n+=1
            continue
a = n
h = 0
while a!=3 and h<1:
        print()
        print("__________________________________________________________________________MAIN MENU_____________________________________________________________________________")
        print(">Press 1 to Print Username: ")
        print(">Press 2 to Print Domain name: ")
        print(">Press 3 to Print Both: ")
        print(">Press 0 to Exit: ")
        print()
        h+=1
        while True:
                b = s.find('@')
                a = input("Enter Your Input:  ")
                c = s[b+1:len(s)+1].upper()
                if a=="1":
                        print("User Name: "+s[:b])   
                elif a=="2":
                        print("Domain Name: "+c)
                elif a=="3":
                        print("User Name: "+s[:b],"  Domain Name:"+c)
                elif a=="0":
                        z=0
                        break
                else:
                        print("Input error")
print("------------------------------------------------------------------------------------------THANK YOU-------------------------------------------------------------")

        
