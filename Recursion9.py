
def Add(no):
    sum = 0
    for i in range(1, no+1):
        sum = sum + i
    return sum
    
def main():
    no = int(input("Enter the number : "))
    ret = Add(no)
    print(ret)
    
if __name__ == "__main__":
    main()