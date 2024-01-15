"""

打印区间内所有的素数
(不熟悉)

"""


def is_prime(number):
    if number in (1, 2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True

def dayin_sushu(begin,end):
    for number in range(begin, end + 1):
        if is_prime(number):
            print(f"{number}is a prime")


print(dayin_sushu(1,4))
