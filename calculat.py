def menu():
    print("Welcome :")
    print("1--> Addition")
    print("2--> Subtraction")
    print("3--> Multiplication")
    print("4--> Division")

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Error syntax!"
    else:
        return a / b
    

def Calculat():
    rep = "YES"
    while rep == "YES":
        menu()
        choix = input("Enter operation ::::: ")
        if choix == '5':
            print("Error syntax! Enter the correct choice!")
            break

        if choix in ['1', '2', '3', '4']:
            try:
                x = int(input("Enter the number a : ")) 
                y = int(input("Enter the number b : "))
            except ValueError:
                print("Enter the whole number")
                continue 
        
        if choix == '1':
           print("the result addition is : ",addition(x,y))
        elif choix == '2':
           print("the result Subtraction is : ", subtraction(x,y))
        elif choix == '3':
           print("the result Multiplication is : ", multiplication(x,y))
        elif choix == '4':
           print("Division: ", division(x,y))
        else:
           print("Invalid enter choice!")  

        rep = input("Do you want content YES or NO:: ")

Calculat()
    
