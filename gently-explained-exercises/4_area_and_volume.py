def area(lenght, width):
    return lenght * width

def perimeter(lenght, width):
    return (lenght + width) * 2

def volume(lenght, width, height):
    return lenght * width * height
    
def surfaceArea(lenght, width, height):
    return((lenght * width) + (lenght * height) + (width * height)) * 2
    # return(lenght * width * 2) + (lenght * height * 2) + (width * height * 2)
   
assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340