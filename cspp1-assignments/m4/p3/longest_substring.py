'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    """
    we have to print the longest substring which is in sequence from the given string
    """
    s_i = input()
    max_sub = []
    for i in range(len(s_i)):
        sub_str = s_i[i]
        count_var = 0
        while i+1 < len(s_i) and s_i[i] <= s_i[i+1]:
            count_var += 1
            i += 1
            sub_str += s_i[i]
        if len(sub_str) > len(max_sub):
            max_sub = sub_str
    print(max_sub)
    # the input string is in s
    # remove pass and start your code here
if __name__ == "__main__":
    main()
