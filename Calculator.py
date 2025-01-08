
class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        return a / b

    def mul(self,a,b):
        return a*b*1000

    def mod(self, a,b):
        return a % b
    
    def iterator(self):
        for i in range(10):
            print("Manager Aditya")

if __name__=='__main__':

    calculator = Calculator()
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    print(calculator.add(a,b))
    print(calculator.subtract(a,b))

    print(calculator.divide(a,b))
    print(calculator.mul(a,b))
    print("---------------")
    calculator.iterator()
