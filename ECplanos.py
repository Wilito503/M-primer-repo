from manim import *
import numpy as np

class EllipticCurveEvolution(Scene):
    def construct(self):
        # Etapa 1: Curva elíptica en el plano real
        self.play(Write(Text("Curva Elíptica en el Plano Real").to_edge(UP)))
        self.plot_real_curve()
        self.wait(2)
        self.clear()

        # Etapa 2: Curva elíptica sobre un campo finito
        self.play(Write(Text("Curva Elíptica sobre un Campo Finito").to_edge(UP)))
        self.plot_finite_field_curve()
        self.wait(2)
        self.clear()

        # Etapa 3: Curva elíptica en el toro
        self.play(Write(Text("Curva Elíptica en el Toro").to_edge(UP)))
        self.plot_toroidal_curve()
        self.wait(2)

    def plot_real_curve(self):
        # Definición de la curva elíptica: y^2 = x^3 + ax + b
        a = -1
        b = 1

        # Definir los ejes
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        def elliptic_function(x):
            value = x**3 + a * x + b
            return (value)**0.5 if value >= 0 else 0

        # Curva elíptica en el plano real
        elliptic_curve = axes.plot(lambda x: elliptic_function(x), color=YELLOW)
        elliptic_curve_neg = axes.plot(lambda x: -elliptic_function(x), color=YELLOW)

        self.play(Create(axes), Write(labels))
        self.play(Create(elliptic_curve), Create(elliptic_curve_neg))
    
    def plot_finite_field_curve(self):
        # Simular una curva elíptica sobre un campo finito Z_p
        a = -1
        b = 1
        p = 7  # Campo finito F_p

        axes = Axes(
            x_range=[0, p, 1], y_range=[0, p, 1],
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Curva elíptica sobre Z_p
        points = VGroup()
        for x in range(p):
            for y in range(p):
                if (y**2) % p == (x**3 + a * x + b) % p:
                    point = Dot(axes.coords_to_point(x, y), color=YELLOW)
                    points.add(point)
        
        self.play(Create(axes), Write(labels))
        self.play(Create(points))

    def plot_toroidal_curve(self):
        # Simular una curva elíptica en un toro
        a = -1
        b = 1

        # Superficie toroidal
        torus = Torus(major_radius=2, minor_radius=0.5)

        # Curva elíptica proyectada en el toro
        curve_points = []
        for t in np.linspace(0, 2 * np.pi, 100):
            x = np.sin(t)
            y = np.cos(t)
            z = np.sin(2*t)  # Ejemplo de curva sobre el toro
            curve_points.append([x, y, z])

        toroidal_curve = VMobject()
        toroidal_curve.set_points_as_corners([*curve_points])
        toroidal_curve.set_color(YELLOW)

        self.play(Create(torus))
        self.play(Create(toroidal_curve))
