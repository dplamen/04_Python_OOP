class Cat:
    def sound(self):
        print("Meow!")


class Train:
    def sound(self):
        print("Sound from wheels slipping!")


for any_type in Cat(), Train():
    any_type.sound()
