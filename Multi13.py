import os, time

def fun(no):
    print("PID is ",os.getpid())
    sum = 0
    for i in range(1, no):
        sum = sum + (i*i*i)
    return sum

def main():
    data = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000,]
    result = []
    
    start_Time = time.time()
    
    for i in data:
        result.append(fun(i))
        
    print(result)
    
    end_Time = time.time()
    
    print("The required time is ",end_Time-start_Time)
    
if __name__ == "__main__":
    main()