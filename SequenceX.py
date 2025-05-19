PI = 3.14         # Global Variable

def CircleArea(Rad):
    Area = PI * Rad * Rad
    return Area

def main():
    print("Enter radius of circle : ")
    radius = float(input())
    
    result = CircleArea(radius)         # Positional Arguments
    
    print("Area of circle is : ", result)
    
if __name__ == "__main__":
    main()