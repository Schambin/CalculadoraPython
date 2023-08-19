try:
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    op = input('Digite um operador: ')

    if op == '+':
        print(num1 + num2)
        
    elif op == '-':
        print(num1 - num2)
        
    elif op == '/':
        print(num1 / num2)
        
    elif op == '*':
        print(num1 * num2)

    elif op == '**':
        print(num1 ** num2)
        
    elif op == '%':
        print(num1 % num2)
        
    elif op == '//':
        print(num1 // num2)
        
    else:
        print('Escolha um operador válido.')
except:
    print('Escolha um NÚMERO válido.')
