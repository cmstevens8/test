import math  # Importing math for circle calculations

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2  # Using π * r²

# Function to calculate the circumference of a circle
def circle_circumference(radius):
    return 2 * math.pi * radius  # Using 2 * π * r

# Function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height  # Using (1/2) * base * height

# Function to calculate the perimeter of a square
def square_perimeter(side_length):
    return 4 * side_length

# Function to print both area and circumference of the circle
def circle_details(radius):
    area = circle_area(radius)
    circumference = circle_circumference(radius)
    print(f"The area of the circle is: {area}")
    print(f"The circumference of the circle is: {circumference}")

# Function to print which shape has a larger perimeter/circumference and larger area
def geometry(side_length, radius):
    square_perimeter_val = square_perimeter(side_length)
    circle_circumference_val = circle_circumference(radius)
    square_area_val = square_perimeter(side_length) ** 2  # Square area: side²
    circle_area_val = circle_area(radius)

    # Compare perimeter/circumference
    if square_perimeter_val > circle_circumference_val:
        print("The square has a larger perimeter than the circle")
    else:
        print("The circle has a larger circumference than the square")
    
    # Compare area
    if square_area_val > circle_area_val:
        print("The square has a larger area than the circle")
    else:
        print("The circle has a larger area than the square")

# Prompt the user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle is: {rectangle_area(length, width)}")

# Prompt the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle is: {circle_area(radius)}")

# Prompt the user for the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print(f"The area of the triangle is: {triangle_area(base, height)}")

# Prompt the user for the side length of the square and call the geometry function
side_length = float(input("Enter the side length of the square: "))
geometry(side_length, radius)
