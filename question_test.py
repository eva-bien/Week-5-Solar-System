import unittest
from solar_system import Question, planets

class QuestionTests(unittest.TestCase):
    def validateQuestion(self, question, expected):
        user_question = Question(question, planets)
        self.assertEqual(user_question.answer(), expected)

    #Unit testing the questions from the brief.
    def test_everything_about_saturn(self):
        self.validateQuestion("Tell me everything about Saturn?", "Please enter a valid question.")

    def test_pluto_question_returns_answer(self):
        self.validateQuestion("Is Pluto in the list of planets?", "Pluto is not a planet. Upon first discovery in 1930, Pluto was considered a planet in the Solar System, but in 2006 was reclassified as a dwarf planet.")

    def test_earth_moons_question_returns_answer(self):
        self.validateQuestion("How many moons does Earth have?", "Earth has 1 moon. The moon's name is The Moon.")

    # Some more tests I thought were relevant to add.
    def test_answer_is_empty(self):
        self.validateQuestion("", "Please enter a valid question.")

