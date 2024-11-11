import tkinter as tk
from tkinter import ttk

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

def display_points(points):
    root = tk.Tk()
    root.title("Puntos en la Curva Elíptica")
    
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Crear un Listbox con scrollbar
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
    
    listbox = tk.Listbox(frame, height=20, width=50, yscrollcommand=scrollbar.set)
    listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    scrollbar.config(command=listbox.yview)
    
    for point in points:
        listbox.insert(tk.END, f'({point[0]}, {point[1]})')
    
    listbox.insert(tk.END, "Punto en el infinito")
    
    root.mainloop()

# Entrada de valores
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
p = int(input("Ingrese el valor de p: "))

# Encontrar los puntos en la curva
points = find_points(a, b, p)

# Mostrar los puntos en una ventana
display_points(points)
