print("Use greet function")

def greet(name):
    print(f"Good moring , {name}")

    if __name__ == "main":
        n = input("Enter a name : ") 
        greet(n)

print("Press q to quit")

while(True):
    a = input("Enter a number: ")
    if 'q' == a :
        break
    try:
        print("Trying.......")
        a = int(a)
        c = 1/a
        print(c)
        if a > 6:
            print("You have a no greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")
    except ZeroDivisionError as e:
        print(f"Dont divide by 0") 
    except :
        raise ValueError("Enter correct value ") 

print("Thanks for playing this game")