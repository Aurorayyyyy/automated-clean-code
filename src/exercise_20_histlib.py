# import argparse
# from typing import Dict, Tuple


# def open_file(filename: str) -> Dict:
#     # fill up histogram
#     histogram = {}
#
#     with open(filename, 'r') as file:
#         for line in file:
#             for character in line:
#                 character = character.strip()
#                 if character == '':
#                     continue
#                 elif character in histogram:
#                     histogram[character] += 1
#                 else:
#                     histogram[character] = 1
#     return histogram


# max_key = str
# max_value = int
# min_key = str
# min_value = int
#
#
# def find_max_key_value_and_min_key_value(histogram: Dict) -> Tuple[max_key, max_value, min_key, min_value]:
#     # find max key
#     current_max_key = None
#     max_counter = 0
#     current_min_key = None
#     min_counter = 0
#     for key, value in histogram.items():
#         if current_max_key is None or value > max_counter:
#             current_max_key = key
#             max_counter = value
#         if current_min_key is None or value < min_counter:
#             current_min_key = key
#             min_counter = value
#     return current_max_key, max_counter, current_min_key, min_counter
#
#
# def main():
#     open_file("../tests/test_histlib.txt")
#     print(f'Min Key = {min_key} with count = {min_counter}')
#     print(f'Max Key = {max_key} with count = {max_counter}')
#
#
# if __name__ == '__main__':
#     main()
