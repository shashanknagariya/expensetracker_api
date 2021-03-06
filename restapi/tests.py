from unittest import TestCase

# Create your tests here.


def two_integer_sum(a, b):
    return a + b


class testsum(TestCase):
    def test_sum(self):
        self.assertEqual(two_integer_sum(1, 2), 3)
