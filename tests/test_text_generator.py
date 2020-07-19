import unittest

from app.text_generator import TextGenerator


class TestTextGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.generator = TextGenerator('fixtures/sentences.txt', 'fixtures/out.txt')

    def test_number_of_rows(self):
        self.assertEquals(3, self.generator.number_of_lines)
