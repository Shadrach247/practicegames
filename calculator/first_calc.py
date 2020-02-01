calc_on = 1

def addition():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first + second)

def subtraction():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first - second)

def multiplication():
    first = int(input('What is your first number? '))
    second = int(input('What is your second_number? '))
    print(first * second)

def division():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first / second)

def modulo():
    first = int(input('What is your first number? '))
    second = int(input('What is your second number? '))
    print(first % second)

def count_to_ten():
    for number in range(1, 11):
        print(number)

def quit():
    global calc_on
    calc_on = 0

def calc_run():
    op = input('add, subtract, multiply, divide, or module, ten, or quit? ')
    if op == 'add':
        addition()
    elif op == 'subtract':
        subtraction()
    elif op == 'multiply':
        multiplication()
    elif op == 'divide':
        division()
    elif op == 'modulo':
        modulo()
    elif op == 'ten':
        count_to_ten()
    else:
        quit()
        # print('Thank you. Goodbye!')

while calc_on == 1:
    calc_run()