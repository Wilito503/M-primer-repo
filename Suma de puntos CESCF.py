import matplotlib.pyplot as plt

# Función para calcular y^2 para un valor dado de x
def curve_equation(x, a, b, p):
    return (x**3 + a*x + b) % p

# Función para encontrar los puntos en la curva elíptica
def find_points(a, b, p):
    points = []
    for x in range(p):
        y2 = curve_equation(x, a, b, p)
        for y in range(p):
            if (y * y) % p == y2:
                points.append((x, y))
    return points

# Función para sumar dos puntos en la curva elíptica
def point_addition(P, Q, a, p):
    if P is None or Q is None:
        return None

    x1, y1 = P
    x2, y2 = Q

    if P == Q:
        # Punto doble
        if y1 == 0:
            return None  # Punto en el infinito
        m = (3 * x1**2 + a) * pow(2 * y1, p-2, p) % p
    else:
        # Suma de dos puntos diferentes
        if x1 == x2:
            if y1 != y2:
                return None  # Punto en el infinito
            else:
                return None  # Los puntos son el mismo punto y se cancelan

        m = (y2 - y1) * pow(x2 - x1, p-2, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

# Graficar la curva elíptica
def plot_curve(points, a, b, p, result_point=None, n=None):
    plt.figure(figsize=(10, 10))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    if points:
        x_vals, y_vals = zip(*points)
        plt.scatter(x_vals, y_vals, color='red')
        for x, y in points:
            plt.text(x, y, f'({x},{y})', fontsize=9, ha='right')

    if result_point:
        x_res, y_res = result_point
        plt.scatter(x_res, y_res, color='blue')
        plt.text(x_res, y_res, f'{n}P = ({x_res},{y_res})', fontsize=12, color='blue', ha='left')

    plt.title(f'Curva Elíptica sobre F_{p}: y^2 = x^3 + {a}x + {b} (mod {p})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-1, p)
    plt.ylim(-1, p)
    plt.show()

# Entrada de valores
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
p = int(input("Ingrese el valor de p: "))
x = int(input("Ingrese el valor de x para el punto P: "))
y = int(input("Ingrese el valor de y para el punto P: "))
n = int(input("Ingrese el número de veces que desea sumar el punto consigo mismo: "))

# Verificar que el punto inicial es válido
points = find_points(a, b, p)
if (x, y) not in points:
    print("El punto proporcionado no está en la curva elíptica.")
else:
    # Sumar el punto P consigo mismo n veces
    P = (x, y)
    Q = P
    for _ in range(n - 1):
        Q = point_addition(Q, P, a, p)
        if Q is None:
            print("El resultado es el punto en el infinito.")
            break

    # Imprimir el resultado de la suma
    print(f'{n}P = {Q}')

    # Graficar los puntos de la curva elíptica y el resultado final
    plot_curve(points, a, b, p, result_point=Q, n=n)
