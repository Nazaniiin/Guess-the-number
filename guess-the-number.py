import random

taken_guesses = 0

print 'Hello! What is your name?'

name = raw_input()
random_number = random.randint(10, 30)

print 'Well,' + name + ',I am thinking of a number between 10 and 30.'
print 'Take a guess.'

while taken_guesses < 6:
	guess = int(raw_input())
	taken_guesses += 1

	if guess < random_number:
		print 'Your guess is lower than the number I am thinking.'
	if guess > random_number:
		print 'Your guess is higher than the number I am thinking.'
	if guess == random_number:
		print 'Good job! You could guess the number in ' + str(taken_guesses) + ' tries.'
		break
		
if guess != random_number:
	print 'The number I was thinking of was ' + random_number


