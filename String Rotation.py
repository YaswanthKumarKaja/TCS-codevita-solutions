'''String Rotation
Rotate a given String in the specified direction by specified magnitude.

After each rotation make a note of the first character of the rotated String, After all rotation are performed the accumulated first character as noted previously will form another string, say FIRSTCHARSTRING.

Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.

If yes print YES otherwise NO.

Input
The first line contains the original string s.
The second line contains a single integer q.
The ith line of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.
Output
YES or NO

Constraints
1 <= Length of original string <= 30
1<= q <= 10
Sample Input & Output
Input

carrace
3
L 2
R 2
L 3

Output

NO

Explanation

After applying all the rotations the FIRSTCHARSTRING string will be rcr which is not anagram of any sub string of original string carrace


'''
def lo(s,n):
    return s[n: ]+s[ :n]
def up(s,n):
    return s[-n: ]+s[ :-n]
def isana(s2,k):
    for i in range(len(k)):
        k=lo(k,1)
        if k in s2:
            return 1
    return 0

s=input()
n=int(input())
s2=s
k=''
for i in range(n):
    s1=input().split()
    if s1[0].upper()=="L":
        s=lo(s,int(s1[1]))
        k+=s[0]
    else:
        s=up(s,int(s1[1]))
        k+=s[0]
if isana(s2,k)==1:
    print("YES")
else:
    print("NO")