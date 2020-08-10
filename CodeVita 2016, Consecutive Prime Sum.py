'''Some prime numbers can be expressed as Sum of other consecutive prime numbers.
For example

5 = 2 + 3
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.

Write code to find out number of prime numbers that satisfy the above mentioned property in a given range.

Input Format:
First line of input contains k - the number of inputs
The next k lines contains a number N.

Output Format:
Print the total number of all such prime numbers which are less than or equal to N.

Example:
Input:
k = 2

N = 20

N = 15
Output:
2 (there are 2 such numbers: 5 and 17)
1

'''


def isprime(n):
    if n == 2 or n == 3 or n == 5:
        return 1  # Function to find prime or not
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return 0
    elif n % 6 == 5 or n % 6 == 1:
        r = int(n ** 0.5)
        for i in range(2, r + 1):
            if n % i == 0:
                return 0
            elif i == r:
                return 1
    else:
        return 0


T = int(input())
for T1 in range(T):
    n = int(input())
    li = []
    for i in range(3, n + 1):
        if isprime(i) == 1:
            li.append(i)
    sume = 2
    count = 0
    for i in range(len(li)):
        sume += li[i]
        if sume in li:
            count += 1
    print(count)


