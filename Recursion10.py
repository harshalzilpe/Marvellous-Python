def Add(no):
    sum = 0
    while(no >= 1):
        sum = sum + no
        no = no - 1
    return sum
    
def main():
    no = int(input("Enter the number : "))
    ret = Add(no)
    print(ret)
    
if __name__ == "__main__":
    main()