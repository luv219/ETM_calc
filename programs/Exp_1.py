import math

f1=float(input("Enter mean Experimental Natural frequency:"))

X0=2
Xn=1.5
n=5

omega_n= 2*math.pi*f1 #rad/s
omega_hz=omega_n/(2*math.pi)
delta=(1/n)*math.log(X0/Xn)
zeta=delta/math.sqrt(delta**2+(2*math.pi)**2)

print("Theoretical Natural Frequency:", omega_hz)
print("Damping Factor:", zeta)