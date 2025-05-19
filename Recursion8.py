
def Display(no):
    if(no >= 1):
        print("*", end=" ")
        no = no - 1
        Display(no)
    
def main():
    no = int(input("Enter the number : "))
    Display(no)
    
if __name__ == "__main__":
    main()