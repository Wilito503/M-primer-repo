from manim import *
import numpy as np

class EllipticCurveOnTorus(ThreeDScene):
    def construct(self):
        # Configuración de la cámara 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Superficie toroidal
        torus = Torus(major_radius=2, minor_radius=0.6, resolution=(30, 30))
        torus.set_color(BLUE_E)
        
        # Agregar el toro a la escena
        self.play(Create(torus))
        self.wait(1)

        # Curva elíptica proyectada en el toro
        elliptic_curve_points = []
        a, b = -1, 1  # Coeficientes de la curva elíptica

        # Generar puntos para la curva elíptica en el toro
        for t in np.linspace(0, 2 * np.pi, 200):
            x = np.sin(t)  # Coord x en el plano paramétrico
            y = np.cos(t)  # Coord y en el plano paramétrico
            z = np.sin(2 * t)  # Coord z para darle forma 3D

            # Proyectar sobre la superficie del toro
            r_major = 2 + 0.5 * np.cos(3 * t)  # Variación en el radio mayor
            x_torus = r_major * np.cos(t)
            y_torus = r_major * np.sin(t)
            z_torus = 0.5 * np.sin(3 * t)  # Modificación del radio menor

            elliptic_curve_points.append([x_torus, y_torus, z_torus])

        # Crear la curva elíptica como un VMobject
        elliptic_curve = VMobject()
        elliptic_curve.set_points_smoothly(elliptic_curve_points)
        elliptic_curve.set_color(YELLOW)

        # Animar la creación de la curva sobre el toro
        self.play(Create(elliptic_curve), run_time=5)
        self.wait(2)

        # Rotar la cámara para visualizar en 3D
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait(2)

