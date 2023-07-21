import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


zeta = np.linspace(0, 1, 100)

num = 2*zeta
den = np.sqrt(-2*zeta**2 + np.sqrt(1+4*zeta**4))

PM = np.arctan(num/den)*180/np.pi
PM_APP = 100*zeta

plt.plot(zeta, PM, label='func')
plt.plot(zeta, PM_APP, label='approximation')
plt.grid()
plt.legend()
plt.xlabel(r'$\zeta$')
plt.ylabel('PM, deg')
plt.show()
