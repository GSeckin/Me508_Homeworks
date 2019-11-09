import math
import numpy
import scipy

# def planck1(n,lam,T):
#     def planck_numerator(n,T):
#         result_planck_numerator = C1 * n**3 * T**5
#         return result_planck_numerator 

#     def planck_nlamt(n,lam,T):
#         result_planck_nlamt = n*lam*T
#         return result_planck_nlamt

#     def planck_bracket(result_planck_nlamt):
#         result_planck_bracket = math.exp(C2 / result_planck_nlamt) - 1
#         return result_planck_bracket
    
#     def planck_denominator(result_planck_nlamt,result_planck_bracket):
#         result_planck_denominator = result_planck_nlamt**5 * result_planck_bracket
#         return result_planck_denominator

#     result_planck1 = result_planck_numerator / result_planck_denominator
#     return result_planck1

uv_alt = 10**-8
vis_alt = 4 * 10**-7
vis_ust = 7 * 10**-7
ir_ust = 10**-3

C1 = 3.7418 * (10**-16)
C2 = 0.014388

class planck1:

    def __init__(self,n,lam,T):
        self.planck_numerator(n,T)
        self.planck_nlamt(n,lam,T)
        self.planck_bracket()
        self.planck_denominator()
        self.result_planck1 = self.result_planck_numerator / self.result_planck_denominator
        
    def planck_numerator(self,n,T):
        self.result_planck_numerator = C1 * n**3 * T**5

    def planck_nlamt(self,n,lam,T):
        self.result_planck_nlamt = n*lam*T

    def planck_bracket(self):
        self.result_planck_bracket = math.exp(C2 / self.result_planck_nlamt) - 1

    def planck_denominator(self):
        self.result_planck_denominator = self.result_planck_nlamt**5 * self.result_planck_bracket


case1 = planck1(n=1,lam=10**-6,T=5777)
print(case1.result_planck1)
case2 = planck1(n=1,lam=10**-3,T=5777)
print(case2.result_planck1)
