try: 
    num= int(input("Enter the number: "))
    print(10/num)
    
except ZeroDivisionError:
    print("Cannot divide by ZERO")
    
except ValueError:
    print("Invalid Input")
    
finally:
    print("Execution completed")