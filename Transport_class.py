#BSCIT-01-0031/2026
# Parent class
class Vehicle:
    def __init__(self, registration_number, model):
        self.registration_number = registration_number
        self.model = model

    def displayVehicle(self):
        print("Registration Number:", self.registration_number)
        print("Vehicle Model:", self.model)


# Child class
class Bus(Vehicle):
    def __init__(self, registration_number, model, capacity):
        super().__init__(registration_number, model)
        self.capacity = capacity

    def displayBus(self):
        self.displayVehicle()
        print("Passenger Capacity:", self.capacity)


# Main section
bus1 = Bus("KDA 123A", "Toyota Coaster", 30)

bus1.displayBus()
