for i in range(1, 19 + 1):
	if i % 15 == 0:
		print(f'{i} FizzBuzz')
	elif(i % 3 ==0):
		print(f'{i} Fizz')
	elif(i % 5 ==0):
		print(f'{i} Buzz')
	else:
		print(f'{i}')
