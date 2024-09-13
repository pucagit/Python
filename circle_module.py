import math

pi = math.pi

def calculate_area(radius):
    return pi * radius ** 2

def calculate_circumference(radius):
    return 2 * pi * radius

def calculate_volume(radius):
    return (4/3) * pi * radius ** 3

def calculate_surface_area(radius):
    return 4 * pi * radius ** 2

def main():
    radius = float(input("Enter the radius of the circle: "))
    print(f"The area of the circle is: {calculate_area(radius):.2f}")
    print(f"The circumference of the circle is: {calculate_circumference(radius):.2f}")
    print(f"The volume of the sphere is: {calculate_volume(radius):.2f}")
    print(f"The surface area of the sphere is: {calculate_surface_area(radius):.2f}")

if __name__ == '__main__': # to execute the main function when it is directly called
    main()