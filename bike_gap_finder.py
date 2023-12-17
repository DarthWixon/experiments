import numpy as np
import matplotlib.pyplot as plt

def time_ratio_calculator(speed_ratio):
	return speed_ratio/(1 - speed_ratio)

speed_ratio_list = np.linspace(0,1,500)
time_ratio_list = time_ratio_calculator(speed_ratio_list)

plt.semilogy(speed_ratio_list*100, time_ratio_list)
plt.xlabel("Lead Group Speed Fraction")
plt.ylabel("Required Multiple of Time Gap")

plt.show()