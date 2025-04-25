class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        # return f'Car({self.color!r}, {self.mileage!r})'
        return (
            f'{self.__class__.__name__}('
            f'{self.color!r}, {self.mileage!r})'
        )

    def __str__(self):
        return f'a {self.color} car'


my_car = Car('red', 37281)
print(my_car)
'{}'.format(my_car)
my_car
