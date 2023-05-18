#IMPORTING THE FUNCTION 
from modules import compute_area_square, cal_area_square, compute_area_rectangle
from modules import cal_area_rectangle, compute_area_circle, calculate_area_circle

#Computing the area of a square in (cm)
print("what is the length of a side of the square (in cm)?: ", end="")
value = float(input(""))
cm_result = compute_area_square(value)
m_result = cal_area_square(value)
print("The area of a square in cm is: {} cm^2".format(cm_result))
print("The area of a square in m is: {} m^2".format(m_result))

print()

#Computing the area of a rectangle in (cm)
print("what is the length of rectangle (in cm): ", end="")
rectangle_len = float(input(""))
print("What is the width of rectangle (in cm): ", end="")
rectangle_width = float(input(""))

cm_result = compute_area_rectangle(lenght=rectangle_len, width=rectangle_width)
m_result = cal_area_rectangle(lenght=rectangle_len, width=rectangle_width)
print("The area of a rectangle in cm is: {} cm^2".format(cm_result))
print("The area of a rectangle in m is: {} m^2".format(m_result))

#OR USE THIS BUT WITH NAME NOTATION
print(compute_area_rectangle(rectangle_len, rectangle_width))
print(cal_area_rectangle(rectangle_len, rectangle_width))

print()


#Computing the area of a circle in (cm)
print("what is the radius of the circle (in cm): ",end="")
value = float(input(""))

cm_result = compute_area_circle(value)
m_result = calculate_area_circle(value)

print("The area of a circle in cm is: {:.2f} cm^2".format(cm_result))
print("The area of a circle in m is: {:.2f} m^2".format(m_result))


