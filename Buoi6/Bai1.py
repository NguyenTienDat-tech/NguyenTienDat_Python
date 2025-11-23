class Manufacturer:
    def __init__(self, identity, location):
        self.identity = identity
        self.location = location
    def describe(self):
        print(f"identity: {self.identity}, location: {self.location}")

class Device:
    def __init__(self, name, price, identity, location):
        self.name = name
        self.price = price
        self.manufacturer = Manufacturer(identity,location)
    def describe(self):
        print(f"name: {self.name}, price: {self.price}, identity: {self.manufacturer.identity}, location: {self.manufacturer.location} ")


Device1 = Device("mouse", 2.5, 9725, "Vietnam")
Device2 = Device("monitor", 12.5, 11, "Germany")
Device1.describe()
Device2.describe()

