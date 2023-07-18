## Homework: Vehicle Rental System

You are tasked with creating classes to represent vehicles in a rental system. There are two types of vehicles: cars and bikes. Both car and bike classes should inherit from the Vehicle class provided below. Your task is to implement the Car and Bike classes and complete the given instructions.

Use the following code as a starting point for your parent Vehicle class:

```python
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
```

Instructions:
1. Create a Car class that inherits from the Vehicle class.
2. Implement the `__init__` method in the Car class. It should take the following arguments:
   - `name` (string): The name of the car.
   - `max_speed` (float): The maximum speed of the car.
   - `mileage` (float): The mileage (fuel efficiency) of the car.
   - `rental_price` (float): The rental price per day for the car.
   - `is_available` (bool): A flag indicating whether the car is available for rent or not. By default, it should be set to `True`.
3. Implement the `get_rental_price` method in the Car class. It should return the rental price of the car per day.
4. Implement the `is_rentable` method in the Car class. It should return `True` if the car is available for rent, and `False` otherwise.
5. Implement the `start_engine` method in the Car class. It should print a message indicating that the car's engine has started.
6. Implement the `stop_engine` method in the Car class. It should print a message indicating that the car's engine has stopped.
7. Create a Bike class that inherits from the Vehicle class.
8. Implement the `__init__` method in the Bike class. It should take the following arguments:
   - `name` (string): The name of the bike.
   - `max_speed` (float): The maximum speed of the bike.
   - `mileage` (float): The mileage (fuel efficiency) of the bike.
   - `rental_price` (float): The rental price per day for the bike.
   - `is_available` (bool): A flag indicating whether the bike is available for rent or not. By default, it should be set to `True`.
9. Implement the `get_rental_price` method in the Bike class. It should return the rental price of the bike per day.
10. Implement the `is_rentable` method in the Bike class. It should return `True` if the bike is available for rent, and `False` otherwise.
11. Implement the `ring_bell` method in the Bike class. It should print a message indicating that the bike's bell is ringing.
12. Test your implementation by creating instances of the Car and Bike classes and calling the methods on them. Print the results to verify the correctness of your code.

**Note:** You are only required to implement the Car and Bike classes. The provided Vehicle class should not be modified.

### Example Usage:

```python
# Create an instance of the Car class
car1 = Car("Toyota Camry", 180, 35.5, 50.0, True)

# Test the get_rental_price method
print(car1.get_rental_price())  # Output: 50.0

# Test the is_rentable method
print(car1.is_rentable())  # Output: True

# Test the seating_capacity method inherited from the Vehicle class
print(car1.seating_capacity(5))  # Output: The seating capacity of a Toyota Camry is 5 passengers

# Test the start_engine method specific to the Car class
car1.start_engine()  # Output: The engine of the Toyota Camry has started

# Create an instance of the Bike class
bike1 = Bike("Mountain Bike", 30, 15.0, 25.0, False)

# Test the get_rental_price method of the Bike class
print(bike1.get_rental_price())  # Output: 25.0

# Test the is_rentable method of the Bike class
print(bike1.is_rentable())  # Output: False

# Test the seating_capacity method inherited from the Vehicle class for the Bike class
print(bike1.seating_capacity(1))  # Output: The seating capacity of a Mountain Bike is 1 passenger

# Test the ring_bell method specific to the Bike class
bike1.ring_bell()  # Output: The bell of the Mountain Bike is ringing
```

**Note:** The above example assumes that the Car and Bike classes are implemented correctly. The output may vary if there are errors in the implementation.

Remember to test your code with different scenarios and edge cases to ensure its correctness.

Good luck!

-Pouya
