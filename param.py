# Whirlybird Parameter File (pg. 126)
import numpy as np

# Physical parameters of the whirlybird (m)
r = .12       #radius of the props
d = .178       #distance to point 4 from the center of the props.
l_1 = .85      #distance from point 2 to point 4
l_2 = .3048      #distance from point 2 to point 3
h = .65       #distance from point 1 to 2, the vertical height

#Mass Characteristics (later)
g = 9.81
m1 = .891
m2 = 1
Jx = 0.0047
Jy = 0.0014
Jz = 0.0041
#Km = ?
Sigma_Gyro = 8.72667e-5
Signal_Pixel = 0.05

# Simulation Parameters
Ts = 0.01 

# Initial Conditions
roll0 = 0.0*np.pi/180  # ,rads
pitch0 = 0.0*np.pi/180  # ,rads
yaw0 = 0.0*np.pi/180  # ,rads