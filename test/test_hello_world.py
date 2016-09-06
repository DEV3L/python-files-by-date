from unittest import TestCase

class TestEmpty(TestCase):
    def test_empty_string_not_none(self):
        assert '' is not None
