print("Let's see a Collatz Sequence")
print('Choose a number:')

def collatz(number):
    if number %2 == 0:
        return number//2
    
    else:
        return 3 * number +1
        
try:
    number = int(input())

except ValueError:
    print('Whoops! That is not a valid number')
    print('Enter another number without letters.')
    number = int(input())   #An actual number after an 'invalid one' is entered. So the program can continue.
                            
while number != 1:
    number= collatz(number)
    print(number)

collatz(number)

