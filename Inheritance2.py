class Circle:
    PI = 3.14
    
    def __init__(self, A):
        print("Inside Circle Constructor")
        self.Radius = A
        
    def CalculateArea(self):
        Ans = 0.0
        Ans = Circle.PI * self.Radius * self.Radius
        return Ans

class CircleX(Circle):
    def __init__(self, B):
        print("Inside CircleX Constructor")
        super().__init__(B)
        
    def CalculateCircumference(self):
        Ans = 0.0
        Ans = 2 * Circle.PI * self.Radius
        return Ans

def main():
    obj = CircleX(10.5)
    Ret = obj.CalculateArea()
    print("Area of circle is ",Ret)
    
    ret = obj.CalculateCircumference()
    print("Circumference of Circle is ",ret)
    
if __name__ == "__main__":
    main()