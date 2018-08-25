'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read the string and replace all the specisl characters with space
    '''
    string = input()
    for char_i in string:
        if char_i in('!', '@', '#', '$', '%', '^', '&', '*', '.', ' '):
        	string = string.replace(char_i, "")
        	
    print(string)
if __name__ == "__main__":
    main()
