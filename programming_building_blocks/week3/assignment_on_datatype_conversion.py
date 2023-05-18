import math

# square = float(input('what is the length of a side of the square: '))
# square_num = square ** 2
# print('The area of the square is: ' + str(square_num))

# rectangle_len = float(input('what is the length of rectangle: '))
# rectangle_width = float(input('What is the width of rectangle: '))
# result = rectangle_len * rectangle_width
# print('The area of the rectangle is: ' + str(result))

#Here i import math function above to calculate 
#with the exact value of Pi
# circle = float(input('what is the radius of the circle: '))
# pi = math.pi
# radius = pi * circle ** 2 
# print(f'The are of the circle is {radius}')



#Here we prompt the user for a single number 
#Then we use the number to cal for
#area of a square, radius of circle,volume of cube
#and volume of a sphere
# number = float(input('Enter a number to be used: '))
# square_area = number ** 2
# circle_rad = math.pi * (number ** 2)
# vol_cube = number ** 3
# vol_sphere = 4/3 * math.pi * (number ** 3)

# print(f'The area of square is: {square_area}')
# print(f'The radius if a circle is: {circle_rad}')
# print(f'The volume of cube is: {vol_cube}')
# print(f'The volume of the sphere is: {vol_sphere}')

#stretch 3: meter conversion and citimeters

value = float(input('what is the length of a side of the square (in cm)?: '))
square_result = value ** 2
print(f'The area of a square in cm is {square_result} cm^2')
print(f'The area of a square in m is {square_result / 10000} m^2')

rectangle_len = float(input('what is the length of rectangle (in cm): '))
rectangle_width = float(input('What is the width of rectangle (in cm): '))
result2 = rectangle_len * rectangle_width
print('The area of the rectangle in cm is ' + str(result2) + ' cm^2')
print('The area of the rectangle in m is ' + str(result2 / 10000) + ' m^2')

#Here i import math function above to calculate 
#with the exact value of Pi
value = float(input('what is the radius of the circle (in cm): '))
pi = math.pi
radius2 = pi * value ** 2 
print(f'The are of the circle in cm is {radius2} cm^2')
print(f'The area of a circle in m is {radius2 / 10000} m^2')