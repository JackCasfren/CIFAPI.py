def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Parameters:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return width * height

# Display the docstring using the help() function


help(calculate_area)


#? For some reason i was thinking of this excersise, one can make some really hard ones.
''' 
for i in range(5):
    for i in range(4):
        print("*")
'''
#* For loops change substancially between js and python.
'''
stars = ""
for i in range(5):
    stars +"*"
    for i in range(4):
        stars += "*"
print(stars)

'''
#simple square:
for i in range(3):
    print("*****")

# Now "+" upside down piramyd

star_num = 5
space_num = 2
to_print = ""
#print(star_num * "+")
for i in range(star_num):
    to_print = space_num * "_" + star_num * "+"
    star_num = star_num-1
    space_num = space_num+1
    

    to_print += star_num * "+" + (space_num-1) * "_"
    #moving this down here because i wanted it to have a center piece, it made it more challenging.
    print(to_print)