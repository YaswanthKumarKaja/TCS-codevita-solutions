'''Accico Equi Pairs
Ron Wesley has been bit by a three headed snake and Harry Potter is searching for a potion. The Witch promises to tell the ingredients of the medicine if Harry can find equi pair of an array. Listen to the conversation between Harry The witch to know more about equi pairs.

Conversation:-

The Witch: To find the equi pair, you must know how to find the slices first.
Harry: What is a slice?
The Witch: If Z is an array with N elements, a slice of indices (X, Y) is Z[X] + Z[X+1]…Z[Y]
Harry: How can I use it to find equi pair?
The Witch: (a, b) is an equi pair if slice of (0, a-1) = slice of (a+1, b-1) = slice of (b+1, N-1) and b>a+1 and size of array > 4

In the case that multiple equi pairs are possible, pick the one for which the middle slice contains the least number of elements.

Input Format:
An array of N integers delimited by white space

Output Format:
Print equi pair in first line in the format { a,b }
Print slices in the format { 0,a-1 }, { a+1,b-1 }, { b+1,N-1 }
OR

Print “Array does not contain any equi pair” if there are no equi pairs in the array
Constraints:
Zi >= 0 and 1 <= i <=N
size of array (N): 4 < N < 10^6
b > (a+1)
Sample Input and Output
Input

8 3 5 2 10 6 7 9 5 2

Output

Indices which form equi pair { 3,6 }
Slices are { 0,2 },{ 4,5 },{ 7,9 }
Explanation

Here index { 3,6 } is an equi pair.
Because Slice of { 0,2 } = 8+3+5=16 is equal to Slice of { 4,5 } = 10+6 = 16 and it is equal to Slice of { 7,9 } = 9+5+2 = 16

Input

6 2 6 2 3 3 1 9

Output

Array does not contain any equi pair
'''
def printAnswer(a, b):
    print(f"Indices which form equi pair {{ {a},{b} }}")
    print(f"Slices are {{ 0,{a-1} }},{{ {a+1},{b-1} }},{{ {b+1},{len(Z)-1} }}")


def solve(Z):
    assert len(Z) > 4

    sumZ = sum(Z)

    # print(Z)

    a, b = 1, len(Z) - 2
    left, right = Z[0], Z[-1]

    while b > a + 1:
        while Z[a] == Z[a + 1] == 0:
            a += 1
        while Z[b] == Z[b - 1] == 0:
            b -= 1

        middle = sumZ - left - right - Z[a] - Z[b]

        # print(a, b, left, middle, right)

        if (left > middle) or (right > middle):
            print("Array does not contain any equi pair")
            return False

        if left == middle == right:
            printAnswer(a, b)
            return True

        if left < right:
            left += Z[a]
            a += 1
        elif left > right:
            right += Z[b]
            b -= 1
        else:
            # at this point, no matter which move we make (inc a or dec b)
            #   middle will change (thanks to the while loops above)
            if left + Z[a] == middle - Z[a + 1]:
                left += Z[a]
                a += 1
            elif right + Z[b] == middle - Z[b - 1]:
                right += Z[b]
                b -= 1
            else:
                left += Z[a]
                a += 1
                right += Z[b]
                b -= 1

    print("Array does not contain any equi pair")
    return False


if __name__ == "__main__":
    Z = list(map(int, input().strip().split()))
    solve(Z)
