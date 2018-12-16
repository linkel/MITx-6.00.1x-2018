balance = 4773
annualInterestRate = 0.2

guess = 10
testbalance = balance
while True:
    payment = guess
    testbalance = balance
    for i in range(12):
        unpaid = testbalance - payment
        testbalance = unpaid + (annualInterestRate/12) * unpaid
    if testbalance <= 0:
        break
    guess = guess + 10
print("Lowest payment: " + str(guess))
