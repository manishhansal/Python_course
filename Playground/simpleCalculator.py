while True:
    num1 = int(input('Enter your first number: '))
    operator = input('Enter your operator(eg. +, -, *, /, %, //, **): ')
    num2 = int(input('Enter your second number: '))
    if operator == '+':
        output = num1 + num2
        print('Your output is', output)
    elif operator == '-':
        output = num1 - num2
        print('Your output is', output)
    elif operator == '*':
        output = num1 * num2
        print('Your output is', output)
    elif operator == '/':
        output = num1 / num2
        print('Your output is', output)
    elif operator == '%':
        output = num1 % num2
        print('Your output is', output)
    elif operator == '//':
        output = num1 // num2
        print('Your output is', output)
    elif operator == '**':
        output = num1 ** num2
        print('Your output is', output)
    else:
        print('You have entered invalid operator.')
