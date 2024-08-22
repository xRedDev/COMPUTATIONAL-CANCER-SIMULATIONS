from manim import *
import numpy as np
import itertools as it
import matplotlib as plt

'''
ESTE PROGRAMA DISEÑA UNA ANIMACIÓN PARA VISUALIZAR LA EVOLUCIÓN DE DISTINTAS POBLACIONES CELULARES EN UN MODELO LOGÍSTICO SIMPLE.
'''

# El programa está diseñado con librerías de Python: ManimCE (Community Edition), NumPy, Itertools y Matplotlib
# Por lo que; se necesitan sus instalaciones y dependencias.

''' LIBRERÍA   |     INSTALACIÓN        | DEPENDENCIAS '''

''' MANIMCE    | pip install manimce    | https://docs.manim.community/en/stable/installation.html '''
''' NUMPY      | pip install numpy      | *pip las descarga en automático* '''
''' ITERTOOLS  | pip install itertools  | https://docs.python.org/3/library/itertools.html '''
''' MATPLOTLIB | pip install matplotlib | *pip las descarga en automático* '''

class LogisticGrowth(Scene):
    '''
    Esta clase hereda de Scene y se emplea para usar las bases de Manim en la animación
    '''
    def construct(self):
        # INICIALIZAMOS LOS PARÁMETROS

        K = 1.0  # Capacidad de carga de la especie celular
        a = 0.5  # Tasa de crecimiento de la especie celular
        #                               (rango incial, rango final, divisiones entre el rango de las condiciones)
        initial_conditions = np.linspace(0.1, 2.0, 35)  # Diferentes condiciones iniciales desde 0.1 a 2.0

        # Función x(t)
        def x_t(t, K, K_prime, a):
            '''
            Esta Función recibe:\n
            tiempo (`t`)\n
            capacidad de carga de la especie celular (`K`)\n
            constante de ingración (`K_prime`)\n
            tasa de crecimiento de la especie celular (`a`)\n

            Y devuelve la función del módelo logístico simple
            
            '''
         #     x(t) = (K_prime * K * e^(at)) / (1 + K_prime * e^(at))"
            return (K_prime * K * np.exp(a * t)) / (1 + K_prime * np.exp(a * t))


        # Definir los ejes donde gráficaremos la evolución de cada población inicial
        axes = Axes(
            x_range=[0, 15, 1], # de 0 a 15 con paso 1
            y_range=[0, 2.1, 0.2], # de 0 a 2.1 con paso 0.2

            # Personalización del eje X
            x_axis_config={
                "include_numbers": False,
                "label_direction": DOWN,
                "include_tip": True,
            },
            # Personalización del eje Y
            y_axis_config={
                "include_numbers": False,
                "label_direction": LEFT,
                "include_tip": True,
            },
        ).scale(.8) # Convertir al 80% de su tamaño original para no saturar la pantalla

        axes_labels = axes.get_axis_labels(x_label="t", y_label="x(t)") # Añadimos los labels a sus ejes

        # Línea punteada horizontal en K (Representa la capacidad de carga)
        K_line = DashedLine(start=axes.c2p(0, K), end=axes.c2p(15, K), color=RED).set_z_index(2)

        # Colores
        colors = it.cycle(plt.cm.rainbow(np.linspace(0, 1, len(initial_conditions))))

        # Comenzamos una Lista a la cual le añadiremos cada evolución de la gráfica
        curves = []
        for x0 in initial_conditions:
            K_prime = x0 / (K - x0)
            curve = axes.plot(lambda t: x_t(t, K, K_prime, a), x_range=[0, 15], color=next(colors))
            curves.append(curve)

        # Animaciones
        self.play(Create(axes, run_time=2))
        self.wait()
        self.play(Create(axes_labels))
        self.wait()
        self.play(Create(K_line), run_time=.7)
        self.wait(2)

        for curve in curves:
            self.play(Create(curve), run_time=.6)
        self.wait(2)

# Para ejecutar la animación:
# Primero, guardar el archivo con el nombre: 01-logistic_growth.py

# Luego, abrir una Terminal (en VScode) con Control + ñ mientras se está en el directorio donde se guardó el archivo

# Correr el comando:
''' VERSIÓN ANIMADA '''
# manim .\01-logistic_growth.py LogisticGrowth -pqh

''' VERSIÓN IMAGEN FINAL (Menor tiempo de espera) '''
# manim .\01-logistic_growth.py LogisticGrowth -ps