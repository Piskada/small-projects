
num1 = int(input("Write the first number: "))
num2 = int(input("Write the second number: "))
op = input("Write the operator: ")

match op:
    case "+":
        res =(num1 + num2)
    case "-":
        res =(num1 - num2)
    case "*": 
        res =(num1 * num2)
    case "/":
        res = (num1 / num2)

print(f'result is {res}')
