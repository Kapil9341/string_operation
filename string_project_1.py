# String methods
lst=input("Enter String :")
print("....String Menu....")
print()
print("1:Capitalize First")
print("2:Make all upercase")
print("3:Make all lowercase")
print("4:Swap case")
print("5:Get length")
print("6:Replace item")
print("7:Count")
print("8:Start with")
print("9:End with")
print("10:Split")
print("11:Find position")
print("12:All alphanumeric")
print("13:All alphabetic")
print("14:All numeric")
print("15:Exit")
def run():
    
    #print("lst=",lst)
   

    s=int(input("Select:"))
    if s==1:
        print(lst.capitalize())
    elif s==2:
        print(lst.upper())
    elif s==3:
        print(lst.lower())
    elif s==4:
        print(lst.swapcase())
    elif s==5:
        print(len(lst))
    elif s==6:
        print(lst)
        s_i=input("Enter string item:")
        c_i=input("Enter change item:")
        print(lst.replace(s_i,c_i))
    elif s==7:
        w=input("Enter word to count:")
        print(lst.count(w))
    elif s==8:
        start_w=input("Enter word or character to check starts with:")
        print(lst.startswith(start_w))
    elif s==9:
        end_w=input("Enter word or character to check ends with:")
        print(lst.endswith(end_w))
    elif s==10:
        print(lst.split())
    elif s==11:
        find_word=input("Enter item to find position ")
        print(lst.find(find_word))
    elif s==12:
        print(lst.isalnum())
    elif s==13:
        print(lst.isalpha())
    elif s==14:
        print(lst.isnumeric())
    elif s==15:
        input("Enter any key")
        exit()

    else:
        print("wrong")
        
while True:
    run()

   
