import sys

line = sys.stdin.readline().strip().split()
row_num, column_num, requests_count = [int(num) for num in line]

matrix = [[0 for _ in range(column_num)] for _ in range(row_num)]

requests_list = []

for _ in range(requests_count):
    line = sys.stdin.readline().strip().split()
    req = [int(num) for num in line]
    if req[0] == 1:
        left_border = req[1]
        right_border = req[2]
        num_tu_sum = req[3]
        for row_pos in range(row_num):
            for column_pos in range(left_border - 1, right_border):
                matrix[row_pos][column_pos] += num_tu_sum

    elif req[0] == 2:
        row_pos = req[1] - 1
        num_to_swipe = req[2]
        for column_pos_ in range(column_num):
            matrix[row_pos][column_pos_] = num_to_swipe
    else:
        row_pos = req[1] - 1
        column_pos = req[2] - 1
        print(matrix[row_pos][column_pos])
