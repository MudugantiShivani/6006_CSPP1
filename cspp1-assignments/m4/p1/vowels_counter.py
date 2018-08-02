"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained 
in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
"""
def main():
    """
    we have to find the number of vowles in the give string
    """
    s_int = input()
    
    ss_int = s_int.lower()
    count_i = 0
    for char_i in ss_int:
        if char_i in('a', 'e', 'i', 'o', 'u'):
            count_i += 1
    print(count_i)
    # the input string is in s
    # remove pass and start your code here
    

if __name__ == "__main__":
    main()
