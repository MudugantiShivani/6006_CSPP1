'''# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number
#and returns the sum of digits of given number.
# This function takes in one number and returns one number.
'''
def sumofdigits(num_in):
    '''
    input:n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if num_in == 0:
        return 0
    return num_in%10 + sumofdigits(num_in//10)
def main():
    '''
    here the input will be a number and the output will
    be the sum of the digits of the given number
    '''
    num_in = input()
    print(sumofdigits(int(num_in)))
if __name__ == "__main__":
    main()
