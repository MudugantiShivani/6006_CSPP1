# Exercise: odd

# Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.


def odd(x):
	'''
	input=number
	returns True if the number is odd and False if the number is even
	'''
	return x%2 == 1
    

def main():
    data = input()
    print(odd(int(data)))

if __name__== "__main__":
    main()
