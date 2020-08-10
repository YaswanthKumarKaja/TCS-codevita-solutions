'''Exchange Digits
Compute nearest larger number by interchanging digits updated.

Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not possible print -1

Constraints
1 <= a,b <= 10000000

Input Format
2 numbers, a and b, separated by space.

Output
A single number, greater than b

If not possible, print -1.

Test Case
Input

459 500

Output

549

Input

645757 457765

Output

465577

Input

5964 9984

Output

-1'''
from itertools import permutations
n1,n2 = map( int,input().split(" "))
ln1=str(n1)
if n1>=1 and n1<=1e7 and n2>=1 and n2<=1e7:
    flag = 0
    n1 = list(str(n1))
    per = sorted(permutations(n1))
    for i in list(per):
        string = " "
        if (i[0]!='0'):
            for j in i:
                string+=j
            if int(string) > n2:
                flag = 1
                break
if flag == 1:
    print(int(string))
else:
    print(-1)