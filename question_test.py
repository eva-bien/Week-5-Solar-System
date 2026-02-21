import unittest
from solar_system import Question, planets

class QuestionTests(unittest.TestCase):
    def test_pluto_question_returns_answer(self):
        user_question = Question("Is Pluto in the list of planets?", planets)
        answer = user_question.answer()
        self.assertEqual(answer, "Pluto is not a planet. Upon first discovery in 1930, Pluto was considered a planet in the Solar System, but in 2006 was reclassified as a dwarf planet.")