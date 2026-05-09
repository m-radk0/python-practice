def fizzBuzz(upTo):
    
    for i in range(1, upTo + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

fizzBuzz(35)

# end=" " - prints the statesments in the same line with space
# by default print uses end="\n"
# Also i % 3 == 0 and i % 5 == 0 can be changed to i % 15 == 0