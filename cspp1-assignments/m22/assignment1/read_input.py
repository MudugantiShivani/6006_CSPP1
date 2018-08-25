'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    Here we read the given file and print the file
    '''
    file_input = input()
    for data in  range(int(file_input)):
        data = input()
        print(data)
if __name__ == '__main__':
    main()
