import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

rng = default_rng()

n_minutes = 30

fail_count = np.zeros(n_minutes)

n_trials = 200000

for t in range(n_trials):
	for m in range(n_minutes):
		for turn in range(6):
			rint = rng.integers(low = 0, high = 100, size = 1)
			if rint < m:
				fail_count[m] += 1
				break
		else:
			continue
		break

fail_count = fail_count/n_trials
cumulative = np.cumsum(fail_count)

plt.plot(cumulative, label = "Cumulative Probability")
plt.plot(fail_count, label = "Failure Probability")
plt.title("Screamer Lifetime Calculation")
plt.xlabel("Minutes Since Activation")
plt.ylabel("Probability")
plt.show()