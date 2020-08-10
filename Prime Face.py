'''Accept a number N up to 5 digits long in the positional numeral system formed by symbols 0, 1, ... 9, A, ..., Z. Also, accept another symbol S other than zero.

Considering N to be represented in the least base possible between 2 and 36, identify the smallest prime number greater than  N that contains at least one occurrence of S in it in base S + 1.

(Refer example section for a better understanding). Prime number should be identified with respect to Base 10 i.e. a regular prime number.

Constraints
Length of N <= 5
Max Base = 36
Face values for symbols:
Symbol => Value in base 10

0 => 0

1 => 1

2 => 2

….

9 => 9

A => 10

B => 11

….

Z => 35

Input Format
First line contains T, the number of test cases. Each test case contains:
One line containing two integers, N and S separated with space.
Output
Print the smallest prime number greater than or equal to N that contains at least one occurrence of S in it, in base S + 1.
Example Test Case 1
2
10 B
ZZ Z
Output
B
11Z
Explanation 1
The least possible base for N is 2 and its value in that base is 2. We want the smallest prime number in base 12 (1 more than the face value of B, 11) that contains symbol B and is greater than or equal to 2. The first few numbers in ascending order in base 12 containing face value B are B (value 11), 1B (value 1 * 12 + 11 = 23), 2B (value 2 * 12 + 11 = 35): of these the smallest number that is prime is 11, which is greater than N. Hence, the output is B.

Explanation 2
The least possible base for N is 36 and its value in that base is 35 * 36 ^1 + 35 = 1295. The first few numbers in ascending order in base 36 (1 more than the face value of Z, 35) containing face value Z and greater than N are 10Z (1 * 36^2 + 0*36^1 + 35 = 1331, non-prime), 11Z (1 * 36^2 + 1 * 36^1 + 35 = 1367, a prime). Hence, the output is 11Z.'''


def get_value(k):  # converting a string to decimal
    value = ord(k) - ord('0')

    if value > 9:
        value = 10 + ord(k) - ord('A')

    return value


def get_in_base_decimal_value(N, base):  # getting N value in given base
    value = 0
    N = str(N)
    for index in range(len(N)):
        power = len(N) - index - 1
        value = value + (get_value(N[index]) * (base ** (power)))

    return value


def get_digit(num):  # get the value of the current digit
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit = digits[num]
    return digit


def isprime(num):  # naive algorithm for finding prime numbers
    if num in [2, 3, 5, 7]:
        return True
    if num % 2 == 0:
        return False

    i = 2
    while (i ** 2 <= num):
        if num % i == 0:
            return False
        i += 1
    return True


def construct_in_base(num, base):
    # construct a srting with given num, in given base
    # must return string

    value = ''
    temp = num
    power = 9

    while temp > 0:
        value = value + get_digit(temp // (base ** power))
        temp = temp % (base ** power)
        power -= 1

    while value[0] == '0':
        value = value[1:]

    return value


T = int(input())

for case in range(T):
    N, B = input().split()

    max_digit = '0'
    for digit in N:
        if get_value(digit) > get_value(max_digit):
            max_digit = digit

    min_base = get_value(max_digit) + 1  # first get the minimum base

    N_in_base = get_in_base_decimal_value(N, min_base)
    # then get N value if it was represented in that base

    desired_base = get_value(B) + 1

    start_number = N_in_base + 1  # starting point, integer data type

    while (B not in construct_in_base(start_number, desired_base)) or (not isprime(start_number)):
        start_number += 1

    ans = construct_in_base(start_number, desired_base)
    print(ans)