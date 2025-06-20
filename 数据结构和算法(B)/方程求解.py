# 牛顿法求解方程 x^3 - 5x^2 +10x -80 =0

def function(x):
    return x**3-5*x**2+10*x-80

def derivative(x):
    return 3*x**2-10*x+10

def gradient(x):
    while function(x) / derivative(x) > 10**(-10):
        x = x - function(x) / derivative(x)
    return x-function(x)/derivative(x)

print(f'{gradient(6):.9f}')
