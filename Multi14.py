import os, time, multiprocessing

def fun(no):
    print("PID is ",os.getpid())
    sum = 0
    for i in range(1, no):
        sum = sum + (i*i*i)
    return sum

def main():
    start_Time = time.time()
    
    data = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000,]
    result = []
    
    p = multiprocessing.Pool()
    result = p.map(fun, data)
    
    p.close()
    p.join()
        
    print(result)
    
    end_Time = time.time()
    
    print("The required time is ",end_Time-start_Time)
    
if __name__ == "__main__":
    main()