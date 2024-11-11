from manim import *

class EllipticCurve(Scene):
    def construct(self):
        # Definición de la curva elíptica: y^2 = x^3 + ax + b
        a = -1
        b = 1
        
        # Definición de los ejes
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Función que evita raíces cuadradas de valores negativos
        def elliptic_function(x):
            value = x**3 + a * x + b
            return (value)**0.5 if value >= 0 else 0

        # Gráfica de la curva elíptica (parte positiva y negativa)
        elliptic_curve = axes.plot(lambda x: elliptic_function(x), color=YELLOW)
        elliptic_curve_neg = axes.plot(lambda x: -elliptic_function(x), color=YELLOW)

        # Agregar todo a la escena
        self.play(Create(axes), Write(labels))
        self.play(Create(elliptic_curve), Create(elliptic_curve_neg))
        self.wait(2)
