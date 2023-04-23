from itertools import product
import sys

line = sys.stdin.readline().strip().split()

array_len, k_num = [int(params) for params in line]

array_a = [int(num) for num in sys.stdin.readline().strip().split()]
array_b = [int(num) for num in sys.stdin.readline().strip().split()]

res = False

for bin_comb in product([0, 1], repeat=array_len):
    res_array = []
    for pos_id, bin_kof in enumerate(bin_comb):
        if bin_kof == 1:
            res_array.append(array_a[pos_id])
        else:
            res_array.append(array_b[pos_id])
    checker = 0
    for array_index in range(0, array_len - 1):
        if abs(res_array[array_index] - res_array[array_index + 1]) > k_num:
            continue
        else:
            checker += 1
    if checker == array_len - 1:
        res = True
        break

if res:
    print('YES')
else:
    print('NO')
