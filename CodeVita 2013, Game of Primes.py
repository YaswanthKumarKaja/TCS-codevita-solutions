'''Game of Primes
In a global Mathematics contest, the contestants are told to invent some special numbers which can be built by adding the squares of its digits. Doing this perpetually, the numbers will end up to 1 or 4.
If a positive integer ends with 1, then it is called the Number of Game.

An example from above is:

13 = 1^2 + 3^2 = 1+9 = 10 (Step:1)
10 = 1^2 + 0^2 = 1+0 = 1 (Step:2), iteration ends in Step 2 since number ends with 1
Then in next round, the contestants are asked to combine their newly invented number, i.e. Number of Game with prime number.

Now, being a smart programmer, write a program to help the contestants to find out the Nth combined number within any given range, where N can be any integer.

Input Format:
Input consists of 3 integers X, Y, N, one on each line. X and Y are upper and lower limits of the range. The range is inclusive of both X and Y. Find Nth number in range [X,Y].

Line 1: X, where X is the upper limit of the range
Line 2: Y, where Y is the lower limit of the range
Line 3: N, where Nth element of the series is required

Constraints
X <= Y
X > 0
N > 0
Output Format:
Output will show the Nth element of the combined series lying in the range between X and Y.

Line 1

For Valid Input,print

U, where U is the Nth element of the combined number series lying in the range between X and Y.

Or

No number is present at this index

For Invalid Input, print

Invalid Input

Sample Input / Output
Input

1
30
3

Output

19

Input

12
33
5

Output

No number is present at this index

Input

-5
@
4

Output

Invalid Input'''


def isprime(n):
    if n == 2 or n == 3:
        return 1
    if (n % 2 != 0 and n != 1):
        if n % 6 == 1 or n % 6 == 5:
            r = int(n ** 0.5)
            for i in range(2, r + 1):
                if n % i == 0:
                    return 0
                elif i == r:
                    return 1
    else:
        return 0


def isiamthehappy(n):
    if (n == 1):
        return 1
    kajahappylist = []
    while (n != 1):
        sume = 0
        for i in str(n):
            sume += int(i) ** 2
        if sume in kajahappylist:
            return 0
        elif sume == 1:
            return 1
        else:
            n = sume
            kajahappylist.append(sume)


try:
    x = int(input())
    y = int(input())
    n = int(input())
    count = 0
    lis = []
    for i in range(x, y + 1):
        if isprime(i) == 1 and isiamthehappy(i) == 1:
            lis.append(i)
    if len(lis) < n:
        print("No number is present at this index")
    else:
        print(lis[n - 1])
except:
    print("Invalid Input")

