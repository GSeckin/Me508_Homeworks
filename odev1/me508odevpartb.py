import math

C1 = 3.7418 * (10**-16)
C2_m = 0.014388
C2_micro = 14388
C2_cm = 1.4388

def column2_value(column1_value):
    return (1/column1_value) * 10**4

def column3_value(column1_value):
    return C1 / (((column1_value*10**-6)**5 * (math.exp(C2_micro / column1_value) - 1))*10**6)

def column4_value(column1_value,column2_value):
    return ( (C1 * (column2_value*10**2)**3) / (math.exp(column2_value*C2_cm) - 1) )*100

val_nT = 1*5777

lam_uv_alt = 10**-2
lam_vis_alt = 4 * 10**-1
lam_vis_ust = 7 * 10**-1
lam_ir_ust = 10**3

input_uv_alt = lam_uv_alt * val_nT
input_vis_alt = lam_vis_alt * val_nT
input_vis_ust = lam_vis_ust * val_nT
input_ir_ust = lam_ir_ust * val_nT

class planck2:

    def __init__(self,column1_value):
        self.result_planck2 = self.column3_value(column1_value)
    
    def column3_value(self,column1_value):
        return C1 / (((column1_value*10**-6)**5 * (math.exp(C2_micro / column1_value) - 1))*10**6)


def numeric_trapezoid(delta,x1,x2):
    p1 = planck2(x1)
    p2 = planck2(x2)
    return 0.5* delta * (p1.result_planck2 + p2.result_planck2)


def numeric_trapezoid_cumulative(xi,xf,number_of_intervals):
    delta = (xf - xi) / number_of_intervals
    pointlist = []
    point = xi
    while point < xf:
        pointlist.append(point)
        point += delta
    pointlist.append(xf)
    
    counter = 0
    integral_result = 0
    while counter < number_of_intervals:
        integral_result += numeric_trapezoid(delta,pointlist[counter],pointlist[counter+1])
        counter += 1
    
    return integral_result

full_range = numeric_trapezoid_cumulative(100,1000000,100000)

column1_list = [1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,
2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,
3100,3200,3300,3400,3500,3600,3700,3800,3900,4000,
4100,4200,4300,4400,4500,4600,4700,4800,4900,5000,
5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,
6200,6400,6600,6800,7000,7200,7400,7600,7800,8000,
8200,8400,8600,8800,9000,9200,9400,9600,9800,10000,
10200,10400,10600,10800,11000,11200,11400,11600,11800,12000,
12200,12400,12600,12800,13000,13200,13400,13600,13800,14000,
14200,14400,14600,14800,15000,
16000,17000,18000,19000,20000,21000,22000,23000,24000,25000,
26000,27000,28000,29000,30000,31000,32000,33000,34000,35000,
36000,37000,38000,39000,40000,41000,42000,43000,44000,45000,
46000,47000,48000,49000,50000]

fulltable = []

for value in column1_list:
    value2 = column2_value(value)
    temporary_list = [value, value2, column3_value(value), column4_value(value,value2), numeric_trapezoid_cumulative(100,value,10000)/full_range ]
    fulltable.append(temporary_list)

for i in fulltable:
    print(i)
