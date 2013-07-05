import time
def add(num1, num2):
    print(num1 + ' + ' + num2 + ' =')
    time.sleep(0.2)
    print(int(num1) + int(num2))

def subtract(num1, num2):
    print(num1 + ' - ' + num2 + ' =')
    time.sleep(0.2)
    print(int(num1) - int(num2))

def multiply(num1, num2):
    print(num1 + ' x ' + num2 + ' =')
    time.sleep(0.2)
    print(int(num1) * int(num2))

def divide(num1, num2):
    print(num1 + ' ÷ ' + num2 + ' =')
    time.sleep(0.2)
    print(int(num1) / int(num2))
    

    
print('Which numbers do you want to calculate?')
print('First number:')
toCalculate1 = input()
print('Good. Second number:')
toCalculate2 = input()
print('What operation do you want to use?')
choice = input()

def chooseFunction():
    if choice == 'Add':
        add(toCalculate1, toCalculate2)

    elif choice == 'Subract':
        subtract(toCalculate1, toCalculate2)

    elif choice == 'Multiply':
        multiply(toCalculate1, toCalculate2)

    else:    
        divide(toCalculate1, toCalculate2)

def playAgain():
    print('Another number?')
    choice2 = input()
    if choice2 != 'Yes' or 'yes' or 'Y' or 'y':
        kill
    else:
        chooseFunction()
        playAgain()
    
    
    

chooseFunction()
playAgain()


