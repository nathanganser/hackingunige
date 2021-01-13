import sympy as sym

x = sym.Symbol('x')
y = sym.Symbol('y')
p = sym.Symbol('X')
q = sym.Symbol('Y')

# sym.sqrt(6*x-8*y)
# x*y**3 - 2*x**3
# sym.ln(x*y)

function = x**3 + y**3
print('---- CHECK FUNCTION ----')
sym.pprint(function)

x_derivative = sym.diff(function, x)
second_x_derivative = sym.diff(x_derivative, x)
y_derivative = sym.diff(function, y)
second_y_derivative = sym.diff(y_derivative, y)
y_x_derivative = sym.diff(y_derivative, x)

print('------ EQUATION ------')

sym.pprint(second_x_derivative*second_y_derivative-y_x_derivative**2)
