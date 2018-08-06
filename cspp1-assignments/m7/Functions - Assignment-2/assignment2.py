# Assignment-2 - Paying Debt off in a Year
# Now write a program that calculates the minimum fixed monthly payment
#needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does
#not change each month, but instead is a constant amount that will be
# paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# The program should print out one line: the lowest monthly payment
#that will pay off all debt in under 1 year, for example:
# Lowest Payment: 180
# Assume that the interest is compounded monthly according to
#the balance at the end of the month (after the payment for that month is
# made).

def payingdebt_offinayear(Previous_balance, Annual_interestrate):
    '''
    Here we will give the previous balance and annual interest rate to
    find the minimum amount
    '''
    Minimumfixed_monthlypayment = 10
    temp = Previous_balance
    flag = 1
    mon_cnt = 0
    monthly_interestrate = (Annual_interestrate) / 12.0
    if Previous_balance < 0:
        flag = 0
        Minimumfixed_monthlypayment = 0
    while flag:
        mon_cnt += 1
        monthly_unpaidbalance = (Previous_balance) - (Minimumfixed_monthlypayment)
        Previous_balance = (monthly_unpaidbalance) + (monthly_interestrate * monthly_unpaidbalance)
        if Previous_balance < 0:
            flag = 0
        if mon_cnt == 12 and flag != 0:
            Minimumfixed_monthlypayment += 10
            mon_cnt = 0
            Previous_balance = temp
    return Minimumfixed_monthlypayment
def main():
    '''
    this function takes the in puts and calls payingdebt_offinayear
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:",payingdebt_offinayear(data[0],data[1]))
    
if __name__ == "__main__":
    main()
    