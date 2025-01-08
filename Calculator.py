
class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def mod(self, a,b):
        return a % b
    

if __name__=='__main__':

    calculator = Calculator()
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    print(calculator.add(a,b))