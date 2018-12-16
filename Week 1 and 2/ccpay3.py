balance = 320000
annualInterestRate = 0.2


monthlyIR = annualInterestRate / 12.0
lowerbound = balance / 12
upperbound = (balance * (1 + monthlyIR)**12) / 12.0


testbalance = balance

while True:
    guess = (lowerbound + upperbound) / 2.0
    payment = guess
    testbalance = balance
    for i in range(12):
        unpaid = testbalance - payment
        testbalance = unpaid + (annualInterestRate/12) * unpaid
    if round(testbalance, 6) == 0.000000:
        break
    if testbalance > 0:
        lowerbound = guess
    if testbalance < 0:
        upperbound = guess
print("Lowest payment: " + str(round(guess, 2)))
