class Car:

    wheels = 4  # Class variable

    def __init__(self, make, model, year, color):
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable

    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} is stopped")


car_1 = Car("Chevy", "corvette", 2024, "blue")
car_2 = Car("Ford", "Mustang", 2024, "black")

car_1.wheels = 2  # changing number of wheels outside of class
print(car_1.wheels)
print(car_2.wheels)
