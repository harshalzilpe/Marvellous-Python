CheckEven = lambda No : No % 2 == 0
Increase = lambda No : No + 1
Sum = lambda A,B : A + B

def filterX(Task, Values):
    Result = []
    
    for no in Values:
        Ret = Task(no)      # Ret.append(Task(no))
        if(Ret == True):
            Result.append(no)
        
    return Result

def mapX(Task, Values):
    Result = []
    
    for no in Values:
        Ret = Task(no) 
        Result.append(Ret)
        
    return Result
    
def reduceX(Task, Values):
    Result = 0
    
    for no in Values:
        Result = Task(Result, no)
        
    return Result

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