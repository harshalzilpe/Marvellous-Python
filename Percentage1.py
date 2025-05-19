

def main():
    print("Enter total marks : ")
    value1 = int(input())
    
    print("Enter Obtained marks : ")
    value2 = int(input())
    
    ans = ((value2 / value1) * 100)
    
    print("Percentage is : ",ans)

if __name__ == "__main__":
    main()