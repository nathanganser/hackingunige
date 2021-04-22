import sympy as sym

x = sym.Symbol('x')
y = sym.Symbol('y')
p = sym.Symbol('X')
q = sym.Symbol('Y')

# sym.sqrt(6*x-8*y)
# x*y**3 - 2*x**3
# sym.ln(x*y)
function = (2.71828)**(2*x*y)*(1-3*x*y)
print('---- CHECK FUNCTION ----')
sym.pprint(function)
x0 = 0
y0 = 1
X = 0.01
Y = 0.99


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