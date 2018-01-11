import random
import time
#
# #Greeting and payouts
print ()
print('Welcome to Jackpot slot machine!')
name = input ("What is your name?")
userReadRules = input("If you want to know the payouts, please press P otherwise, any other key.")
if userReadRules == "P" or userReadRules == "p":

# payouts print here
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

# time delay of three seconds added for reading.
time.sleep (1)

while (userBalance < 1 or userBalance >50) and userBetAmount != 0:
    userBalance = int(input('Please enter a starting balance not exceeding $50: '))
    if userBalance > 50:
        print("Whoa there cowboy! Your buy-in can't exceeds $50.")
    elif userBalance == 0:
        print("You can't play if you don't put down any money fool.")
    else:
        print()
        time.sleep (1)
        print("Your starting balance is " + str(userBalance) +" tokens")
        print()

time.sleep (1)

# Explain bets amounts (1,2 or 3) and request bet amount.
print("Okay " + name +", you can make one, two or three token bets.")
bet = int(input("How many do you want to wager?"))


while (bet < 1 or bet > 3) and bet !=0:
    if bet > 3:
        print("The max bet is 3, so we will reduce it to 3 tokens.")
        bet = 3
    elif bet == 0:
        print("Come on Jack, enter a bet between 1-3.")


print()
print ("You bet " + str(bet) + " tokens,")

# time delay of three seconds added for reading.
time.sleep (2)

print ("OMG! this is exciting")

# time delay of three seconds added for reading.
time.sleep (2)

# random number generates from 1-6. Each number matches a symbol in dictionary.
for x in range(1):
    reel_1 = (random.randint(1,6))
    reel_2 = (random.randint(1,6))
    reel_3 = (random.randint(1,6))

result = (reel_1, reel_2, reel_3)

# # remove later. Viewing results.
# print (reel_1, reel_2, reel_3)

# Dictionary to match random numbers with symbols.
symbol = {1:'Bar',
    2:'DoubleBar',
    3:'TripleBar',
    4:'Cherries',
    5:'Sevens',
    6:'Blank'}

print("and the reels return:")

# time delay of three seconds added for reading.
time.sleep (2)

print ()
print (symbol [reel_1] + "   " + symbol [reel_2] + "   " + symbol [reel_3])

print ()
# print ("Dang, you lost!")
# print ("Your new balance is " + str(userBalance - bet))


# use result variable to figure payout.
# print(result)
