'''
# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find
# the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with
# large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return
# value as you did in Assignment 2.
'''
def payingdebt_offinayear(balance_in, annual_interestrate):
	'''In this program we will give the input as the balance available
	and annual interest rate
	'''
	init_balance = balance_in
	moninterest_rate = annual_interestrate/12
	low_i=init_balance/12
	up_i = (init_balance * (1+ moninterest_rate)**12)/12.0
	epsilon = 0.03
	while abs(balance_in) > epsilon:
		mon_payrate = (up_i+low_i)/2
		balance_in = init_balance
		for _ in range(12):
			ans_i = balance_in - mon_payrate
			balance_in = ans_i + (ans_i * moninterest_rate)
		if balance_in > epsilon:
			low_i = mon_payrate
		elif balance_in < -epsilon:
			up_i = mon_payrate
		else:
			break
	return str(round(mon_payrate, 2))

def main():
	'''find the lowest amount to be paid to make the interest zero
	'''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest payment:", payingdebt_offinayear(data[0],data[1]))
    
if __name__== "__main__":
    main()
