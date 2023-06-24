#print a string
print('hello world')

#math operation
x = 5
y = 9
print('sum : ' , x + 5)
print('multi : ' , x * 5)

#loops
for i in range(0, 1):
    print('for loop')

i = 0
while i != 1:
    print('while loop')
    i += 1

#if condition
if(1 == 1):
    print('if condition')
elif 1 != 1:
    print('from elif')
else :
    print('from else')

#take values from terminal
x = int(input('put a number'))
y = int(input('put a other number'))
print(f'sum {x} + {y} = {x + y}')