import os
import unittest

from day01.src import aoc


class MyTestCase(unittest.TestCase):

    def test_part1(self):
        aoc.start('input.txt', 'part1')



if __name__ == '__main__':
    unittest.main()
