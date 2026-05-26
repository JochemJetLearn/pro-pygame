class Controller:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.battery = 100

    def use(self, minutes):
        if self.battery > 0:
            print(f"{self.name} is being used.")
            self.battery -= minutes / 2
        else:
            print(f"{self.name} has no battery left. Please recharge.")
    
    def recharge(self, minutes):
        self.battery += minutes / 2
        if self.battery > 100:
            self.battery = 100
        print(f"{self.name} is recharged to {self.battery}% battery.")

class Keyboard:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.battery = 100

    def type(self, minutes):
        if self.battery > 0:
            print(f"{self.brand} keyboard is being used.")
            self.battery -= minutes / 2
        else:
            print(f"{self.brand} keyboard has no battery left. Please recharge.")
    
    def recharge(self, minutes):
        self.battery += minutes / 2
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} keyboard is recharged to {self.battery}% battery.")

my_controller = Controller("Xbox Controller", "Black")
friend_controller = Controller("PlayStation Controller", "White")
sister_controller = Controller("Nintendo Controller", "Red")
second_controller = Controller("Xbox Controller", "Black")

my_keyboard = Keyboard("Logitech", "Black")
friend_keyboard = Keyboard("Razer", "Green")
sister_keyboard = Keyboard("Corsair", "White")
second_keyboard = Keyboard("Logitech", "Black")

print(my_controller.name)
print(friend_controller.color)
my_controller.use(30)
friend_controller.use(45)
print(my_controller.battery)
my_controller.recharge(20)
print(my_controller.battery)

my_keyboard.type(15)
friend_keyboard.type(30)
print(my_keyboard.battery)
my_keyboard.recharge(10)
print(my_keyboard.battery)