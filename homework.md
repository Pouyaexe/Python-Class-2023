Homework Title: Shape Hierarchy, Method Overriding, and Perimeter Calculation

## Problem Statement

You are tasked with designing a Python program to represent different shapes using classes and objects. The program should demonstrate the concept of inheritance, method overriding, and include a method to calculate the perimeter of each shape.

**Base Class:**

Create a base class called "Shape" that contains the following attributes and methods:

Attributes:
- `name`: A string representing the name of the shape.
- `color`: A string representing the color of the shape.

Methods:
- `__init__(self, name, color)`: Initializes the `name` and `color` attributes with the provided values.
- `area(self)`: A placeholder method that calculates and returns the area of the shape. Since the base class does not have any specific shape, the area calculation is not defined here.
- `perimeter(self)`: A placeholder method that calculates and returns the perimeter of the shape. Since the base class does not have any specific shape, the perimeter calculation is not defined here.

**Derived Classes:**

Create the following derived classes, each representing a specific shape. Each derived class should inherit from the base class "Shape" and implement the necessary attributes and methods.

1. Rectangle:
Attributes:
- `length`: A float representing the length of the rectangle.
- `width`: A float representing the width of the rectangle.

Methods:
- `area(self)`: Overrides the `area` method from the base class and calculates and returns the area of the rectangle (length * width).
- `perimeter(self)`: Overrides the `perimeter` method from the base class and calculates and returns the perimeter of the rectangle (2 * (length + width)).

2. Circle:
Attributes:
- `radius`: A float representing the radius of the circle.

Methods:
- `area(self)`: Overrides the `area` method from the base class and calculates and returns the area of the circle (π * radius^2).
- `perimeter(self)`: Overrides the `perimeter` method from the base class and calculates and returns the perimeter of the circle (2 * π * radius).

3. Triangle:
Attributes:
- `side1`: A float representing the length of the first side of the triangle.
- `side2`: A float representing the length of the second side of the triangle.
- `side3`: A float representing the length of the third side of the triangle.

Methods:
- `area(self)`: Overrides the `area` method from the base class and calculates and returns the area of the triangle using Heron's formula.
- `perimeter(self)`: Overrides the `perimeter` method from the base class and calculates and returns the perimeter of the triangle (side1 + side2 + side3).

**Instructions:**

1. Define the "Shape" class with the specified attributes and methods.
2. Implement the derived classes: "Rectangle," "Circle," and "Triangle," inheriting from the "Shape" class.
3. Override the `area` and `perimeter` methods in each derived class to calculate and return the respective shape's area and perimeter.
4. Test your implementation by creating instances of each shape and displaying their names, colors, areas, and perimeters.
5. Ensure that the program demonstrates the concept of inheritance, method overriding, and calculates the areas and perimeters correctly for each shape.

**Note:** You can use the value of π as 3.14159 for simplicity.

**Sample Output:**
```python
# Creating instances of each shape
rectangle = Rectangle("Rectangle", "Blue", 5.0, 3.0)
circle = Circle("Circle", "Red", 2.5)
triangle = Triangle("Triangle", "Green", 4.0, 6.0, 5.0)

# Displaying shape information, area, and perimeter
print(rectangle.name)
print(rectangle.color)
print(rectangle.area())  # Output: 15.0
print(rectangle.perimeter())  # Output: 16.0

print(circle.name)
print(circle.color)
print(circle.area())  # Output: 19.63495
print(circle.perimeter())  # Output: 15.70795

print(triangle.name)
print(triangle.color)
print(triangle.area())  # Output: 9.92156
print(triangle.perimeter())  # Output: 15.0
```

In the above example, we create instances of the derived classes, set their attributes (including the name and color inherited from the base class), and calculate their respective areas and perimeters using the overridden `area` and `perimeter` methods in each derived class.

Good luck!

-Pouya
