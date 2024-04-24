#-----------qetwryuiopasdfghjkl'zxcvbnm,.?123456789(@#%*+\!)
import math
def print_menu():
    print('welcome')
    print('operators:')
    print('+ for sum')
    print('- for sub')
    print('* for mul')
    print('/ for div')
    print('sin for sin')
    print('cos for cos')
    print('tan for tng')
    print('log for log')
    print('pow for power')
    print('sqrt for sqrt')
    print('press e to exit')
def calculator():
    
    while True:
        print_menu()
        operator = input('select operator plz:')
        if operator == 'e':
            break
        if operator not in ['+','-','*','/','sin','cos','tan','log','sqrt','pow']:
            print(' operator is not vlid')
            continue
        num1 = float(input('plz enter first number:'))
        num2 = float(input('plz enter second number:'))
        if operator == '+':
            result = num1 + num2
            print('result', result)
        elif operator == '-':
            result = num1 - num2
            print('result', result)
        elif operator == '*':
            result = num1 * num2
            print('result', result)
        elif operator == '/':
            result = num1 / num2
            print('result', result)
            if num2 == 0:
                print('syntax error')
            else:
                result = num1 / num2
        elif operator == 'log':
            result = math.log(num1,num2)
            print('result:', result)
        else:
            num1 = float(input('plz enter first number:'))
            if operator == 'sin':
             result = math.sin(num1)
             print('result:', result)
            elif operator == 'cos':
                result = math.cos(num1)
                print('result:', result)
            elif operator == 'tan':
                result = math.tan(num1)
                print('result:', result)
            elif operator == 'pow':
                result = math.pow(num1,num2)
                print('result:', result)
            elif operator == 'sqrt':
                result = math.sqrt(num1)
                print('result:', result)
print('**********************************')
calculator()