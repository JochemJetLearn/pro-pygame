class Family:
    religion = "Athist"
    sirname = "Miller"
    def __init__(self, name, age, height, friends, relation):
        self.name = name
        self.age = age
        self.height = height
        self.friends = friends
        self.relation = relation
        print("object created")
    
    def eating(self):
        print(f"{self.name}: let's have dinner together")
    
    def introduce(self):
        print(f"My name: {self.name}, my age: {self.age}, my height: {self.height}, my friends: {', '.join(self.friends)}, my relation: {self.relation}")

John = Family("John", 23, 180, ["James", "Jack"], "Son")
Mary = Family("Mary", 45, 165, ["Susan", "Jenny"], "Mother")
Tim = Family("Tim", 50, 185, ["Bob", "Tom"], "Father")

John.introduce()
Mary.introduce()
Tim.introduce()
Mary.eating()

print(Mary.sirname)
print(Tim.religion)