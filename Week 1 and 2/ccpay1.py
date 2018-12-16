balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


for i in range(12):

    payment = monthlyPaymentRate * balance
    unpaid = balance - payment
    balance = unpaid + (annualInterestRate/12) * unpaid
print("Remaining balance: " + str(round(balance,2)))