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
