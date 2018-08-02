'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    """we print number of times bob has occured in the given string
    """
    s_i = input()
    len_m = len(s_i)
    count_var=0
    for index in range(len_m-2):
        if s_i[index] == "b" and s_i[index+1] == "o" and s_i[index+2] == "b":
            count_var+=1
    print(count_var)
    # the input string is in s
    # remove pass and start your code here
if __name__== "__main__":
    main()
