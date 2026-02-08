def __main__():
    print("Aloha")

__main__()

class Planet:
    def __init__(self, name, mass, distance, temperature, moons=[]):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.temperature = temperature
        self.moons = moons
