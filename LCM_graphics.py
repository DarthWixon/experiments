import numpy
import matplotlib.pyplot as pyplot

highest_number = 1000

n_list = numpy.arange(highest_number)

gcd_data = numpy.zeros((highest_number, highest_number))
lcm_data = numpy.zeros((highest_number, highest_number))

for i in n_list:
	gcd_data[i,:] = numpy.gcd(i, n_list)
	lcm_data[i,:] = numpy.lcm(i,n_list)


pyplot.matshow(gcd_data, fignum = 1)
pyplot.colorbar(orientation = 'horizontal')
pyplot.title('GCD for Numbers Between 1 and {}'.format(highest_number))


pyplot.matshow(lcm_data, fignum = 2)
pyplot.colorbar(orientation = 'horizontal')
pyplot.title('LCM for Numbers Between 1 and {}'.format(highest_number))

pyplot.show()