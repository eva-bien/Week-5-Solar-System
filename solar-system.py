class Planet:
    def __init__(self, name, mass, distance_from_the_sun, moons=[]):
        self.name = name
        # As mass is such a large number, I opted to use scientific notation as a data type. 
        # Earth mass on Wikipedia is (5.97217±0.00028)×10^24 kg which is represented by scientific notation as 5.97217e24.
        # https://richardkilleen.co.uk/blog/python/python-scientific-notation/#:~:text=Right%20so%20python%20scientific%20notation,%2C%20you%20write%201e%2D06.
        self.mass = mass 
        self.distance_from_the_sun = distance_from_the_sun
        self.moons = moons

    def convertMass(self, mass):
        # Scientific notation is not human-readable. Below is a method of converting the scientific number into a well displayed number.
        # I used this discussion as inspiration: https://stackoverflow.com/questions/56029841/how-to-print-coefficient-and-exponent-separate-from-each-other-in-python.
        base, power = f"{mass:.4e}".split("e")
        power = int(power)
        return f"{base} x 10^{power} kg"

class Moon:
    def __init__(self, name):
        self.name = name

class Question:
    def __init__(self, question, planets):
        self.question = question
        self.planets = planets

    def moonAnswer(self, name, moons):
        if len(moons) == 0:
            return f"{name.title()} has no moons." 
        if len(moons) == 1:
            return f"{name.title()} has 1 moon. The moon's name is {moons[0].name}." 
        return f"{name.title()} has {len(moons)} moons: {', '.join([moon.name for moon in moons])}." 
    
    def distanceFromSunAnswer(self, name, distance_from_the_sun):
        return f"The distance from {name.title()} and the Sun is between {distance_from_the_sun[0]} - {distance_from_the_sun[1]} AU."

    def massAnswer(self, name, mass):
        return f"{name.title()} has a mass of {mass}." 
    
    def isMassQuestion(self, question):
        return "mass" in question.lower() or "big" in question.lower() or "size" in question.lower() or "heavy" in question.lower() or "kg" in question.lower()

    def answer(self):
        for item in self.planets:
            if item.name.lower() in self.question.lower():
                if "moon" in self.question.lower():
                    return self.moonAnswer(item.name, item.moons)
                if "sun" in self.question.lower():
                    return self.distanceFromSunAnswer(item.name, item.distance_from_the_sun)
                if self.isMassQuestion(self.question):
                    return self.massAnswer(item.name, item.convertMass(item.mass))
                return f"{self.moonAnswer(item.name, item.moons)} \n{self.massAnswer(item.name, item.mass)}"
        return "no match"

def __main__():
    planets = [
        Planet("Earth", 5.97217e24, (0.98, 1.02), [Moon("The Moon")])
        ]
    user_question = Question(input("My name is Cosmos🌝. Ask me about the Solar System. "), planets)
    answer = user_question.answer()
    print(answer)

__main__()

