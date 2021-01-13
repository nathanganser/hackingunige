import sympy as sym

x = sym.Symbol('x')
y = sym.Symbol('y')
p = sym.Symbol('X')
q = sym.Symbol('Y')

# sym.sqrt(6*x-8*y)
# x*y**3 - 2*x**3
# sym.ln(x*y)

function = 3*x**2 - y*x
print('---- CHECK FUNCTION ----')
sym.pprint(function)
x0 = 1
y0 = 2
X = 1.01
Y = 1.98


x_derivative = sym.diff(function, x)
y_derivative = sym.diff(function, y)

print('------ EQUATION ------')

a = function.subs([(x, x0), (y, y0)])
b = x_derivative.subs([(x, x0), (y, y0)])*(p-x0)
c = y_derivative.subs([(x, x0), (y, y0)])*(q-y0)
sym.pprint(a+b+c)

print('------ SOLUTION (val approximative) ---')
a = function.subs([(x, x0), (y, y0)])
b = x_derivative.subs([(x, x0), (y, y0)])*(X-x0)
c = y_derivative.subs([(x, x0), (y, y0)])*(Y-y0)
print(a+b+c)

print('---- DIFFERENTIELLE ___')
print(b+c)