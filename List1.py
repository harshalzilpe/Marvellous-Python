
def main():
    """"
    ------List------
        Syntax : [],
        Heterogenous, 
        Ordered, 
        Indexed, 
        Data Mutable, 
        List Mutable, 
        Duplicate allowed
    """
    data = [10,90.67,"Hello",40, True]
    
    print("Data type is ",type(data))
    print("Length is ",len(data))
    print(data)
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    
    data[0] = 11
    print(data[0])
    
    data.append(40)
    print(data[4])
    
    print("Data display using Loop")
    for value in data:
        print(value)

if __name__ == "__main__":
    main()