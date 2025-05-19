def Display(no):
    for i in range(0,no):
        print("*", end=" ")
    print()
    
def main():
    no = int(input("Enter the number : "))
    Display(no)
    
if __name__ == "__main__":
    main()