import math
while 1 == 1:
	inp = int(input("(only intergers!) simplify the sqrt of "))
	print(" ")
	if not math.floor(math.sqrt(inp)) == math.sqrt(inp):
		i = math.floor(math.sqrt(inp))
		i = i  + 1
		multiplier = 1
		sqrt = inp
		while i > 0:
			if ( inp / i**2 ) == math.floor(inp / i**2):
				multiplier = i
				sqrt = inp / i**2
				break
			i = i-1
		if multiplier == 1:
			answer = "sqrt(" + str(sqrt) + ")"
		else:
			answer = str(multiplier) + "* sqrt(" + str(sqrt) + ")"
	else:
		answer = math.sqrt(inp)
	print(answer)
	print(" ")