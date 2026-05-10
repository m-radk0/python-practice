def ordinalSuffix(number):
    if number % 100 in [11, 12, 13]:
        # Ending in 11, 12, 13 gives always "th"
        return f"{number}th"
    elif number % 10 == 1:
        return f"{number}st"
    elif number % 10 == 2:
        return f"{number}nd"
    elif number % 10 == 3:
        return f"{number}rd"
    else:
        return f"{number}th"

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'

# ----- Testing -----
# number = 5123
# print(str(number)[-1])

# number = 101
# if number % 10 == 1:
#     print('works')
#     print(str(number) + "st")

# % returns the remainder:
# 123 % 10 = (12 * 10) + 3 remainder 
