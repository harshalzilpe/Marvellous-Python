def main():
    """"
        ------Tuple------
        Syntax : (),
        Heterogenous,
        Ordered,
        Indexed, 
        Data Imutable, 
        Tuple Imutable, 
        Duplicate allowed
    """
    data = (10,"Hello",90.67,True,10)
    print("Data type is ",type(data))
    print("Length is ",len(data))
    print(data)
    
    print(data[0])
    print(data[1])
    
    # data[0] = 11
    
    print("Data display using Loop")
    for value in data:
        print(value)
    
    print("Data display using Loop:range")
    for i in range(len(data)):
        print(data[i])

if __name__ == "__main__":
    main()