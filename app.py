from flask import Flask, render_template, request
import math
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/Calc_Exp1", methods=['GET',"POST"])
def Calc_Exp1():
    if request.method=='POST':
        f1=float(request.form["f1"])
        X0=float(request.form["X0"])
        Xn=float(request.form["Xn"])
        n=float(request.form["n"])

        omega_n= 2*math.pi*f1 #rad/s
        omega_Hz=omega_n/(2*math.pi)
        delta=(1/n)*math.log(X0/Xn)
        zeta=delta/math.sqrt(delta**2+(2*math.pi)**2)

        return render_template('result.html', 
                               result1=f"Theoretical Natural Frequency: {omega_Hz:.2f} Hz",
                               result2=f"Damping Factor: {zeta:.4f}")
    return render_template('exp1.html')

@app.route("/Calc_Exp1", methods=['GET',"POST"])
def Calc_Exp1():
    if request.method=='POST':
        frequency_Hz = int(request.form['frequency_Hz'])
        F0_mlb = float(request.form['F0_mlb'])
        amplitude_mg = int(request.form['amplitude_mg'])
        density=int(request.form['density'])
        l=float(request.form['l'])
        b=float(request.form['b'])
        t=float(request.form['t'])
        c=float(request.form['c'])
        E=210e9


        F0=F0_mlb*4.45/1000
        amplitude=amplitude_mg*9.81/1000
        omega=2*math.pi*frequency_Hz
        I=(b*t**3)/12
        k=(8*E*I)/(l**3)
        volume=(l*b*t)
        m_beam=density*volume

        X0_theory=F0/math.sqrt((k-m_beam*omega**2)**2+(c*omega**2))
        X0_exp=amplitude/(omega**2)

        return render_template('result.html', 
                               result1=f"Vibration Displacement Theory: {X0_theory:.6f} m",
                               result2=f"Vibration Displacement Experimental: {X0_exp:.6f} m")
    return render_template('exp2.html')

if __name__ == '__main__':
    app.run(debug=True)