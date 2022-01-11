import math

n, m = map(int, input().split())

power = n * math.log(2)

if m < 1000:
    facto = 0
    for i in range(1, m+1):
        facto += math.log(i)
else:
    facto = m * (math.log(m) - 1) + (1/2) * (math.log(2*math.pi*m))

if power > facto:
    print('Exponential')
else:
    print('Factorial')





    
'''
1 31 3 1 4
submit
taro
1
02/01 10:00-12:00
check
taro
submit
jiro
3
01/31 09:00-12:00 02/01 10:00-12:00 02/02 08:00-10:00
check
jiro
'''