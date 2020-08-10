'''Cyclic Palindrome
A string is said to be palindrome, if it reads the same from both the ends. Given a string S, you are allowed to perform cyclic shifts. More formally, you can pick any one character from any end (head or tail) and you can append that character at the other end. For example, if the string is abc, then if we do a shift using the character at head position then the string becomes bca. Similarly, if we do the shift using the character at the tail then the input string becomes cab. Your task is to find out the minimum number of shifts needed to make the given string, a palindrome.

In case, we can’t convert the string to palindrome then print -1.

Input Format
First line starts with T i.e. number of test cases, and then T lines will follow each containing a string S.

Output Format
Print the minimum number of cyclic shifts for each string if it can be made a palindrome, else -1.

Constraints
1<=T<=100
1<=|S|<=300, S will contains only lower case alphabets a-z.

Sample Input and Output
Input

4
abbb
aaabb
aabb
abc
Output

-1
1
1
-1
Explanation:

For Test Case 2 (aaabb):

Shift the character at the tail to the head and the result will be baaab, which is a palindrome. This is an operation which requires minimum number of shifts to make the given string a palindrome.

For Test Case 3 (aabb):

One way to convert the given string to palindrome is, shift the character at the head to the tail, and the result will be abba, which is a palindrome. Another way is to shift the character at the tail to the head, and the result will be baab, which is also a palindrome. Both require only one shift.

'''
def ispal(n):
    for i in range(len(n) // 2):
        if n[i] != n[- i - 1]:
            return 0
    return 1


def leftshift(a):
    return a[1:] + a[0]
def rightshift(a):
    return a[-1] + a[:-1]


def shift(a):
    left, right = a, a
    for i in range( len(a) // 2):
        left = leftshift(left)
        right = rightshift(right)
        if (ispal(left) or ispal(right)):
            return i+1
    return -1


test = int(input())
for i in range(test):
    a = input().lower()
    if ispal(a)==1:
        print(0)
    else:
        print(shift(a))




'''def ls(s):
    return s[1: ]+s[0]
def rs(s):
    return s[-1]+s[:-1]
def isp(s):
    for i in range((len(s)//2)+len(s)%2):
        if s[i]!=s[-1-i]:
            return 0
    return 1


T=int(input())
for T1 in range(T):
    s=input()
    s_r=s
    s_l=s
    i=0
    count=0
    if isp(s)==1:
        print(0)
    else:
        #print((len(s)//2)+(len(s)%2))
        for i in range((len(s)//2)+(len(s)%2)):
            #print(count)
            count+=1
            #print(s_l)
            s_l=ls(s_l)
            #print(s_l)
            if isp(s_l)==1:
                print(count)
                break
            #print(s_r)
            s_r=rs(s_r)
            #print(s_r)
            if isp(s_r)==1:
                print(count)
                break
            if i==(len(s)//2)+(len(s)%2)-1:
                 print(-1)'''
