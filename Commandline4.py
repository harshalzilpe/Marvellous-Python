import sys

def main():
    print("number of commanline arguments are : ",len(sys.argv))
    
    print("List of commandline arguments are : ")
    for i in range(1, len(sys.argv)) :
        print(sys.argv[i])
    
if __name__ == "__main__":
    main()