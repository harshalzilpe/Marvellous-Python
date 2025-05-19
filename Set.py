def main():
    """"
        ------Set------
        Syntax : { },
        Heterogenous,
        Unordered,
        Not indexed, 
        Data Imutable, 
        Set Mutable, 
        Duplicate not allowed
    """
    data = {10,90.67,"Hello",True,10}
    print("Data type is ",type(data))
    print("Length is ",len(data))
    print(data)
    
    # print(data[0])
    # print(data[1])
    
    data.add(71)
    print(data)
    
    data.remove(10)
    print(data)
    
    print("Data display using For Loop")
    for value in data:
        print(value, end=" ")

if __name__ == "__main__":
    main()