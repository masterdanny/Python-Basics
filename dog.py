class Dog():
    """simple dog class"""

    def __init__(self, dog_name, gender, age):
        self.dog_name = dog_name
        self.gender = gender
        self.age = age
    
    def name(self):
        print("His name is" + self.dog_name)
    
    def gender(self):
        print("His gender is", self.gender)
    
    def age(self):
        print("He is currently " + self.age + " old.")

my_dog = Dog("Max", "male", 11)
my_dog.name()
