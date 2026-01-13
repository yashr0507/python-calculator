import csv
import os
from datetime import datetime

class Calculator:
    def add(self, a,b):
        return a + b
    def subtract(self, a,b):
        return a - b
    def multiply(self, a,b):
        return a * b
    def divide(self, a,b):
        if b == 0:
            raise ZeroDivisionError
        return a / b
    def power(self, a,b):
        return a**b
    def modulus(self, a,b):
        if b == 0:
            raise ZeroDivisionError
        return a % b
    
calc = Calculator()

while True:
    log_row = False
    print("""
    Menu: +, -, *, /, **, %
    or press q to quit
          """)
    
    userinput = input('Enter decision: ') 
    if userinput == 'q':
        break

    if userinput not in ['+', '-', '*', '/', '**', '%']:
        print('Unrecognized Operator')
        continue

    try:
        a = float(input('Enter a Number: '))
        b = float(input('Enter another Number: '))
    except ValueError:
        print('Please enter numbers only.')
        continue

    if userinput == '+':
        result = (calc.add(a,b))
        print(result)
        log_row = True
    
    elif userinput == '-':
        result = (calc.subtract(a,b))
        print(result)
        log_row = True
        
    elif userinput == '*':
        result = (calc.multiply(a,b))
        print(round(result,3))
        log_row = True

    elif userinput == '/':
        try:
            result = (calc.divide(a,b))
            print(round(result,3))
            log_row = True
        except ZeroDivisionError:
            print('Can not divide a number by zero.')
            continue


    elif userinput == '**':
        result = (calc.power(a,b))
        print(round(result,3))
        log_row = True

    elif userinput == '%':
        try:
           result = (calc.modulus(a,b))
           print(round(result,2))
           log_row = True
        except ZeroDivisionError:
            print('Can not divide a number by zero.')
            continue
            

    file_exists = os.path.isfile('calculatorlog.csv')
    if log_row:
            with open('calculatorlog.csv', 'a', newline="") as log:
                writer = csv.writer(log)
                if not file_exists:
                    writer.writerow(['timestamp', 'operation', 'a', 'b', 'result']) 
                writer.writerow([datetime.now(), userinput, a, b, result])


