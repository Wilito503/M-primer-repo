def curve_equation(x, a, b, p):
    return (x**3 + a*x + b) % p

def find_points(a, b, p):
    points = []
    for x in range(p):
        y2 = curve_equation(x, a, b, p)
        for y in range(p):
            if (y * y) % p == y2:
                points.append((x, y))
    return points

def point_addition(P, Q, a, p):
    if P is None or Q is None:
        return None
    x1, y1 = P
    x2, y2 = Q
    if P == Q:
        if y1 == 0:
            return None 
        m = (3 * x1**2 + a) * pow(2 * y1, p-2, p) % p
    else:
        if x1 == x2:
            if y1 != y2:
                return None 
            else:
                return None 

        m = (y2 - y1) * pow(x2 - x1, p-2, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

def calculate_order(P, a, p):
    Q = P
    order = 1
    while True:
        Q = point_addition(Q, P, a, p)
        if Q is None:
            return order + 1
        if Q == P:
            break
        order += 1
    return order + 1

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
p = int(input("Ingrese el valor de p: "))
x = int(input("Ingrese el valor de x para el punto P: "))
y = int(input("Ingrese el valor de y para el punto P: "))

points = find_points(a, b, p)
if (x, y) not in points:
    print("El punto proporcionado no está en la curva elíptica.")
else:
    P = (x, y)
    order = calculate_order(P, a, p)
    print(f'El orden del punto ({x},{y}) es: {order}')
