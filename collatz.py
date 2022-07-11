# Enter a number into the Collatz Equation and see how many steps it takes to get to 1!

i = 0

def collatz(number):
    global i
    while number > 1:
        if number % 2 == 0:
            print(i + 1 , end=')  ')
            print(number // 2)
            number = number // 2
            i = i + 1
            collatz(number)
            break
        if number % 2 == 1:
            print(i + 1, end=')  ')
            print(3 * number + 1)
            number = 3 * number + 1
            i = i + 1
            collatz(number) 
            break      

try:
    print('Enter Number Into Collatzer 3000:')
    number = int(input())
    collatz(number)
except ValueError:
    print('You should really try entering a real integer next time!')