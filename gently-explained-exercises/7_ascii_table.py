def print_acii_table ():
    for i in range(32, 127):
        print(f"{i} {chr(i)}")
        
        # asii_text = chr(i)
        # print(f"{i} {asii_text}")
        
print_acii_table()

# ord() 
# accepting a string of a single character 
# and returning its integer code point. (ordinal)

# chr()
# accepts an integer argument of a code point 
# and returns the string of that code point’s character.