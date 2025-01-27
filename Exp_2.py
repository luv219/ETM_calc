import math
l=31.5/100 #m
b=2.5/100 #m
t=0.6/100 #m

f0=float(input("Enter Force amplitude:"))
rho=7810 #kg/m^3
E=210*10**9 #pa

I=(b*(t**3))/12 #m^4
k=(8*E*I)/(l**3)

c=0
omega=0

X = f0 / math.sqrt((k - (rho * l * b * t) * omega**2)**2 + (c * omega)**2)

print('Vibration Displacement theory:', X)

a=int(input("Enter the amplitude:"))
a_fin=a*9.8/1000
Xf=a_fin/omega**2

print("Vibration Displacement apltitude(exp):", Xf)