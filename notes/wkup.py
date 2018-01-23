

#Greeting and payouts
#my name is John jDunn

print('Welcome to Jackpot slot machine!')
userReadRules = input("If you want to know the payouts, please press P otherwise, any other key.")
if userReadRules == "P" or userReadRules == "p":

# @John, this is where you come in again
# I'm gonna get after this!

    print("Three 7's: 35 to 1")
    print("Three BARS: 1 to 1")
    print("Three Cherries: 1 to 1")
    print("Three Diamonds: 1 to 1")
    print("Three lemons: 2 to 1")
    print("Three Bells: 3 to 1")

#Initiate user Balance
userBalance = 0
userBetAmount = 21
continuePlay = 'yes'

while (userBalance < 1 or userBalance >20) and userBetAmount != 0:
    userBalance = int(input('Please enter a starting balance not exceeding $20: '))
    if userBalance > 20:
        print('Balance amount exceeds maximum starting of $20.')
    elif userBalance == 0:
        print('Starting balance cannot be 0.')
    else:
        print("Your starting balance is " + str(userBalance))


        #my name is carlos
