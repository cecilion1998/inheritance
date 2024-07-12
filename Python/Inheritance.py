class Father:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} goes to work")

    def hobby(self):
        print(f"{self.name} enjoys fishing")


class Mother:
    def __init__(self, name):
        self.name = name

    def cook(self):
        print(f"{self.name} cooks dinner")

    def read(self):
        print(f"{self.name} reads books")


class Child(Father, Mother):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def play(self):
        print(f"{self.name}, aged {self.age}, plays with friends")


# Example usage:
if __name__ == "__main__":
    father = Father("Mohammad")
    mother = Mother("Sahel")
    child = Child("Ali", 8)

    father.work()
    mother.cook()
    child.hobby()
    child.play()
