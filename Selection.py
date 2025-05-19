
def main():
    print("Enter your age : ")
    Age = int(input())
    
    if(Age < 18):
        print("You are not eligible for voting")
    else:
        print("You are eligible for voting")

if __name__ == "__main__":
    main()