import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors

'''
ESTE PROGRAMA DISEÑA UNA ANIMACIÓN PARA VISUALIZAR LA EVOLUCIÓN DE DISTINTAS POBLACIONES EN UN MODELO LOGÍSTICO.
'''
# ESTA ES LA VERSIÓN DE MALTPLOLIB PARA EL MODELO LOGÍSTICO SIMPLE CON EL FIN DE OBTENER RESULTADOS MÁS RÁPIDAMENTE

# Parámetros
K = 1.0  # Capacidad de carga
a = 0.1  # Tasa de crecimiento (ajustada)
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
        Recibe parámetros con los cuales ca
    '''
    return (K_prime * K * np.exp(a * t)) / (1 + K_prime * np.exp(a * t))

# Tiempo
t = np.linspace(0, 100, 500)  # Ajustar el tiempo hasta 100 unidades para observar el crecimiento a largo plazo

# Configuración estética
fig, ax = plt.subplots(figsize=(10, 6), facecolor='black')
ax.set_xlim(0, 100)  # Ajustar el límite del eje x para el rango de tiempo
ax.set_ylim(0, 2) # Ajustar el límite del eje y para el rango de las condiciones x0
ax.set_facecolor('black')
ax.tick_params(colors='white')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

# Aplicar colores
colors = plt.cm.rainbow(np.linspace(0, 1, len(initial_conditions)))

# Inicializar líneas para cada condición inicial
lines = []
for color in colors:
    line, = ax.plot([], [], lw=2, color=color)
    lines.append(line)

# Línea horizontal en la Capacidad de Carga K
ax.axhline(y=K, color='orange', linestyle='--', label='K')

# Títulos y leyendas
ax.set_xlabel('Tiempo (t)', color='white')
ax.set_ylabel('x(t)', color='white')
ax.set_title('Modelo logístico para distintas poblaciones iniciales de células tumorales', color='white')
ax.legend(loc='upper right', frameon=False, fontsize=10)
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Función de inicialización
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Función de actualización
def update(frame):
    for i, x0 in enumerate(initial_conditions):
        K_prime = x0 / (K - x0)
        x_values = x_t(t[:frame], K, K_prime, a)
        lines[i].set_data(t[:frame], x_values)
    
    # Reiniciar la animación si todas las curvas han alcanzado K
    if np.all([x_t(t[frame], K, x0 / (K - x0), a) >= K for x0 in initial_conditions]):
        init()
        return lines
    return lines

# Animación
ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20, repeat=True)

plt.show()

# Correr el código con Control + Alt + n
