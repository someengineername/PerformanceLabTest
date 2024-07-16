class Solution:

    def __init__(self, file_name: str):
        self._file_name = file_name
        print(self.calculate_answer())

    def calculate_answer(self):

        temp_list = []

        # read input file
        with open(self._file_name, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                temp_list.append(int(line.strip()))

        temp_list1 = sorted(temp_list)
        min_value, max_value = min(temp_list1), max(temp_list1)

        # store at least 1st sum of absolute delta's -> to check with later on
        last_value_storage = sum([abs(temp_list1[0] - j) for j in temp_list1])

        for i in range(min_value + 1, max_value + 1):
            delta_values = [abs(i - j) for j in temp_list1]

            sum_of_delta_values = sum(delta_values)

            # if calculated value greater than that one stored in memory - break the cycle
            if sum_of_delta_values > last_value_storage:
                break
            # if calculated value lower -> exchange value and go down by cycle
            else:
                last_value_storage = sum_of_delta_values

        return last_value_storage


if __name__ == '__main__':
    # file_name_input = 'test_file.txt'
    file_name_input = input()

    solution = Solution(file_name_input)
