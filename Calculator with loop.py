print("=== Simple Calculator ===")
print("Choose operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

def saddie():
    operation = input("Enter your choice (+, -, *, /): ")
    numbers=input("Enter numbers: ").split()
    numbers=[float(p) for p in numbers]
    print(numbers)
    def add(numbers):
        result=0
        for n in numbers:            
            result+=n
        return result

    def subtract(numbers):
        result=0
        for n in numbers:    
            result-=n
        return result

    def multiply(numbers):
        result=1
        for n in numbers:
            result*=n
        return result
    

    def divide(numbers):
            if numbers == 0:
                result=1
                for n in numbers:    
                    result/=n
                return result

    if operation == '+':
        result = add(numbers)
    elif operation == '-':
        result = subtract(numbers)
    elif operation == '*':
        result = multiply(numbers)
    elif operation == '/':
        result = divide(numbers)
    else:
        result = "Invalid operator"

    print("Result:", result)

    cont = input("Do you want to continue Yes/No? ")
    YES = ("Yes","YES","YeS","Yes","Y","yES","yes","YeS","YEs","yeS","y")
    if cont in YES:
        saddie()
    else:
        print("Thank you for calculating")
saddie()
