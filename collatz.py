def collatz(number):
        while number != 1:
                if number % 2 == 0:
                        number = number // 2
                        print(number)
                elif number % 2 == 1:
                        number = 3 * number + 1
                        print(number)
                else:
                        break

print('Type an integer.')
try:
        collatz(int(input()))
        print('You did it!')
except:
        print('Error. You did not type an integer.')
