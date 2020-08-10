'''Distribute Books
For enhancing the book reading, school distributed story books to students as part of the Children’s day celebrations.

To increase the reading habit, the class teacher decided to exchange the books every weeks so that everyone will have a different book to read. She wants to know how many possible exchanges are possible.

If they have 4 books and students, the possible exchanges are 9. Bi is the book of i-th student and after the exchange he should get a different book, other than Bi.

B1 B2 B3 B4 - first state, before exchange of the books
B2 B1 B4 B3
B2 B3 B4 B1
B2 B4 B1 B3
B3 B1 B4 B2
B3 B4 B1 B2
B3 B4 B2 B1
B4 B1 B2 B3
B4 B3 B1 B2
B4 B3 B2 B1
Find the number of possible exchanges, if the books are exchanged so that every student will receive a different book.

Constraints
1<= N <= 1000000

Input Format
Input contains one line with N, indicates the number of books and number of students.

Output
Output the answer modulo 1000000007.

Test Case Explanation
Example 1 Input

4

Output
9

'''
n=int(input())

f=[0,1]

i=3

if n==1:

    print(f[n-1])

elif n==2:

    print(f[n-1])

else:

    while i<(n+1):

        f.append(((i-1)*(f[0]+f[1]))%1000000007)

        f.pop(0)

        i=i+1
if(n!=1 and n!=2):
    print(f[1])