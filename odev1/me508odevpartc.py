import math

val_nT = 1*5777

lam_uv_alt = 10**-2
lam_vis_alt = 4 * 10**-1
lam_vis_ust = 7 * 10**-1
lam_ir_ust = 10**3

input_uv_alt = lam_uv_alt * val_nT
input_vis_alt = lam_vis_alt * val_nT
input_vis_ust = lam_vis_ust * val_nT
input_ir_ust = lam_ir_ust * val_nT

C1 = 3.7418 * (10**-16)
C2_micro = 14388

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

print("\n\n\n\n")
print("fraction of ultraviolet range: ",numeric_trapezoid_cumulative(input_uv_alt,input_vis_alt,100000)/full_range)
print("fraction of visible range:    ",numeric_trapezoid_cumulative(input_vis_alt,input_vis_ust,100000)/full_range)
print("fraction of infrared range:   ",numeric_trapezoid_cumulative(input_vis_ust,input_ir_ust,100000)/full_range)
print("\n\n\n\n")
