'''Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest lexicographical string that can be made out of this new order. Can you help him?

You are given a string P that denotes the new order of letters in the English dictionary.

You need to print the smallest lexicographic string made by rearranging all the letters of the given string S.

Constraints
1 <= T <= 1000
Length (P) = 26
1 <= length (S) <= 100
All characters in the string S, P are in lowercase

Input Format
The first line contains number of test cases T
The second line has the string P
The third line has the string S
Output
Print a single string in a new line for every test case giving the result
Example Input
2
polikujmnhytgbvfredcxswqaz
abcd
qwryupcsfoghjkldezxvbintma
ativedoc
Output
bdca
codevita
Explanation
The transformed smallest lexicographical strings are in order they would be if order of letters are changed to string P

'''

T = int(input())

for case in range(T):
    P = input()
    S = input()

    order = {}

    for i in range(len(P)):
        order[P[i]] = i  # getting order as per the new dictionary

    ans = list(S)

    ans.sort(key=lambda x: order[x])  # sorting as per the new order

    ans = ''.join(ans)  # converting back to a string
    print(ans)  # printing the string'''
'''T=int(input())
for T1 in range(T):
    s=[x for x in input()]
    p=[x for x in input()]
    for i in s:
        while(i in p):
            print(i,end="")
            p.remove(i)
    print("")'''

'''test = int(input())
for i in range(test):
    p = input()
    p = list(p)
    a = input()
    a = list(a)
    for i in range(len(p)):
        while p[i] in a:
            print(p[i], end="")
            a.remove(p[i])

    print()'''
