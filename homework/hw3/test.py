import sympy
import numpy as np

x = sympy.Symbol('x')
y = sympy.Symbol('y')

# f = x + y - 100 * (x**2 + y**2 - 1) ** 2
f = x*x + y*y
dfx = sympy.diff(f, x)
dfy = sympy.diff(f, y)

print(sympy.diff(f, x))
# print(sympy.diff(f, y))

# print(dfx.evalf(subs={x:1, y:1}))
# print((1 - 0.005 * dfx.evalf(subs={x:1, y:1})))
x0 = 10
y0 = 10
n = 0.005
epsilon = 1e-8

# for i in range(0, 1000):
while True:
    tmpx = x0
    tmpy = y0
    dx = dfx.evalf(subs={x:tmpx, y:tmpy})
    dy = dfy.evalf(subs={x:tmpx, y:tmpy})
    print(dx)

    x0 = tmpx - n * dx
    y0 = tmpy - n * dy
    error = abs(dfx.evalf(subs={x:tmpx, y:tmpy}) - dfx.evalf(subs={x:x0, y:y0}))
    # print(error)
    if error < epsilon:
        break
    # print("x =", x0)
    # print("y =", y0)

print("x =", x0)
print("y =", y0)