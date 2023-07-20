import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import control
#https://jckantor.github.io/CBE30338/05.03-Creating-Bode-Plots.html
#https://docs.sympy.org/latest/modules/physics/control/control_plots.html
# Define Transfer Function
num = np.array([2])
den = np.array([3 , 1])
H = signal.TransferFunction(num , den)
print ('H(s) =', H)

ww, mag, phase = signal.bode(H)
plt.figure()
plt.semilogx(ww, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(ww, phase)  # Bode phase plot

w,HF = signal.freqs(num, den)

# Step Response
t, y = signal.step(H)

zero=signal.ZerosPolesGain(H)
print(zero)

plt.figure()
plt.plot(w,20*np.log10(HF))
plt.xscale('log')
plt.grid()


#find bode plot

# Plotting
plt.figure()
plt.plot(t, y)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()


plt.show()
