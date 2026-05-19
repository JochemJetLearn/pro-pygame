class Computer:
    fans=True
    cpu=True
    gpu=True
    ram=True

    

    def run(self):
        print("starting...")
        print("computer is on")

my_computer=Computer()

parent_computer=Computer()

print(my_computer.fans)
print(parent_computer.cpu)

my_computer.run()