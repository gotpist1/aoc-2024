import unittest

from day02.python.src import aoc


class MyTestCase(unittest.TestCase):

    def test_part1(self):
        aoc.start('../../../input.txt', 'part2')

        #part2 758 to high | 398 to low, right for someone else.



if __name__ == '__main__':
    unittest.main()