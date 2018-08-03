# Write a python program to find the square root of the given number 
# using approximation method

def main():
	x=int(input())
	epsilon = 0.01
	step = 0.1
	guess = 0.0

	while abs(guess**2-x) >= epsilon:
    	if guess <= x:
       		guess += step
    	else:
        	break

	if abs(guess**2 - x) >= epsilon:
    	print('failed')
	else:
    	print('succeeded: ' + str(guess))
	#your code here

if __name__ == "__main__":
	main()