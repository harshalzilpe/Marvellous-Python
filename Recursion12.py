def Factorial(no):
    Fact = 1
    
    while(no >= 1):
        Fact = Fact * no
        no = no - 1
    return Fact
    
def main():
    no = int(input("Enter the number : "))
    ret = Factorial(no)
    print(ret)
    
if __name__ == "__main__":
    main()