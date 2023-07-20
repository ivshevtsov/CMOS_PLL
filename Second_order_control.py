import matplotlib.pyplot as plt
import numpy as np
import control

#example

wn=5
zeta=1

num = np.array([wn * wn])
den = np.array([1, 2 * zeta * wn, wn * wn])
H = control.tf(num, den)
print('H(s) =', H)
z = control.zero(H)
print('z =', z)
p = control.pole(H)
print('p =', p)

plt.figure(1)
control.pzmap(H)

# Step Response
t, y = control.step_response(H)
# Plotting
plt.figure(2)
plt.plot(t, y, label=fr'$\zeta$={zeta}')
plt.legend()
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()

plt.figure(3)
Gmag, Gphase, Gomega = control.bode_plot(H)



#plt.figure()
#plt.semilogx(Gomega, Gmag)    # Bode magnitude plot
#plt.figure()
#plt.semilogx(Gomega, Gphase)  # Bode phase plot


plt.show()