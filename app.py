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

        formatted_zeta = "{:.6e}".format(zeta)
        formatted_zeta = formatted_zeta.replace("e", " x 10^").replace("+", "")

        return render_template('result.html', 
                               result1=f"Theoretical Natural Frequency: {omega_Hz:.2f} Hz",
                               result2=f"Damping Factor: {formatted_zeta}")
    return render_template('exp1.html')

@app.route("/Calc_Exp2", methods=['GET',"POST"])
def Calc_Exp2():
    if request.method=='POST':
        frequency_Hz = int(request.form['frequency_Hz'])
        F0_mlb = float(request.form['F0_mlb'])
        amplitude_mg = int(request.form['amplitude_mg'])
        density=int(request.form['density'])
        l=float(request.form['l'])/100
        b=float(request.form['b'])/100
        t=float(request.form['t'])/100
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

        formatted_x0t = "{:.3e}".format(X0_theory)
        formatted_x0e = "{:.3e}".format(X0_exp)

        formatted_x0t = formatted_x0t.replace("e", " x 10^").replace("+", "")
        formatted_x0e = formatted_x0e.replace("e", " x 10^").replace("+", "")

        return render_template('result.html', 
                               result1=f"Vibration Displacement Theory: {formatted_x0t} m",
                               result2=f"Vibration Displacement Experimental: {formatted_x0e} m")
    return render_template('exp2.html')

@app.route("/Calc_Exp3", methods=['GET', 'POST'])
def Calc_Exp3():
    if request.method == 'POST':
        # Fixed parameters
        g = 9.81
        length_tank = 0.30
        breadth_tank = 0.30
        A = length_tank * breadth_tank
        h_rise = 0.10
        d1 = 0.025
        d2 = 0.01677

        # Calculate areas
        a1 = math.pi * (d1**2) / 4
        a2 = math.pi * (d2**2) / 4

        # Get user inputs
        h1 = float(request.form['h1'])
        h2 = float(request.form['h2'])
        t = float(request.form['time'])

        # Calculations
        hm = abs(h1 - h2)
        H = hm * 1e-2  # Convert cm to m
        
        # Calculate discharges
        Qa = (A * h_rise) / t
        
        numerator = a1 * a2 * math.sqrt(2 * g * H)
        denominator = math.sqrt(a1**2 - a2**2)
        Qt = numerator / denominator
        
        Cd = Qa / Qt

        # Format all results for scientific notation
        formatted_Qa = "{:.3e}".format(Qa)
        formatted_Qt = "{:.3e}".format(Qt)
        formatted_Cd = "{:.3e}".format(Cd)

        # Replace 'e' with ' x 10^' for all formatted values
        formatted_Qa = formatted_Qa.replace("e", " x 10^").replace("+", "")
        formatted_Qt = formatted_Qt.replace("e", " x 10^").replace("+", "")
        formatted_Cd = formatted_Cd.replace("e", " x 10^").replace("+", "")

        return render_template('result.html',
                             result1=f"Manometer head difference (hm) = {hm:.2f} cm",
                             result2=f"Equivalent water head (H) = {H:.4f} m",
                             result3=f"Actual discharge (Qa) = {formatted_Qa} m³/s",
                             result4=f"Theoretical discharge (Qt) = {formatted_Qt} m³/s",
                             result5=f"Coefficient of discharge (Cd) = {formatted_Cd}")
    return render_template('exp3.html')

if __name__ == '__main__':
    app.run(debug=True)