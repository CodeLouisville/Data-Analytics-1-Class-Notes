from unittest import TestCase
from order import MENU, get_prompt

class TestOrder(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.good_menu = MENU

    def test_input(self):
        print("tested")

    def test_valid_manu_get_prompt(self):
        prompt = get_prompt(self.good_menu)
        for value in self.good_menu.values():
            self.assertIn(value, prompt)

    def test_invalid_manu_get_prompt(self):
        bad_menu = [1, 2, 3, 4, 5]
        with self.assertRaises(AttributeError):
            prompt = get_prompt(bad_menu)