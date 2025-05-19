
def main():
    Ans = 0
    
    try:
        no1 = int(input("Enter the first number : "))
        no2 = int(input("Enter the second number : "))
        
        Ans = no1 / no2
        
    except ZeroDivisionError as zobj:
        print("Exception ocurred due to second input : ",zobj)
        
    except ValueError as vobj:
        print("Invalid data type of input : ",vobj)
        
    print("Division is",Ans)
    
        
if __name__ == "__main__":
    main()