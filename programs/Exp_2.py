import math

frequency_Hz=int(input("Enter Force frequency:")) #Hz

F0_mlb=float(input("Enter Force Amplitude:")) #mlb(milli-pound)
F0=F0_mlb*4.45/1000 #N

amplitude_mg=int(input("Enter Amplitude:")) #mg (milli-gravity)
amplitude=amplitude_mg*9.81/1000 #m/s^2

omega=2*math.pi*frequency_Hz #rad/s

E=210e9 #N/m^2
density=7810 #kg/m^3
l=0.315 #m
b=0.025 #m
t=0.006 #m

I=(b*t**3)/12 #m^4

K=(8*E*I)/(l**3) #N/m

volume=(l*b*t) #m^3
m_beam=density*volume #Kg

X0_theory=F0/math.sqrt((K-m_beam*omega**2)**2) #m
X0_exp=amplitude/(omega**2) #m

print("Vibration Displacement Theory:", X0_theory,'m')
print("Vibration Displacement Experimental:", X0_exp,'m')