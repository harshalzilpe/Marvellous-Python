import sys

def main():
    print("number of commanline arguments are : ",len(sys.argv))
    
    print("List of commandline arguments are : ")
    
    for value in sys.argv :
        print(value)
    
if __name__ == "__main__":
    main()