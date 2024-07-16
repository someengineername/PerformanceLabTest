import random
import time

list_db = [[random.randint(-10000, 10000) for i in range(1, random.randint(2, 5))] for _ in range(1000)]
print(list_db)


# solution here:...

def solution1(input_list):
    temp_list1 = sorted(input_list)

    min_value, max_value = min(temp_list1), max(temp_list1)

    last_value_storage = sum([abs(temp_list1[0] - j) for j in temp_list1])

    for i in range(min_value + 1, max_value + 1):
        delta_values = [abs(i - j) for j in temp_list1]

        sum_of_delta_values = sum(delta_values)

        # if calculated value greater than stored in memory - break the cycle, return value in memory
        if sum_of_delta_values > last_value_storage:
            break
        # if calculated value lower - than exchange value and keep on
        else:
            last_value_storage = sum_of_delta_values
    return last_value_storage


def solution2(input_list):
    temp_list1 = sorted(input_list)
    # print('orient:', temp_list1)
    min_value, max_value = min(temp_list1), max(temp_list1)

    total_delta_ranges = []

    for i in range(min_value, max_value + 1):
        delta_values = [abs(i - j) for j in temp_list1]

        # print(delta_values)

        sum_of_delta_values = sum(delta_values)

        # if list not empty - just lay down value
        if total_delta_ranges:

            # check if value bigger than last
            if sum_of_delta_values > total_delta_ranges[-1]:
                break

            # if yes - then break and return result as [-1]
            else:
                total_delta_ranges.append(sum_of_delta_values)

        # if list empty - just lay down value
        else:
            total_delta_ranges.append(sum_of_delta_values)

    # print(total_delta_ranges)

    return total_delta_ranges[-1]


# print(solution1(temp_list))
# print(solution2(temp_list))
#
#

time1 = time.perf_counter()
for test_list in list_db:
    solution1(test_list)
time2 = time.perf_counter()
dt = time2 - time1
print('time for sol1:', dt)

time1 = time.perf_counter()
for test_list in list_db:
    solution2(test_list)
time2 = time.perf_counter()
dt = time2 - time1
print('time for sol2:', dt)
