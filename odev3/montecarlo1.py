import math
import random

R = 1
H = 2
angle_max = math.atan(R/H)
hits = 0
test_number = int(input("Deneme sayısını rakamla giriniz\n"))

for i in range(test_number):
    number_gen = random.random()
    angle_new = math.asin(math.sqrt(number_gen))
    if angle_new <= angle_max:
        hits += 1

print("Results\nSample Size= {}\nNo. of hits= {}\nView Factor= {}".format(test_number,hits,hits/test_number))
    


