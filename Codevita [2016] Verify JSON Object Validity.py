'''Verify JSON Object validity
A JSON object is a key-value pair data structure that is enclosed within { }. A sample JSON object would look like

{
"key1":"value1",
"key2":"value2",
"key3": {
"key4":"value4",
"key5":"value5"},
"key6":"value6",
"key7":[
{
"key8":"value8"
}]
}
Given a JSON object, ignore the literal values of the object and check whether the distinguishing characters and notation of the object are valid to determine if the JSON object is valid or not.

Note:

Key3 points to another JSON object (Concept of nesting of JSON objects).
Key7 points to an array of JSON objects.
You may wish to refer JSON.org to get a more formal description of JSON grammar.
Input Format
First line contains a pattern of JSON without any literal
Output Format:
Print 1 if pattern is valid, -1 otherwise.

Constraints:
A JSON object should start with { and ends with a }.
The key and value should be separated by a :.
A , suggests an additional JSON property.
An array only consists of JSON objects. It cannot contain a “key”:“value” pair by itself.
Sample Input & Output
Input
{:[{},{}]}

Output
1

Explanation

{
"Key": [{
"Key": "Value"
}, {
"Key": "Value"
}]
}
Pattern is following all constraints hence prints 1

Input
{:{[]},{}}

Output
-1

Explanation

{
"Key": {
[
"Key": "Value"
]
},
{
"Key": "Value"
}
}
Constraint 4 “An array only consists of JSON objects. It cannot contain a “key”:“value” pair by itself.” not followed here, so it’s a invalid pattern, hence prints -1

'''


def get_end_index(word, index, bracket):
    corresponding = None
    if bracket == '[':
        corresponding = ']'
    elif bracket == '{':
        corresponding = '}'

    num_open = 1
    num_close = 0
    for i in range(index + 1, len(word)):
        if word[i] == bracket:
            num_open += 1
        if word[i] == corresponding:
            num_close += 1
        if num_open == num_close:
            return i
    return -1


def verify(word, start, end):
    # print('verifying', word[start:end])
    if word[start:end] in ['{}', '[]']:
        return True
    if end - start <= 1:
        return False
    if (word[start] + word[end - 1] not in ['{}', '[]']):
        return False
    index = start + 1
    while index < end - 1:
        if word[index] == ',':
            if word[index - 1] not in ('}', ']', ':'):
                return False
            index += 1
        elif word[index] == ':':
            if word[index - 1] != ',' and word[index - 1] != '{':
                return False
            else:
                index += 1
        elif word[index] in ('{', '['):
            if word[index] == '[' and word[index - 1] == '{':
                return False
            end_index = get_end_index(word, index, word[index])
            if end_index == -1:
                return False
            ans = verify(word, index, end_index + 1)
            if not ans:
                return False
            index = end_index + 1
        else:
            print(index, end)
            return False
    return True


word = input().strip()

if '{' not in word:
    print(-1)
    exit()

ans = verify(word, 0, len(word))
# print(word)
if ans:
    print(1)
else:
    print(-1)
