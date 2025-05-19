
def CircleArea(Rad, PI = 3.14):     # Default Argument
    Area = PI * Rad * Rad
    return Area

def main():
    print("Enter radius of circle : ")
    radius = float(input())
    
    result = CircleArea(Rad = radius)
    
    print("Area of circle is : ", result)
    
if __name__ == "__main__":
    main()