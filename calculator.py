from time import sleep
print('Calculator v1.0 (Python 3.6.2)')
isCalc = input('Hello! Are you here for calculating?(y/n)')

if isCalc == 'y':
     print('OK! LOADING...')
     sleep(3)
elif ans == 'n':
     print("Oh, you're not going ahead... OK.") # watch out for apostrophes in strings
     quit()

num1 = int(input('Input 1st number: '))
method = input('Input symbol(+,-,*,/): ')
num2 = int(input('Input 2nd number: '))
ans = 0

if method == '+':
     ans = num1 + num2
elif method == '-':
     ans = num1 - num2
elif method == '*':
     ans = num1 * num2
elif method == '/':
     ans = num1 / num2

print('Answer is ', ans)