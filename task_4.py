import sys

line = sys.stdin.readline().strip().split()
array_len, max_num, min_num = [int(num) for num in line]

array = [int(num) for num in sys.stdin.readline().strip().split()]

result = 0

for left_board in range(array_len):
    for right_board in range(left_board + 1, array_len + 1):
        subset = array[left_board: right_board]
        if max(subset) == max_num and min(subset) == min_num:
            result += 1
print(result)
