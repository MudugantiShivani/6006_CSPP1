'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def main():
    '''
    here we will take a string and remove all special characters from it and print the string
    '''
    string = input()
    for char in string:
        if char in('!', '@', '#', '$', '%', '^', '&', '*', '.', ' ', '(', ')'):
            string = string.replace(char, "")
    print(string)
if __name__ == '__main__':
    main()
