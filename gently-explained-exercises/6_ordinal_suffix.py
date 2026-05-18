# Solution #2: -----------------------------------------------------------------
def ordinalSuffix(number):
    number_str = str(number)
    if number_str[-2:] in ('11', '12', '13'):
        return f"{number_str}th"
    elif number_str[-1] == "1":
        return f"{number_str}st"
    elif number_str[-1] == "2":
        return f"{number_str}nd"
    elif number_str[-1] == "3":
        return f"{number_str}rd"
    else:
        return f"{number_str}th"
    
# ---
    # if number_str[-2:] == "11":
    #     return f"{number_str}th"
    # elif number_str[-2:] == "12":
    #     return f"{number_str}th"
    # elif number_str[-2:] == "13":
    #     return f"{number_str}th"
# ---

# Solution #1: -----------------------------------------------------------------
# def ordinalSuffix(number):
#     if number % 100 in [11, 12, 13]:
#         # Ending in 11, 12, 13 gives always "th"
#         return f"{number}th"
#     elif number % 10 == 1:
#         return f"{number}st"
#     elif number % 10 == 2:
#         return f"{number}nd"
#     elif number % 10 == 3:
#         return f"{number}rd"
#     else:
#         return f"{number}th"

print("\nworks")

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

# ******************************************************************************
# Chrez [] se dostupva do value/element/
# Indeksaciqta zapochva ot 0 -> 1, 2, 3...
# Purviqt element ot niza e 0, vtoriqt element e 1...
# Slice format:
# text[start:stop]  - vzemi ot start do stop, no bez stop

# text = "Python"
# print(text[0:2])    - "Py"
# print(text[2:5])    - "tho"
# print(text[:3])     - "Pyt" vzemi ot nachaloto do 3, no bez 3
# print(text[-2:])    - "on" vzemi poslednite dve do kraq
# posledniq element ima indeks -1

# number_str[-2:] in ["11", "12", "13"] 
# - Check if the last two characters are 11, 12, or 13.

# ["11", "12", "13"]    - is list, can be changed
# ("11", "12", "13")  - is tuple, cannot be changed