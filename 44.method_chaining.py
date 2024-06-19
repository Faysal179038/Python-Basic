# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self


class Car:

    def turn_on(self):
        print("You turn on the engine.")
        return self  # return self to allow method chaining

    def drive(self):
        print("You drive the car.")
        return self  # return self to allow method chaining

    def brake(self):
        print("You step on the break")
        return self  # return self to allow method chaining

    def turn_off(self):
        print("You turn off the engine.")
        return self  # return self to allow method chaining


car = Car()

# car.turn_on().drive()
# car.brake().turn_off()


car.turn_on().drive().brake().turn_off()
