'''# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number
#and returns the sum of digits of given number.
# This function takes in one number and returns one number.
'''
def sumofdigits(n):
    '''
    input:n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n == 0:
        return 0
    return n%10 + sumofdigits(n//10)
def main():
    '''
    here the input will be a number and the output will
    be the sum of the digits of the given number
    '''
    n = input()
    print(sumofdigits(int(n)))
if __name__ == "__main__":
    main()