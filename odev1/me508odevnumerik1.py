import math

uv_alt = 10**-8
vis_alt = 4 * 10**-7
vis_ust = 7 * 10**-7
ir_ust = 10**-3

C1 = 3.7418 * (10**-16)
C2 = 0.014388

class planck:

    def __init__(self,n,lam,T):
        self.planck_numerator(n,T)
        self.planck_nlamt(n,lam,T)
        self.planck_bracket()
        self.planck_denominator()
        self.result_planck = self.result_planck_numerator / self.result_planck_denominator
        
    def planck_numerator(self,n,T):
        self.result_planck_numerator = C1 * n**3 * T**5

    def planck_nlamt(self,n,lam,T):
        self.result_planck_nlamt = n*lam*T

    def planck_bracket(self):
        self.result_planck_bracket = math.exp(C2 / self.result_planck_nlamt) - 1

    def planck_denominator(self):
        self.result_planck_denominator = self.result_planck_nlamt**5 * self.result_planck_bracket


def numeric_trapezoid(delta,x1,x2):
    p1 = planck(n=1,lam=x1,T=5777)
    p2 = planck(n=1,lam=x2,T=5777)
    return 0.5* delta * (p1.result_planck + p2.result_planck)


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

# print(numeric_trapezoid_cumulative(vis_alt,vis_ust,1))
# print(numeric_trapezoid_cumulative(vis_alt,vis_ust,10))
# print(numeric_trapezoid_cumulative(vis_alt,vis_ust,100))
# print(numeric_trapezoid_cumulative(vis_alt,vis_ust,1000))
# print(numeric_trapezoid_cumulative(vis_alt,vis_ust,10000))
# print(numeric_trapezoid_cumulative(vis_alt,vis_ust,100000))
print("\n\n\n\n")
print("Integrating Planck's Law using cumulative trapezoids numerical method with 1 million intervals;")
print("Integral over ultraviolet range: ",numeric_trapezoid_cumulative(uv_alt,vis_alt,1000000)," W/m^2")
print("Integral over visible range:    ",numeric_trapezoid_cumulative(vis_alt,vis_ust,1000000)," W/m^2")
print("Integral over infrared range:   ",numeric_trapezoid_cumulative(vis_ust,ir_ust,1000000)," W/m^2")
print("\n\n\n\n")

    




