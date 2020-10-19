import matplotlib.pyplot as plt
import numpy as np
from scipy import fft

x = np.linspace(0, 2 * np.pi, 200)
sin1 = np.sin(8*x)
sin2 = np.sin(6*x)
sin3 = np.sin(4*x)
sin4 = np.sin(2*x)

sum = sin1 + sin2 + sin3 + sin4

Y = np.fft.fft(sum) 
fig, (ax1, ax2) = plt.subplots(ncols = 2, sharex = True, sharey = True)

fig.suptitle("DFT of Sum of Sinusoids")
ax1.plot(x*100,sum)
ax2.plot(Y)
plt.show()