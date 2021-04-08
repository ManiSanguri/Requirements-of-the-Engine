# Input Parameters

m = input('Enter the mass of the vehicle');  
rr = input('Enter the rolling resistance of the vehicle'); 
sin_theta = input('Enter the sine of gradient angle of the road');
A = input('Enter the frontal area of the vehicle');
Cd = input('Enter the coefficient of drag of the vehicle');
g = 9.8; # Acceleration due to gravity
rho = 1.225; # Value of Air Density
r = input('Enter the radius of the tire'); 
gear_min = input('Enter the gear ratio of first gear');
gear_max = input('Enter the gear ratio of last gear');

# Enter your choice from the following 

i = input('Enter your choice from the following: \n 1. Just starting the vehicle (v=0) \n 2. Constant velocity of the vehicle (a=0) \n 3. Accelerating or Deccelerating the vehicle \n ');

#Calculation of the forces on the vehicle

if i==1:
    a = input('Enter the maximum acceleration of the vehicle');
    v = 0;
    Faero = 0.5*m*v*v*rho*A; # Aerodynamic force on the vehicle
    Fgr = m*g*sin_theta; # Gradient force on the vehicle
    Frr = rr*m*g; # Rolling resistance force on the vehicle
    Fin = 1.25*m*a; # Inertial force on the vehicle
    
elif i==2:
    v = input('Enter the maximum velocity of the vehicle');
    a = 0;
    Faero = 0.5*m*v*v*rho*A; # Aerodynamic force on the vehicle
    Fgr = m*g*sin_theta; # Gradient force on the vehicle
    Frr = rr*m*g; # Rolling resistance force on the vehicle
    Fin = 1.25*m*a; # Inertial force on the vehicle
    
elif i==3:
    v = input('Enter the maximum velocity of the vehicle');
    a = input('Enter the maximum acceleration of the vehicle');
    Faero = 0.5*m*v*v*rho*A; # Aerodynamic force on the vehicle
    Fgr = m*g*sin_theta; # Gradient force on the vehicle
    Frr = rr*m*g; # Rolling resistance force on the vehicle
    Fin = 1.25*m*a; # Inertial force on the vehicle

else :
     print('Wrong option');

# Calculation of total forces on the vehicle

Ftotal = Faero+Fgr+Frr+Fin;

# Calculation of the torque requirement of the vehicle

T = Ftotal*r;
if i==1:
    Treq = T/gear_min;
else:
    Treq = T/gear_max;

print('Torque requirement of the vehicle is',Treq);
    
# Calculation of the power requirement of the vehicle

P = Ftotal*v;

print('Power requirement of the vehicle is',P);

# End
