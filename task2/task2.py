import sys


class Solution:

    def __init__(self, file_name1, file_name2):
        self.file_name1 = file_name1
        self.file_name2 = file_name2

    def print_answer(self):
        from collections import namedtuple

        # namedtuple for circle/points description in simple form - to avoid classes
        Point = namedtuple('Point', 'x y')
        Circle = namedtuple('Circle', 'x y r')

        list_of_points = []

        # some optimization can be applied here - handle memory with care, direct output result e.t.c.

        with (open(self.file_name1, 'r', encoding='UTF-8') as file1,
              open(self.file_name2, 'r', encoding='UTF-8') as file2):

            # print('got inside w/OPEN')
            # input()

            circle_raw_data = []
            points_raw_data = []

            # prepare circle data

            # reading file with data
            for line in file1.readlines():
                circle_raw_data.append(line.strip())
            # value formation
            x, y = [float(i) for i in circle_raw_data[0].split(' ')]
            r = float(circle_raw_data[1])
            circle = Circle(x, y, r)

            # prepare points data -> store it in list

            # reading file with data
            for line in file2.readlines():
                points_raw_data.append(line.strip())
            # value formation - list of points, t.b.e.
            for raw_pos in points_raw_data:
                temp_list1 = raw_pos.split(' ')
                list_of_points.append(Point(*[float(i) for i in temp_list1]))

        # check each point in list to circle's parameters and print-out answer

        for point in list_of_points:

            distance = (point.x - circle.x) ** 2 + (point.y - circle.y) ** 2
            r2 = circle.r ** 2

            if distance > r2:
                print('2')
            elif distance == r2:
                print('0')
            else:
                print('1')

if __name__ == '__main__':
    a, b = sys.argv[1:]

    solution = Solution(a, b)
    solution.print_answer()