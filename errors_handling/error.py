def add(n1,n2):
    print(n1+ n2)
add(30, 50)    

try:
    number_1 = int(input("Enter Your first Number  "))
    number_2 = int(input("Enter Your 2nd Number  "))
    
except:
   print("Addition Is Complete")
   
finally:
    print("It Works ")
   
add(number_1, number_2)



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

try:
    for i in ['a','b','c']:
        print(i**2)
        
except TypeError:
    print("Type error")
        
finally:
    print("I run after That")
    
