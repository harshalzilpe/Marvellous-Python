no = 11

def fun():
    global no
    print("Inside fun")
    x = 21
    print("Value of x is",x)
    no = no + 1
    print("Value of no is",no)
    
def main():
    print("Value of no before fun is ",no)
    fun()
    print("Value of no after fun is ",no)
    
if __name__ == "__main__":
    main()