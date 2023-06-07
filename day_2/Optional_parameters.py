class Car(object):
    def init(self, make, model, year, condition="used", kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def showinfo(self, show_all=True):
        if show_all:
            print(f"This car is a {self.make} {self.model} from {self.year}, it is {self.condition}"
                  f" and has {self.kms} kilometers.")
        else:
            print(f"This car is a {self.make} {self.model} from {self.year}.")


my_brothers_car = Car('Renault', "Megane 3", 2009)
my_brothers_car.showinfo()