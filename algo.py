# --------> multiple
def multiple():
    var1 = int(input('enter a number : '))
    var2 = int(input('enter a number : '))
    var3 = int(input('enter a number : '))
    print(f'multiple : {var1 * var2 * var3}')
# to call the function => multiple()


# --------> odd or even
def number_type():
    print('the number must be between 1 and 30')
    var = int(input('enter a number : '))
    if var > 30 or var < 1:
        return 'the number must be between 1 and 30'
    if var % 2 == 0:
        print(f'the number {var} is even')
    else:
        print(f'the number {var} is odd')
# number_type()


# --------> multiple of a number
def number_multiple(var):
    for i in range(0, 11):
        print(f'{var} x {i} = {var * i}')
# number_multiple(7)


# --------> the factorial algo
def factorial(var):
    factorial = 1
    for i in range(1, var + 1):
        factorial *= i
    print(f'{var} factorial is : {factorial}')
#factorial(5)


# --------> infinit condition
def just_try():
    while True:
        num = int(input('Enter your number : '))
        if num > 20:
            print('Ops the number must be less than ', num)
        if num < 10:
            print('Ops the number must be greater than ', num)
        if num >= 10 and num <= 20:
            print('BOOYAH you did it :) .....')
            break
#just_try()


#--------> ecomm_return algo => algo tha show how many 10 dollars and 5 dollars and 1 dollar you have to return based on client cash 
def cach(price, htt):
    price -= htt
    tenDollars = int(price / 10)
    price %= 10
    fiveDollars = int(price / 5)
    price %= 5
    oneDollars = int(price / 1)
    print(f'you have to return \n==> 10 dollars : {tenDollars}\n==> 5 dollars : {fiveDollars}\n==> 1 dollars {oneDollars}')
#cach(567, 300)