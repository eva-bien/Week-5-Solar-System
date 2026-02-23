# GUI.py is the main entry point of this program, it imports parts from this file

class Planet:
    def __init__(self, name, mass, distance_from_the_sun, moons=[]):
        self.name = name
        # As mass is such a large number, I opted to use an int with scientific notation as a data type. 
        # Earth mass on Wikipedia is 5.97217×10^24 kg which is represented by scientific notation as 5.97217e24.
        # https://richardkilleen.co.uk/blog/python/python-scientific-notation/#:~:text=Right%20so%20python%20scientific%20notation,%2C%20you%20write%201e%2D06.
        # Using scientific notation is more versatile than holding the information about mass as a string.
        self.mass = mass 
        self.distance_from_the_sun = distance_from_the_sun
        # As per the brief I am not including numbers of moons larger than 30.
        self.moons = moons

    def convert_mass(self, mass):
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

    # Displaying different messages depending on how many moons a planet has. 
    def moon_answer(self, name, moons):
        if len(moons) == 0:
            return f"{name.title()} has no moons." 
        if len(moons) == 1:
            return f"{name.title()} has 1 moon. The moon's name is {moons[0].name}." 
        return f"{name.title()} has {len(moons)} moons: {', '.join([moon.name for moon in moons])}." 
    
    # Storing the distance from the Sun as a tuple enabled me to display a range in the answer.
    def distance_from_sun_answer(self, name, distance_from_the_sun):
        return f"The distance from {name.title()} and the Sun is between {distance_from_the_sun[0]} - {distance_from_the_sun[1]} AU."
    
    def min_max_from_sun_answer(self, name, type, distance_from_the_sun):
        # As I have already got this data, I decided to add this in when asked for it specifically.
        if type == "perihelion":
            return f"The nearest point ({type}) of {name}'s direct orbit around the Sun is {distance_from_the_sun[0]} AU."
        return f"The furthest point ({type}) of {name}'s direct orbit around the Sun is {distance_from_the_sun[1]} AU."

    def mass_answer(self, name, mass):
        return f"{name.title()} has a mass of {mass}." 
    
    # Question about mass can be asked in different ways, so I have decided to accept the following keywords in the questions and take them all as questions about mass.
    def is_mass_question(self, question):
        return "mass" in question.lower() or "big" in question.lower() or "size" in question.lower() or "heavy" in question.lower() or "kg" in question.lower() or "weight" in question.lower()

    # This is the method for providing a message that appears when a question about Pluto is asked.
    def pluto_answer(self):
        return "Pluto is not a planet. Upon first discovery in 1930, Pluto was considered a planet in the Solar System, but in 2006 was reclassified as a dwarf planet."

    def match_planet_to_question(self, question):
        matched_planets = []
        for item in self.planets:
            if item.name.lower() in question.lower():
                matched_planets.append(item)
        return matched_planets

    def answer(self):
        # No question provided 
        if self.question == "":
            return "Please enter a valid question."
        # Pluto question
        if "pluto" in self.question.lower():
            return self.pluto_answer()

        matched_planets = self.match_planet_to_question(self.question)
        # If question doesn't match any planets in the list
        if len(matched_planets) == 0:
            list_of_planets = []
            for planet in self.planets:
                list_of_planets.append(planet.name)
            return f"I couldn't find the answer to your question. I can answer questions about one of the following planets: {', '.join(list_of_planets[:-1])}, and {list_of_planets[-1]}."
        # If question is about more than 1 planet
        if len(matched_planets) > 1:
            return f"You asked about two or more planets. Please only ask about one planet."
        
        matched_planet = matched_planets[0]
        
        # Displaying different information based on the keywords provided in the question
        converted_mass = matched_planet.convert_mass(matched_planet.mass)
        if "moon" in self.question.lower():
            return self.moon_answer(matched_planet.name, matched_planet.moons)
        if "aphelion" in self.question.lower():
            return self.min_max_from_sun_answer(matched_planet.name, "aphelion", matched_planet.distance_from_the_sun)
        if "perihelion" in self.question.lower():
            return self.min_max_from_sun_answer(matched_planet.name, "perihelion", matched_planet.distance_from_the_sun)
        if "sun" in self.question.lower():
            return self.distance_from_sun_answer(matched_planet.name, matched_planet.distance_from_the_sun)
        if self.is_mass_question(self.question):
            return self.mass_answer(matched_planet.name, converted_mass)
        # Returning the full information if none of the specific keywords are mentioned in the question
        return f"{matched_planet.name} is a planet in the Solar System. \n{self.moon_answer(matched_planet.name, matched_planet.moons)} \n{self.mass_answer(matched_planet.name, converted_mass)} \n{self.distance_from_sun_answer(matched_planet.name, matched_planet.distance_from_the_sun)}"

# List of planets and their characteristics
planets = [

    Planet("Mercury", 3.3011e23, (0.31, 0.59), []),

    Planet("Venus", 4.86731e24, (0.72, 0.73), []),

    Planet("Earth", 5.97217e24, (0.98, 1.02), [
        Moon("The Moon")
    ]),

    Planet("Mars", 6.4171e23, (1.38, 1.67), [
        Moon("Phobos"), Moon("Deimos")
    ]),

    Planet("Jupiter", 1.898125e27, (4.95, 5.46), [
        Moon("Metis"), Moon("Adrastea"), Moon("Amalthea"), Moon("Thebe"),
        Moon("Io"), Moon("Europa"), Moon("Ganymede"), Moon("Callisto")
    ]),

    Planet("Saturn", 5.68317e26, (9.08, 10.12), [
        Moon("Mimas"), Moon("Enceladus"), Moon("Tethys"), Moon("Dione"),
        Moon("Calypso"), Moon("Telesto"), Moon("Helene"), Moon("Polydeuces"),
        Moon("Rhea"), Moon("Titan"), Moon("Hyperion"), Moon("Iapetus"),
        Moon("Phoebe")
    ]),

    Planet("Uranus", 8.68099e25, (18.3, 20.1), [
        Moon("Cordelia"), Moon("Ophelia"), Moon("Bianca"), Moon("Cressida"),
        Moon("Desdemona"), Moon("Juliet"), Moon("Portia"), Moon("Rosalind"),
        Moon("Cupid"), Moon("Belinda"), Moon("Perdita"), Moon("Puck"),
        Moon("Mab"), Moon("S/2025 U 1"), Moon("Miranda"), Moon("Ariel"),
        Moon("Umbriel"), Moon("Titania"), Moon("Oberon"), Moon("Francisco"),
        Moon("Caliban"), Moon("Stephano"), Moon("Trinculo"), Moon("Sycorax"),
        Moon("Margaret"), Moon("Prospero"), Moon("Setebos"), Moon("Ferdinand"),
        Moon("S/2023 U 1")
    ]),

    Planet("Neptune", 1.024092e26, (29.9, 30.5), [
        Moon("Naiad"), Moon("Thalassa"), Moon("Despina"), Moon("Galatea"),
        Moon("Larissa"), Moon("Hippocamp"), Moon("Proteus"), Moon("Triton"),
        Moon("Nereid"), Moon("Halimede"), Moon("Sao"), Moon("Laomedeia"),
        Moon("Psamathe"), Moon("Neso"), Moon("S/2002 N 5"), Moon("S/2021 N 1")
    ])

]
