from unittest import TestCase
from src.__main__ import entry_point

class TestConsole(TestCase):
    def test_basic(self):
        entry_point()