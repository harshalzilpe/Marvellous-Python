def main():
    """"
        ------Dict------
        Syntax : {key : value},
        Heterogenous,
        Ordered,
        Indexed (not numeric), 
        Data Mutable (only value),
        Key duplicate are allowed but old gets overwritten
        Value duplicate are allowed
    """
    data = {"Name" : "Let us C", "Author" : "Y Kanetkar", "Price" : 320, "Publication" : "BPB Publication"}
    
    print("Data type is ",type(data))
    print("Length is ",len(data))
    print(data)
    
    print(data["Author"])
    
    data["Price"] = 400
    print(data)
    
    print("Loop to display keys")
    for X in data:
        print(X, end=", ")
        
    print("Loop to display value")
    for Y in data.values():
        print(Y, end=", ")
        
    print("Loop to display key and value")
    for X,Y in data.items():
        print(X,":",Y)

if __name__ == "__main__":
    main()