import matplotlib.pyplot as plt
import numpy as np
import control
num = np.array([1, 1])
den = np.array([3 , 1])
H1 = control.tf(num , den)
num = np.array([2, 1])
den = np.array([4 , 1]) 
H2 = control.tf(num , den)
H = control.series(H1,H2)
print ('H(s) =', H)
z = control.zero(H)
print ('z =', z)
p = control.pole(H)
print ('p =', p)

plt.figure()
control.pzmap(H)

# Step Response
t, y = control.step_response(H)
# Plotting
plt.figure()
plt.plot(t, y)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()

plt.figure()
Gmag, Gphase, Gomega = control.bode_plot(H)

#plt.figure()
#plt.semilogx(Gomega, Gmag)    # Bode magnitude plot
#plt.figure()
#plt.semilogx(Gomega, Gphase)  # Bode phase plot


plt.show()