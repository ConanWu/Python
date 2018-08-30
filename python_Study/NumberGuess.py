import random, easygui

secret = random.randint(1, 100)
guess = 0
tries = 0

easygui.msgbox("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
easygui.msgbox("It is a number from 1 to 99. I'll give you 6 tries. ")

while guess != secret and tries < 6:
    guess = easygui.integerbox("what's your guess? ")
    if guess < secret:
        easygui.msgbox("Too low!")
    elif guess > secret:
        easygui.msgbox("Too high! ")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("Avast! You got it! Found my secret, you did it!")
else:
    easygui.msgbox("No more guess! Better luck next time")
    #print("The secret number was", secret)
