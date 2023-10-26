class Pet:
    """A Pet abstraction"""
    def __init__(self, color):
        self.color = color
        self.jump_count = 0

    def jump(self):
        self.jump_count += 1

class Dog(Pet):
    """A dog, which is a Pet"""
    def __init__(self, color):
        super().__init__(color)

    def speak(self):
        print("Arf")

class Husky(Dog):
    def __init__(self):
        super().__init__("Gray")

    def jump(self):
        self.jump_count += 10