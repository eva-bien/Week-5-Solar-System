class Planet:
    def __init__(self, name, mass, distance_from_the_sun, moons=[]):
        self.name = name
        # As mass is such a large number, I opted to use scientific notation as a data type. 
        # Earth mass on Wikipedia is 5.97217×10^24 kg which is represented by scientific notation as 5.97217e24.
        # https://richardkilleen.co.uk/blog/python/python-scientific-notation/#:~:text=Right%20so%20python%20scientific%20notation,%2C%20you%20write%201e%2D06.
        self.mass = mass 
        self.distance_from_the_sun = distance_from_the_sun
        # As per the brief I am not including numbers of moons larger than 30.
        self.moons = moons

    def convertMass(self, mass):
        # Scientific notation is not human-readable. Below is a method of converting the scientific number into a well displayed number.  Most of the planets in the data set rounded the mass to 5 decimal places, so I have kept it consistent. 
        # I used this discussion as inspiration: https://stackoverflow.com/questions/56029841/how-to-print-coefficient-and-exponent-separate-from-each-other-in-python.
        base, power = f"{mass:.5e}".split("e")
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
    
    def minMaxFromSunAnswer(self, name, type, distance_from_the_sun):
        # As I have already got this data, I decided to add this in when asked for it specifically.
        if type == "perihelion":
            return f"The nearest point ({type}) of {name}'s direct orbit around the Sun is {distance_from_the_sun[0]} AU."
        return f"The furthest point ({type}) of {name}'s direct orbit around the Sun is {distance_from_the_sun[1]} AU."

    def massAnswer(self, name, mass):
        return f"{name.title()} has a mass of {mass}." 
    
    def isMassQuestion(self, question):
        return "mass" in question.lower() or "big" in question.lower() or "size" in question.lower() or "heavy" in question.lower() or "kg" in question.lower()

    def plutoAnswer(self):
        return f"Pluto is not a planet. Upon first discovery in 1930, Pluto was considered a planet in the Solar System, but in 2006 was reclassified as a dwarf planet."

    def matchPlanetToQuestion(self, question):
        for item in self.planets:
            if item.name.lower() in question.lower():
                return item
        return None

    def answer(self):
        if self.question == "":
            return f"Please enter a valid question."
        if "pluto" in self.question.lower():
            return self.plutoAnswer()

        found_planet = self.matchPlanetToQuestion(self.question)
        if found_planet == None:
            list_of_planets = []
            for planet in self.planets:
                list_of_planets.append(planet.name)
            return f"I couldn't find the answer to your question. I can answer questions about the following planets: {', '.join(list_of_planets[:-1])}, and {list_of_planets[-1]}."
        
        converted_mass = found_planet.convertMass(found_planet.mass)
        if "moon" in self.question.lower():
            return self.moonAnswer(found_planet.name, found_planet.moons)
        if "sun" in self.question.lower():
            return self.distanceFromSunAnswer(found_planet.name, found_planet.distance_from_the_sun)
        if "aphelion" in self.question.lower():
            return self.minMaxFromSunAnswer(found_planet.name, "aphelion", found_planet.distance_from_the_sun)
        if "perihelion" in self.question.lower():
            return self.minMaxFromSunAnswer(found_planet.name, "perihelion", found_planet.distance_from_the_sun)
        if self.isMassQuestion(self.question):
            return self.massAnswer(found_planet.name, converted_mass)
        return f"{found_planet.name} is a planet in the Solar System. \n{self.moonAnswer(found_planet.name, found_planet.moons)} \n{self.massAnswer(found_planet.name, converted_mass)} \n{self.distanceFromSunAnswer(found_planet.name, found_planet.distance_from_the_sun)}"

planets = [
    Planet("Earth", 5.97217e24, (0.98, 1.02), [Moon("The Moon")]),
    Planet("Mars", 6.4171e23, (1.38, 1.67), [Moon("Phobos"), Moon("Deimos")])
        ]  


def __main__():

    user_question = Question(input("My name is Cosmos🌝. Ask me about the Solar System. "), planets)
    answer = user_question.answer()
    print(answer)




if __name__ == "__main__":
    __main__()

