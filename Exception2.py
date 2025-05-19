
def main():
    no1 = int(input("Enter the first number : "))
    no2 = int(input("Enter the second number : "))
    
    Ans = 0
    
    try:
        Ans = no1 / no2
        
    except ZeroDivisionError:
        print("Exception ocurred due to second input.")
    
    print("Division is",Ans)
    
        
if __name__ == "__main__":
    main()