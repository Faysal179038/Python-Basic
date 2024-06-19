# multi-level inheritance = when a child class is derived from more than one parent class


class Prey:

    def flee(self):
        print("Fleeing from predator")


class Predator:

    def hunt(self):
        print("Hunting prey")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Badger(Prey, Predator):
    pass


rabbit = Rabbit()

rabbit.flee()

hawk = Hawk()

hawk.hunt()

badger = Badger()

badger.flee()

badger.hunt()
