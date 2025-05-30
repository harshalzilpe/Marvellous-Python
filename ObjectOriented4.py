class Employee:
    CompanyName = "Marvellous"      # Class Variable
    
    def __init__(self, A, B, C):    # Constructor
        print("Inside Constructor") 
        self.Name = A               # Instance Variable
        self.Salary = B             # Instance Variable
        self.City = C               # Instance Variable
        
    def __del__(self):
        print("Inside Destructor")  # Destructor
        
    def DisplayInfo(self):          # Instance Method
        print("Inside Instance method DisplayInfo")
        print("Employee Name : "+self.Name)
        print("Employee Salary : ",self.Salary)
        print("Employee City : "+self.City)
        
    @classmethod                    # Decorator
    def DisplayCompanyDetails(cls): # Class Method
        print("Inside Class method DisplayCompanyDetails")
        print("Company Name : "+cls.CompanyName)
    
    @staticmethod 
    def DisplayCompanyPolicy():     # Static Method
        print("Inside static method DisplayCompanyPolicy")
        print("All employees are 18+")
        print("Working hours are 9 to 6")
        print("Holidays : Saturday & Sunday")
        
def main():
    print("Class Variable : "+Employee.CompanyName)
    Employee.DisplayCompanyDetails()
    
    emp1 = Employee("Rahul", 15000, "Pune")     # Object Creation
    emp2 = Employee("Pooja", 25000, "Mumbai")   # Object Creation
    
    print("Employee Name: "+emp1.Name)
    print("Employee Salary: ",emp1.Salary)
    print("Employee City: "+emp1.City)
    
    emp2.DisplayInfo()
    
    Employee.DisplayCompanyPolicy()
    
    del emp1
    del emp2
    
if __name__ == "__main__":
    main()