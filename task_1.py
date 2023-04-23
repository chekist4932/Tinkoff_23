import sys


def mess_checker(crypt_mess: str):
    res = "NO"
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(crypt_mess) - 9):
        flag = 1
        _slice = crypt_mess[i:i + 10]
        for num in numbers:
            if _slice.count(num) != 1 and _slice.count(num) != 0:
                flag = 0
                break
        if flag == 1:
            res = "YES"
            break
    return res


crypt = sys.stdin.readline().strip()

print(mess_checker(crypt))
