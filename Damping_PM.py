import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


zeta = np.linspace(0.1, 1, 100)

#PM and damping factor relationship
num = 2*zeta
den = np.sqrt(-2*zeta**2 + np.sqrt(1+4*zeta**4))
PM = np.arctan(num/den)*180/np.pi
PM_APP = 100*zeta

#Quality factor and damping factor relationship
Q = 1/(2*zeta)

plt.figure()
plt.plot(zeta, PM, label='func')
plt.plot(zeta, PM_APP, label='approximation')
plt.grid()
plt.legend()
plt.xlabel(r'$\zeta$')
plt.ylabel('PM, deg')

plt.figure()
plt.plot(zeta, Q)
plt.grid()
plt.xlabel(r'$\zeta$')
plt.ylabel('Q')

plt.show()