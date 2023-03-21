# Define a class for a car object
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f"{self.make} {self.model}, {self.year}")

# Create a car object and print its information
my_car = Car("Toyota", "Corolla", 2022)
my_car.print_info()
