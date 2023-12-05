# An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.
# The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).
# Derive function abundantNumber(num)/abundant_number(num) which returns true/True/.true. if num is abundant, false/False/.false. if not.


def abundant_number(num):
    # O(sqrt(num))
    sum_x = 1
    int_sqrt = int(num ** 0.5)
    for i in range(2, int_sqrt + 1):
        if num % i == 0:
            sum_x += i + num // i
    if int_sqrt ** 2 == num:
        sum_x -= int_sqrt
    return sum_x > num




