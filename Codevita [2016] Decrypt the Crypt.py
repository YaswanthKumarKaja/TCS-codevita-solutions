'''Decrypt the Crypt
Walter uses multiple applications at his workplace. He was assigned a unique password of variable lengths for each application (maximum length being 10). The only common factor among them was that all the passwords were a combination of 10 distinct characters. Walter created an algorithm to encrypt these passwords and wrote the codes on his desk to avoid a situation in which he would not be able to recollect a password.

Given as an input, is an encoded password and a list of 10 unique characters. Write a program that obtains the password by reverting the algorithm used by Walter.

Algorithm used by Walter to encode his password is as follows:

Walter observes all his passwords and lists down every distinct character. He assigns an index value to each character from 0 to 9. (Note: This list will be provided as an input to the program). This list MUST contain 10 DISTINCT characters.
He then replaces every character in the password with the corresponding index value to convert the password to a 10 digit numeric value.
The leftmost digit in this number sequence is noted; let’s say ‘A’. Now, starting from the leftmost position, every digit in the number is added to the digit on its right. The last digit in the sequence is added to ‘A’.
Step 3 provides new sequences of numbers. He then scans through each of the summations and if any of the summation results in a value greater than 9, it is subtracted by 10, and its position is noted (Say B).
He then lists every digit from 0 to 9 separated by | character and prepends each digit with its position in the sequence as noted in ‘B’. The resulting sequence after this step is saved (Say C).
The encoded password would therefore be
< value_of_C >||< contents_of_array_B > < Value_of_A >
Decrypt the encrypted password that has been created by Walter using the above algorithm to compute the actual password!

Print -1 if there is any error in the inputs.

Input Format:
First line contains T, the number of test cases. The following T lines contain:

First line contains the encoded password as it should be according to Walter’s algorithm
Second line contains 10 unique characters
Output Format:
Obtained password by reverting the algorithm. Print -1 if there is any error in the inputs.

Constraints:
Second line of input MUST contain 10 DISTINCT characters.
Encoded password should be in format
< value_of_C >||< contents_of_array_B >< value_of_A >
Sample Input & Output
Input:

0|1|2|43|14|5|6|7|308|29||0149
*Acf$Zd&T@
Output:

@@Z$$
Explanation:

The following are the steps used to encrypt the password. Your task is to reverse the logic and decrypt the encrypted string provided as input, and get back the clear-text password.

Consider input characters and its position
Input character list:  *Acf$Zd&T@
Position:              0123456789
(Note: The character list will not contain more than 10 characters and each character must be unique)

Now replace the characters in the password with the position value of the respective character as defined in step 1, to convert the password into a numeric value.
Password:      @@Z$$
Numeric value: 99544
(Note: Remember leftmost value (Say A) = 9)

Starting from the left most position, add each digit to the digit on its right. Add the last digit with the first digit in the sequence
Numeric value of password:  9  9  5  4  4
Addition:                  18 14  9  8 13
For each addition result equal to or greater than 10, subtract it by 10 and note its position.
Additive step output:  18  14  9   8  13
Selective subtraction: 8   4   9   8   3
Numeric value:         0   1   2   3   4
(Note: Remember the selective subtraction step positions obtained (Say B) = 014)

The password will follow the following format
Format:  0|1|2|3|4|5|6|7|8|9
Now, each number in this format is pre-appended with the positions of the occurrence of the respective number in the output obtained in selective subtraction step of Step 4.
Encrypted password:  0|1|2|43|14|5|6|7|038|29
(Note: Say C = 0|1|2|43|14|5|6|7|038|29)

The final encrypted password will be of the following format to account for the calculations performed in generating the encrypted password
Encrypted password (format): <C>||<B><A>
Encrypted password:          0|1|2|43|14|5|6|7|308|29||0149
Input:

0|1|2|43|14|5|6|7|308|29||0149
*Acf$Zd&T
Output:

-1
Explanation

Second line of input contains 9 characters only hence prints -1

'''
def solve(enc, charset):
    # split into A, B, C (reverse step 7)
    C, AB = enc.split("||")
    A, B = AB[-1], AB[:-1]

    assert len(A) > 0
    assert len(C) > 0

    # (reverse step 6, 5)

    # d will contain the additive step output as a dictionary {k: v} where k is the position and v is the value at that position
    d = {}

    for item in C.split("|"):
        v, positions = item[-1], item[:-1]
        for p in positions:
            d[int(p)] = int(v)

    # reconstruct the additive step output as a list now (reverse step 4)
    ssPositions = set(map(int, B))  # selective subtraction positions
    for p in ssPositions:
        d[int(p)] += 10

    addition = [d[i] for i in range(len(d))]

    # from here, we reconstruct the list of numeric values (reverse step 3)
    addition[-1] -= int(A)

    for i in range(len(addition) - 2, -1, -1):
        addition[i] -= addition[i + 1]

    # reconstruct the password as a list of characters (reverse step 2)
    password = [charset[i] for i in addition]

    # return the password as a string (reverse step 1)
    return "".join(password)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        try:
            enc = input().strip()
            charset = input().strip()

            assert len(set(charset)) == 10

            # solve also throws an assertion error if the password is not
            # encoded correctly
            print(solve(enc, charset))

        except Exception as e:
            print("-1")

