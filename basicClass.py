class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__walk()

    def name_name(self):
        print(f'My name is {self.name}')

    def speak(self):
        print("speak")

    def _walk(self):
        print("I walk")


class Dog(Animal):
    def __walk(self):
        print("I walk private")

    def _walk(self):
        print("I walkkkk")

    def speak(self):
        print("I bark")
        # Dog.__walk(self)


class Cat(Animal):
    def speak(self):
        print("I meow")
        Dog.speak(self)
        Dog._walk(self)


# dog = Dog("Jimmy", 2)
# dog.speak()
# dog.name_name()
cat = Cat("Julie", 2)
cat.speak()
# cat.name_name()
# cat.__walk()
# dog.__walk()

a = Animal("manju", 34)
a.name_name()
