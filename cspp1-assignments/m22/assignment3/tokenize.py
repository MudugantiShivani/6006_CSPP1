'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re

def tokenize(string, new_dict):
    '''
    here we write the function of tokenize the dictionary
    '''
    for word in string:
        if word in new_dict:
            new_dict[word] += 1
        elif word not in new_dict:
            new_dict[word] = 1
    return new_dict

def main():
    '''
    this is the main function of the program
    '''
    new_dict = {}
    line_count = int(input())
    while line_count:
        read_line = input()
        my_string = re.sub("[^ 0-9A-Za-z]", "", read_line)
        my_ans = tokenize(my_string.split(), new_dict)
        line_count -= 1
    print(my_ans)
if __name__ == '__main__':
    main()
