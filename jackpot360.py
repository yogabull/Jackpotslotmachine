import random
import time


# Greeting and payouts
print('Welcome to Jackpot slot machine!')
name = input ("What is your name? \n" )
print()

userReadRules = input("If you want to know the payouts, please press P otherwise, any other key.")
if userReadRules == "P" or userReadRules == "p":

# payouts print here
    print("Three 7's: 35 to 1")
    print("Three BARS: 5 to 1")
    print("Three Cherries: 2 to 1")
    print("Three Diamonds: 2 to 1")
    print("Three lemons: 2 to 1")
    print("Three Bells: 2 to 1")

# userBetAmount = 51 # is this needed?
continuePlay = 'yes'

# Initiate user Balance
userBalance = 0
while (userBalance < 1 or userBalance >50): #and userBalance != 0
    userBalance = int(input('Please enter a starting balance not exceeding $50: '))
    if userBalance > 50:
        print('\nBalance amount exceeds maximum starting of $50.')
    elif userBalance == 0:
        print('\nStarting balance cannot be 0.')
    else:
        print("Your starting balance is " + str(userBalance) + "\n")

startBalance = userBalance

time.sleep (1)

# explains bet limits of 1,2 or 3, and request bet amount.
print("Okay " + name +", you can make one, two or three token bets.")

# this askes for how many tokens to bet. Loop accepts only bets of 1, 2, or 3.
valid_bet = [1,2,3]
bet = int()
while bet not in valid_bet:
    bet = int(input("How many do you want to wager? "))
    if bet in valid_bet:
        print ("You bet " + str(bet) + " tokens.\n")
        userBalance = userBalance - bet
    else:
        print ("A valid bet is 1, 2 or 3 tokens, {}." .format(name) +"\n")
        # time delay of three seconds added for reading.
        time.sleep (1)

# time delay for reading.
time.sleep (1)
print ("OMG! this is exciting")
time.sleep (1)


# # //////////////////////
# # for testing: Comment out above text except the random and time modules (line 1 & 2).
# name = "Jacko"
# userBalance = 44
# startBalance = 44
# bet = 3
# # //////////////////////


# random number generates from 1-6. Each number matches a symbol in dictionary.
for x in range(1):
    reel_1 = (random.randint(1,6))
    reel_2 = (random.randint(1,6))
    reel_3 = (random.randint(1,6))

result = (reel_1, reel_2, reel_3)


# # //////////////////////
# # for testing three matching reels)
# test = 1
# reel_1 = test
# reel_2 = test
# reel_3 = test
# result = (reel_1, reel_2, reel_3)
# # //////////////////////


# Dictionary to match random numbers with symbols.
symbol = {1:'Seven',
    2:'Triple-Bar',
    3:'Cherries',
    4:'Diamonds',
    5:'Lemons',
    6:'Bells'}

print("and the reels return: \n")

# time delay of one second added for reading.
time.sleep (1)

# shows reel results
print (symbol [reel_1] + "   " + symbol [reel_2] + "   " + symbol [reel_3] +"\n")
time.sleep (1)

if  [reel_1] ==  [reel_2] and  [reel_2] == [reel_3]:
    print('Jackpot! Congratulations, you won!')
    if result == (1,1,1):
        userBalance = userBalance + bet * 35 # ("Three 7's: 35 to 1")
    elif result == (2,2,2):
        userBalance = userBalance + bet * 5 # ("Three BARS: 5 to 1")
    elif result == (3,3,3):
        userBalance = userBalance + bet * 2 # ("Three Cherries: 2 to 1")
    elif result == (4,4,4):
        userBalance = userBalance + bet * 2 # ("Three Diamonds: 2 to 1")
    elif result == (5,5,5):
        userBalance = userBalance + bet * 2 # ("Three lemons: 2 to 1")
    elif result == (6,6,6):
        userBalance = userBalance + bet * 2 # ("Three Bells: 2 to 1")
# If two symbols match, this code code returns 1 to 1 winnings
elif ([reel_1] == [reel_2]) or ([reel_2] == [reel_3] or [reel_1] == [reel_3]):
    print ("No Jackpot, but you don't lose.")
    userBalance == userBalance + bet * 1
    print ("You still have " + str(userBalance) + " tokens. \n")
else:
    print('You suck! Try again fool.')
    userBalance = userBalance - bet
print ("Your new balance is " + str(userBalance) +" tokens.\n")



# # //////////////////////
# # for testing balances
# print (startBalance)
# print (userBalance)
# print ()
# # //////////////////////


# this block compares winnings with the starting balance, and needs to prompt for playing again.
print (name +" you started with " + str(startBalance) + " tokens.")

if startBalance < userBalance:
    print ("You are ahead " + str(userBalance - startBalance) + " tokens. Let's win some more!\n")
elif startBalance == userBalance:
    print ("Not bad, but you gotta bet big to win big " + str(name) + "!\n")
else:
    print ("You are down " + str(startBalance - userBalance) + " tokens, but I know you can win it back!\n")

print ("need code to loop back into the betting cycle.\n")
