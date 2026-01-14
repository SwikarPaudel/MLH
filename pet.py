# Object Oriented Digital Pet

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50      # 0 = full, 100 = very hungry
        self.happiness = 50   # 0 = sad, 100 = very happy

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            if self.hunger < 0:
                self.hunger = 0
            print(f"{self.name} has been fed!")
        else:
            print(f"{self.name} is already full.")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            if self.happiness > 100:
                self.happiness = 100
            self.hunger += 5   # Playing makes pet hungry
            if self.hunger > 100:
                self.hunger = 100
            print(f"You played with {self.name}!")
        else:
            print(f"{self.name} is already very happy!")

    def getStatus(self):
        print("\n---- Pet Status ----")
        print(f"Name: {self.name}")
        print(f"Hunger Level: {self.hunger}/100")
        print(f"Happiness Level: {self.happiness}/100")

        if self.hunger > 70:
            print(f"{self.name} is very hungry!")
        if self.happiness < 30:
            print(f"{self.name} is feeling sad.")
        print("--------------------")


# Create a pet
my_pet = Pet("Buddy")

# Interact with the pet
my_pet.getStatus()
my_pet.feed()
my_pet.play()
my_pet.getStatus()
