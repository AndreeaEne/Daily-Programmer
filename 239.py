# Back in middle school, I had a peculiar way of dealing with super boring classes. I would take my handy pocket calculator and play a "Game of Threes". Here's how you play it:
# First, you mash in a random large number to start with. Then, repeatedly do the following:
# If the number is divisible by 3, divide it by 3.
# If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
# The game stops when you reach "1".
# While the game was originally a race against myself in order to hone quick math reflexes, it also poses an opportunity for some interesting programming challenges. Today, the challenge is to create a program that "plays" the Game of Threes.


def add(steps, nr):
	steps.append(nr)

def pairwise(it):
    it = iter(it)
    while True:
        yield next(it), next(it)


def gameOfThrees(nr):
	steps = []

	while nr != 1 :
		if nr % 3 == 0 :
			# add(steps, nr)
			print("%d %d" % (nr, 0))
			nr /= 3
			# add(steps, "0")
		elif (nr-1) % 3 == 0 :
			# add(steps, nr)
			print("%d %d" % (nr, -1))
			nr = (nr - 1) / 3
			# add(steps, "-1")
		else:
			# add(steps, nr)
			print("%d %d" % (nr, +1))
			nr = (nr + 1) / 3
			# add(steps, "1")
	print (1)

	# for i in pairwise(steps):
	# 	print(i)


gameOfThrees(31337357)