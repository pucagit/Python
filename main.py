# import circle_module

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(add(1,2,3,4,5))

# def print_addr(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# print_addr(name="John", age=30, city="New York")

# print("----------")

# list = [ x * 2 for x in range (1, 10)]
# print(list)

# print("----------")

# nums = [1, -2, 3, -4, 5]
# positive_nums = [num for num in nums if num >= 0]
# negative_nums = [num for num in nums if num < 0]
# print(positive_nums, negative_nums)

# print("----------")

# print(circle_module.pi)
# print(f"Circle's area:          {circle_module.calculate_area(4):.2f}")
# print(f"Circle's circumference: {circle_module.calculate_circumference(4):.2f}")
# print(f"Circle's volume:        {circle_module.calculate_volume(4):.2f}")
# print(f"Circle's surface area:  {circle_module.calculate_surface_area(4):.2f}")

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius
        print("Radius is deleted")

c = Circle(5)
c.radius = 10
# del c.radius
print(c.radius)