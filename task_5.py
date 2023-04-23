import sys
from itertools import product


def switch_counter():
    res = telescope_count
    for comb in product(telescope_mode.values(), repeat=telescope_count):

        temp_telescope_mode = {f"{telescope_id + 1}": str(tel_mode) for telescope_id, tel_mode in enumerate(comb)}
        temp = 0
        for pair in tel_targets:
            if temp_telescope_mode[str(pair[0])] == temp_telescope_mode[str(pair[1])]:
                temp += 1
        if temp == stars_count:
            temp_res = checker(temp_telescope_mode)
            if res > temp_res:
                res = temp_res
    return res


def checker(temp_telescope_mode_: dict):
    res = 0
    for telescope_id in telescope_mode.keys():
        if temp_telescope_mode_[telescope_id] != telescope_mode[telescope_id]:
            res += 1
    return res


line = sys.stdin.readline().strip().split()

telescope_count, stars_count, mods_count = [int(params) for params in line]

telescope_mode = {f"{telescope_id + 1}": str(tel_mode) for telescope_id, tel_mode in
                  enumerate(sys.stdin.readline().strip().split())}
tel_targets = []

for star_id in range(stars_count):
    tel_targets.append([tel_id for tel_id in sys.stdin.readline().strip().split()])

print(switch_counter())
