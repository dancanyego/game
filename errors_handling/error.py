def add(n1,n2):
    print(n1+ n2)
add(30, 50)    

number_1 = int(input("Enter Your first Number  "))
number_2 = int(input("Enter Your 2nd Number  "))

add(number_1, number_2)


try:
    pass
except:
    pass


try:
    f = open('testfile','w')
    f.write("This is a test file")
except TypeError:
    print("There Waas a type error")
    
except OSError:
    print("OS Error was found")
finally:
    print("I Always Run nigga")
    
    
def ask_for_int():
    while True:
        try:
            result = int(input("PLease Provide your number "))
            
        except:
            print("Whoopsie not a number!!")
            continue
        else:
            print("Finnaly nigga")
            break
            
        finally:
            print("End of Block ")
        
ask_for_int()
    