import unittest

from day05.python.src import aoc


class MyTestCase(unittest.TestCase):

    def test_part1(self):
        aoc.start('../../../input.txt', 'part1')

    def test_part2(self):
        aoc.start('../../../input.txt', 'part2')

if __name__ == '__main__':
    unittest.main()