import unittest
from solar_system import Question, planets

class QuestionTests(unittest.TestCase):
    def validate_question(self, question, expected):
        user_question = Question(question, planets)
        self.assertEqual(user_question.answer(), expected)

    #Unit testing the questions from the brief.
    def test_everything_about_saturn(self):
        self.validate_question("Tell me everything about Saturn?", "Saturn is a planet in the Solar System. \nSaturn has 13 moons: Mimas, Enceladus, Tethys, Dione, Calypso, Telesto, Helene, Polydeuces, Rhea, Titan, Hyperion, Iapetus, Phoebe. \nSaturn has a mass of 5.68317 x 10^26 kg. \nThe distance from Saturn and the Sun is between 9.08 - 10.12 AU.")

    def test_how_massive_is_neptune(self):
        self.validate_question("How massive is Neptune?", "Neptune has a mass of 1.02409 x 10^26 kg.")

    def test_pluto_question_returns_answer(self):
        self.validate_question("Is Pluto in the list of planets?", "Pluto is not a planet. Upon first discovery in 1930, Pluto was considered a planet in the Solar System, but in 2006 was reclassified as a dwarf planet.")

    def test_earth_moons_question_returns_answer(self):
        self.validate_question("How many moons does Earth have?", "Earth has 1 moon. The moon's name is The Moon.")

    # Some more tests I thought were relevant to add.
    def test_answer_is_empty(self):
        self.validate_question("", "Please enter a valid question.")

    def test_question_with_no_match(self):
        self.validate_question("Random planet", "I couldn't find the answer to your question. I can answer questions about one of the following planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.")

    # It would be too complicated to work with multiple planets at once and it was not mentioned in the brief.
    def test_multiple_planets_requested(self):
        self.validate_question("What are the masses of Earth and Mercury?", "You asked about two or more planets. Please only ask about one planet.")

    # Validating all the test cases for the moon reponses.
    def test_planet_with_zero_moons(self):
        self.validate_question("How many moons does Mercury have?", "Mercury has no moons.")

    def test_planet_with_one_moon(self):
        self.validate_question("How many moons does Earth have?", "Earth has 1 moon. The moon's name is The Moon.")

    def test_planet_with_multiple_moons(self):
        self.validate_question("How many moons does Mars have?", "Mars has 2 moons: Phobos, Deimos.")

    # Validating all the test cases for the distance from the Sun reponses.
    # In my solution you can ask for aphelion, perihelion or both at the same time (distance from the Sun). I have added a test for each.
    def test_distance_from_the_sun(self):
        self.validate_question("What is the distance from Uranus to the Sun?", "The distance from Uranus and the Sun is between 18.3 - 20.1 AU.")

    def test_distance_from_the_sun_aphelion(self):
        self.validate_question("What is the aphelion from Uranus to the Sun?", "The furthest point (aphelion) of Uranus's direct orbit around the Sun is 20.1 AU.")

    def test_distance_from_the_sun_perihelion(self):
        self.validate_question("What is the perihelion from Uranus to the Sun?", "The nearest point (perihelion) of Uranus's direct orbit around the Sun is 18.3 AU.")

    # Here are the mass based questions.
    def test_mass_of_planet(self):
        result = "Venus has a mass of 4.86731 x 10^24 kg." 
        self.validate_question("What is the mass of Venus?", result)
        self.validate_question("How big is Venus?", result)
        self.validate_question("What is the size of Venus?", result)
        self.validate_question("How heavy is Venus?", result)
        self.validate_question("What is the weight of Venus?", result)
        self.validate_question("How many kg is Venus?", result)
        