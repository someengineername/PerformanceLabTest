class Solution:

    def __init__(self, file1, file2, file3):
        self._file1 = file1
        self._file2 = file2
        self._file3 = file3
        self._values_baked = dict()
        self.solution()

    def solution(self):
        import json

        with (open(self._file1, 'r') as values_file,
              open(self._file2, 'r') as tests_file,
              open(self._file3, 'w') as report_file):
            values_data = json.load(values_file)
            tests_data = json.load(tests_file)

            unpacked_values = [list(i.values()) for i in values_data['values']]

            # prepare values from values_file with guideline of {id:value...id:value} to easy comparison down later
            self.values_baked = {a: b for a, b in unpacked_values}

            temp_walker1 = self.recursive_reconstruction(tests_data)

            try:
                json.dump(temp_walker1, report_file)
            except Exception as e:
                print('Error', e, 'has occurred')

    def recursive_reconstruction(self, obj):

        # 1st recursive end - obj is dict, so traverse by key:value
        if isinstance(obj, dict):
            temp_dict = dict()
            for k, v in obj.items():
                temp_dict.update({k: self.recursive_reconstruction(v)})

            # reconstruction process itself
            if 'id' in temp_dict.keys() and 'value' in temp_dict.keys():
                if temp_dict['id'] in self.values_baked:
                    temp_dict['value'] = self.values_baked[temp_dict['id']]

            return temp_dict

        # 2nd recursive end - obj is list, so traverse by elements
        if isinstance(obj, list):
            temp_list = []
            for pos in obj:
                temp_list.append(self.recursive_reconstruction(pos))
            return temp_list

        # Base end (obj is non-list & non-dict)
        return obj


if __name__ == '__main__':
    # filename1 = 'values.json'
    # filename2 = 'tests.json'
    # filename3 = 'report.json'

    filename1 = input()
    filename2 = input()
    filename3 = input()

    solution = Solution(filename1, filename2, filename3)
