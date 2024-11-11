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

# Entrada de valores
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
p = int(input("Ingrese el valor de p: "))

# Encontrar los puntos en la curva
points = find_points(a, b, p)

# Incluir el punto en el infinito
number_of_points = len(points) + 1  # Incluye el punto en el infinito

print(f'Número de puntos en la curva elíptica: {number_of_points}')
