def Display(no):
    while(no >= 1):
        print("*", end=" ")
        no = no - 1
    print()
    
def main():
    no = int(input("Enter the number : "))
    Display(no)
    
if __name__ == "__main__":
    main()