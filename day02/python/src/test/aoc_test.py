import unittest

from day02.python.src import aoc


class MyTestCase(unittest.TestCase):

    def test_part1(self):
        aoc.start('../../../input.txt', 'part2')



if __name__ == '__main__':
    unittest.main()