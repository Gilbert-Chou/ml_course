import sympy
import numpy as np

x = sympy.Symbol('x')
y = sympy.Symbol('y')

#方程式
f = x + y - 100 * (x**2 + y**2 - 1) ** 2

#求一階導數
dfx = sympy.diff(f, x)
dfy = sympy.diff(f, y)

# print(sympy.diff(f, x))
# print(sympy.diff(f, y))

#初始位置
x0 = 1
y0 = 1

#步數
n = 0.005
# epsilon = 1e-8

for i in range(0, 1000):
# while True:
    tmpx = x0
    tmpy = y0

    #Gradient Descent
    x0 = tmpx - n * dfx.evalf(subs={x:tmpx, y:tmpy})
    y0 = tmpy - n * dfy.evalf(subs={x:tmpx, y:tmpy})

    # error = abs(dfx.evalf(subs={x:tmpx, y:tmpy}) - dfx.evalf(subs={x:x0, y:y0}))
    # print(error)
    # if error < epsilon:
    #     break

print("x =", x0)
print("y =", y0)