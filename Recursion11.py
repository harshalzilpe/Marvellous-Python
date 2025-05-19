sum = 0
def Add(no):
    global sum
    if(no >= 1):
        sum = sum + no
        no = no - 1
        Add(no)
    return sum
    
def main():
    no = int(input("Enter the number : "))
    ret = Add(no)
    print(ret)
    
if __name__ == "__main__":
    main()