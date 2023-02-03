from typing import List


def calclulate_prime(n: int) -> List[int]:
    ans: List[int] = []
    for number in range(1, n + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                ans.append(number)
    return ans


def print_prime_in_col(list: List[int], print_row: int, print_col: int):
    num = 0

    for page in range(int(len(list) / (print_row * print_col)) + 1):

        print(f"=== Page{page + 1} ===")
        for row in range(num, num + print_row):
            for col in range(print_col):
                num += 1
                if (row + print_row * col) < len(list):
                    print(list[row + print_row * col], end=" ")
            print()


print_prime_in_col(calclulate_prime(769), 5, 8)
