class Solution:

    def __init__(self, file1, file2, file3):
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3
        self.solution()
        self.values_baked = dict()

    def solution(self):
        import json

        with (open(self.file1, 'r') as values_file,
              open(self.file2, 'r') as tests_file,
              open(self.file3, 'w') as report_file):
            values_data = json.load(values_file)
            tests_data = json.load(tests_file)

            unpacked_values = [list(i.values()) for i in values_data['values']]
            self.values_baked = {i[0]: i[1] for i in unpacked_values}

            temp_walker1 = self.magic_walking(tests_data)

            json.dump(temp_walker1, report_file)

    def magic_walking(self, obj):

        if isinstance(obj, dict):
            temp_dict = dict()
            for k, v in obj.items():
                temp_dict.update({k: self.magic_walking(v)})

            if 'id' in temp_dict.keys() and 'value' in temp_dict.keys():
                if temp_dict['id'] in self.values_baked:
                    temp_dict['value'] = self.values_baked[temp_dict['id']]

            return temp_dict

        if isinstance(obj, list):
            temp_list = []
            for pos in obj:
                temp_list.append(self.magic_walking(pos))
            return temp_list

        return obj


if __name__ == '__main__':
    filename1 = 'values.json'
    filename2 = 'tests.json'
    filename3 = 'report.json'

    # filename1 = input()
    # filename2 = input()
    # filename3 = input()

    solution = Solution(filename1, filename2, filename3)
