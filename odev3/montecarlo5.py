import math
import random
import numpy as numpy

radius_circle = float(input("Write radius(r):"))
h_distance = float(input("Write distance h:"))
a_distance = float(input("Write distance a:"))

x0, y0, z0 = a_distance, 0, h_distance

circle_eqn = "x**2 + y**2 = r**2"
line_eqn = "(x,y,z) = ( x0 + t*xu, y0 + t*yu, z0 + t*zu )"
hits = 0


def generate_unit_vector():
    phi = numpy.random.uniform(0,numpy.pi*2)
    costheta = numpy.random.uniform(1,0)
    theta = numpy.arccos(math.sqrt(costheta))
    
    xu = numpy.sin( theta ) * numpy.cos( phi)
    yu = numpy.sin( theta ) * numpy.sin( phi)
    zu = - numpy.cos( theta )

    return xu,yu,zu,xu**2+yu**2+zu**2


def check_hit(xu,yu,zu):
    if zu == 0:
        return "NO"
    else:
        t = - h_distance / zu
        x2 = a_distance + t*xu
        y2 = t*yu

        value_circle = (x2)**2 + (y2)**2
        
        if value_circle <= radius_circle**2 :
            return "YES"
        else:
            return "NO"


trial_number = int(input("Write the number of trials:"))

for i in range(trial_number):
    list_unitvector = generate_unit_vector()
    # print(list_unitvector)

    if check_hit(list_unitvector[0],list_unitvector[1],list_unitvector[2]) == "YES":
        hits += 1


print("\nResults\nSample Size= {}\nNo. of hits= {}\nView Factor= {}".format(trial_number,hits,hits/trial_number))

print("\n\nfrom Appendix D")
H = h_distance / a_distance
R = radius_circle / a_distance 
Z = 1 + H**2 + R**2
F = 0.5 * ( 1 - (Z-2*R**2)/(math.sqrt(Z**2 - 4*R**2)) )
print("View Factor = {}".format(F))