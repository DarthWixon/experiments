import numpy
import matplotlib.pyplot as pyplot
import time


def per(n, n_loops = 0):
	if len(str(n)) == 1:
		return n_loops

	digits = [int(i) for i in str(n)]

	result = 1
	for digit in digits:
		result *= digit

	return per(result, (n_loops + 1))

def worth_doing(n):
	string_n = str(n)
	if '0' in string_n or '5' in string_n:
		return False
	else:
		return True

test_range = int(1e4)

max_n = 0
max_per = 0

storage = True
printing = True # printing requires storage also

start = time.time()

if storage:
	data = numpy.zeros(test_range)
	for n in range(len(data)):
		ans = per(n)
		data[n] = ans
		if ans > max_per:
			max_per = ans
			max_n = n

# else:
# 	for n in range(test_range):
# 		ans = per(n)
# 		if ans > max_per:
# 			max_per = ans
# 			max_n = n

else:
	n = 0
	while n < test_range:
		if worth_doing(n):
			ans = per(n)
			if ans > max_per:
				max_per = ans
				max_n = n
			n += 1
		else:
			n += 1
			continue

end = time.time()

print('Time taken: {:.3f} minutes'.format((end-start)/60))


print("Highest permanence = {}, for n = {}".format(max_per, max_n))

if printing and storage:
	pyplot.bar(list(range(test_range)), data)
	pyplot.xlabel('Number')
	pyplot.ylabel('Multiplicative Permanance of N')
	pyplot.show()


