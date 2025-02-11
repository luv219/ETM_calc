import math

def orifice_meter_discharge():
    # Known/Fixed parameters (update if needed)
    g = 9.81  # m/s^2, acceleration due to gravity
    
    # Collecting tank dimensions
    length_tank = 0.30  # m
    breadth_tank = 0.30  # m
    A = length_tank * breadth_tank  # m^2
    h_rise = 0.10  # m (10 cm rise)
    
    # Orifice meter dimensions (in meters)
    d1 = 0.025  # 25 mm inlet diameter
    d2 = 0.01677   # 16.77 mm orifice diameter (corrected)
    
    # Calculate cross-sectional areas of inlet and orifice
    a1 = math.pi * (d1**2) / 4
    a2 = math.pi * (d2**2) / 4
    
    # Prompt user for manometer readings and time
    h1 = float(input("Enter manometer reading h1 (in cm): "))
    h2 = float(input("Enter manometer reading h2 (in cm): "))
    t  = float(input("Enter time (in seconds) for 10 cm rise in the tank: "))
    
    # Differential manometer reading in cm
    hm = abs(h1 - h2)
    
    # Convert this to an equivalent water head H (in meters)
    # Often given as H = (12.6 × hm × 10^-2) if the fluid is mercury, etc.
    # Adjust the factor as per your laboratory instructions.
    # For example:
    # H = 0.126 * hm
    # Here we just assume direct cm -> m if the manometer fluid is water:
    H = hm * 1e-2  # (simple case: 1 cm difference => 0.01 m of water)
    
    # --- Actual discharge (Q_a) ---
    # Q_a = (Area of tank × height rise) / time
    # Since area = 0.09 m^2 and height = 0.1 m, A*h = 0.009 m^3
    # so Q_a = 0.009 / t
    Qa = (A * h_rise) / t
    
    # --- Theoretical discharge (Q_t) ---
    # From the standard orifice equation:
    # Q_t = (a1 * a2 * sqrt(2*g*H)) / sqrt(a1^2 - a2^2)
    # (valid when a1 > a2; otherwise, use the appropriate formula if orifice is larger)
    numerator   = a1 * a2 * math.sqrt(2 * g * H)
    denominator = math.sqrt(a1**2 - a2**2)  # be mindful if a2 > a1
    Qt = numerator / denominator
    
    # --- Coefficient of discharge (C_d) ---
    Cd = Qa / Qt
    
    # Print results
    print(f"\n--- Results ---")
    print(f"Manometer head (Hm)                = {hm} m")
    print(f"Manometer head (H)                = {H:.4f} m")
    print(f"Actual discharge (Q_a)            = {Qa:.6f} m^3/s")
    print(f"Theoretical discharge (Q_t)       = {Qt:.6f} m^3/s")
    print(f"Coefficient of discharge (C_d)    = {Cd:.4f}")

# Run the function if desired:
orifice_meter_discharge()
