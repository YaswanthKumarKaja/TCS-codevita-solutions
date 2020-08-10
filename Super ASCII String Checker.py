'''Super ASCII String Checker
In the Byteland country a string S is said to super ascii string if and only if count of each character in the string is equal to its ascii value.

In the Byteland country ascii code of a is 1, b is 2 …z is 26.

Your task is to find out whether the given string is a super ascii string or not.

Input Format:
First line contains number of test cases T, followed by T lines, each containing a string S.

Output Format:
For each test case print Yes if the String S is super ascii, else print No

Constraints
1<=T<=100
1<=|S|<=400, S will contains only lower case alphabets ('a'-'z')
Sample Input and Output
Input

2
bba
scca

Output

Yes
No

In case 1, viz. String "bba" -
The count of character 'b' is 2. Ascii value of 'b' is also 2.
The count of character 'a' is 1. Ascii value of 'a' is also 1.
Hence string "bba" is super ascii.

'''
T=int(input())
li={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
for _ in range(T):
    a=input()
    dic={}
    flag=1
    for i in a.lower():
        if i not in li:
            continue
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    #print(dic)
    for i,j in dic.items():
        #print(ord(i)-96==j, ord(i)-96)
        if li[i]==j:
            continue
        else:
            print("No")
            flag=0
            break
    if flag==1:
        print("Yes")
#print(ord("a"))



''''T=int(input())
for T1 in range(T):
    s=input()
    p={}
    flag=0
    for j in s:
        #print(j)
        if j in p:
            p[j]+=1
        else:
            p[j]=1
    #print(s)
    if '\r' in p:
        del p['\r']
   # print(p)
    for j,k in p.items():
        if ord(j)-96!=k:
            flag=1
            break
    if flag==1:
        print("No")
    else:
        print("Yes")'''


















''''T=int(input())
for _ in range(T):
    a=input()
    dic={}
    flag=1
    for i in a.lower():
        if i=='\r':
            continue
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i,j in dic.items():
        if ord(i)-96==j:
            continue
        else:
            print("No")
            flag=0
            break
    if flag==1:
        print("Yes")'''


