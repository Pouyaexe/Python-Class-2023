**Follow-up Homework: Area Calculation for Isosceles and Equilateral Triangles**

For the follow-up homework, we will focus specifically on the `Triangle` class and introduce two new derived classes: `IsoscelesTriangle` and `EquilateralTriangle`. Both of these classes will be special cases of the `Triangle` class, and we will override the `area` method for each of them to calculate their areas using specific formulas. Additionally, we will implement the `perimeter` method for both classes.

Problem Statement:

1. Create a new class called `IsoscelesTriangle` that inherits from the `Triangle` class.
2. Add an attribute called `base`, representing the length of the base of the isosceles triangle.
3. Implement the `area` method for `IsoscelesTriangle` to calculate and return the area of the isosceles triangle using the formula: `area = 0.5 * base * height`, where `height` can be calculated using the Pythagorean theorem: `height = sqrt(side1^2 - (0.25 * base^2))`.
4. Implement the `perimeter` method for `IsoscelesTriangle` to calculate and return the perimeter of the isosceles triangle.
5. Create a new class called `EquilateralTriangle` that also inherits from the `Triangle` class.
6. Implement the `area` method for `EquilateralTriangle` to calculate and return the area of the equilateral triangle using the formula: `area = (sqrt(3) / 4) * side1^2`.
7. Implement the `perimeter` method for `EquilateralTriangle` to calculate and return the perimeter of the equilateral triangle.

Instructions:

1. Implement the `IsoscelesTriangle` class and override the `area` and `perimeter` methods.
2. Implement the `EquilateralTriangle` class and override the `area` and `perimeter` methods.
3. Test your implementation by creating instances of each type of triangle and displaying their names, colors, areas, and perimeters.
4. Ensure that the program calculates the areas and perimeters correctly for each type of triangle.

Sample Output:

```python
isosceles_triangle = IsoscelesTriangle("Isosceles", "Purple", 5.0, 4.0)
equilateral_triangle = EquilateralTriangle("Equilateral", "Yellow", 6.0)

print(isosceles_triangle.name)
print(isosceles_triangle.color)
print(isosceles_triangle.area())  # Output: 8.0
print(isosceles_triangle.perimeter())  # Output: 13.0

print(equilateral_triangle.name)
print(equilateral_triangle.color)
print(equilateral_triangle.area())  # Output: 15.58845
print(equilateral_triangle.perimeter())  # Output: 18.0
```

In this example, we have created instances of `IsoscelesTriangle` and `EquilateralTriangle`, set their attributes (including the name and color inherited from the `Triangle` class), and calculated their respective areas and perimeters using the overridden `area` and `perimeter` methods in each derived class.
