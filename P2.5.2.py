import math
Hplus = 0
Hplus1 = (((1.78*10**(-5))*(0.01-Hplus))**(0.5))

while (abs(float(Hplus1-Hplus))>float(1*((10)**(-10)))):
  Hplus = Hplus1
  Hplus1=(((1.78*10**(-5))*(0.01-Hplus))**(0.5))
print ("Hydrogen ion concentration is ",Hplus1)
print ("pH is ",(math.log(Hplus1))*-1)


  