CheckEven = lambda No : No % 2 == 0
Increase = lambda No : No + 1
Sum = lambda A,B : A + B

from MarvellousFMR import filterX, mapX, reduceX

def main():
    Data = []
    print("Enter number of elements : ")
    Size = int(input())
    
    print("Please enter numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
        
    print("Input Data : ",Data)

    FData = list(filterX(CheckEven, Data))
    print("Filter Output : ",FData)

    MData = list(mapX(Increase, FData))
    print("Map Output : ",MData)

    RData = reduceX(Sum, MData)
    print("Reduce Output : ",RData)
    
if __name__ ==  "__main__":
    main()

