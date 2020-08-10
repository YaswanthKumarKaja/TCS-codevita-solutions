'''Saving for a Rainy Day
By nature, an average Indian believes in saving money. Some reports suggest that an average Indian manages to save approximately 30+% of his salary. Dhaniram is one such hard working fellow. With a view of future expenses, Dhaniram resolves to save a certain amount in order to meet his cash flow demands in the future.

Consider the following example.

Dhaniram wants to buy a TV. He needs to pay Rs 2000/- per month for 12 installments to own the TV. If, let’s say, he gets 4% interest per annum on his savings bank account, then Dhaniram will need to deposit a certain amount in the bank today, such that he is able to withdraw Rs 2000/- per month for the next 12 months without requiring any additional deposits throughout.

Your task is to find out how much Dhaniram should deposit today so that he gets assured cash flows for a fixed period in the future, given the rate of interest at which his money will grow during this period.

Input Format:
First line contains k, the number of inputs. The following k lines have:

First line contains desired cash flow M
Second line contains period in months denoted by T
Third line contains rate per annum R expressed in percentage at which deposited amount will grow
Output Format:
Print total amount of money to be deposited now rounded off to the nearest integer

Constraints:
M > 0
T > 0
R >= 0
Calculation should be done upto 11-digit precision

Example
Input:

k = 3

500
3
12

6000
3
5.9

500
2
0
Output:

1470
17824
1000'''
import math
test=int(input())
for i in range(test):
    mp=int(input())
    m=int(input())
    r=float(input())
    #if(mp<=0 or m<=0 or r<0):
     #   continue
    #else:
    if 1:
        ra=mp
        while(m):
            amount=ra/(1+(r/1200.0))
            intrest=ra-amount
            ra=ra+(mp-intrest)
            m-=1
        ra=ra-mp
        final=math.ceil(ra-0.5)
        if(final>ra):
            final=math.ceil(ra)
        else:
            final=math.floor(ra)
        print(final)