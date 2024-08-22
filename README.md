# COMPUTATIONAL-CANCER-SIMULATIONS

Contenido principal de las simulaciones realizadas para el proyecto de Aula de cálculo diferencial respecto al artículo investigativo de Modelos matemáticos para el crecimiento de células tumorales.

Este trabajo es de carácter Open Source y puede ser empleado en simulaciones computacionales básicas propias. Sin embargo; la atribución de este proyecto queda reservada para los dueños de este repositorio en exclusiva.

## Dependencias del proyecto

Las simulaciones empleadas fueron diseñadas con librerías del Lenguaje de Programación Python. Por lo que, una correcta ejecución de las simulaciones computacionales aquí presentadas requiere la previa instalación de las librerías.

### ManimCE
> Librería encargada de renderizar las animaciones de objetos matemáticos en alta calidad.
- **Descripción**: Una biblioteca de Python mantenida por la comunidad para crear animaciones matemáticas.
- **Sitio**: [Documentación de Manim](https://docs.manim.community/en/stable/installation.html)
- **Instalación**: 
    ```bash
    pip install manim
    ```

### NumPy
> Librería para realizar cálculos necesarios en los modelos empleados computacionalmente.
- **Descripción**: NumPy es el paquete fundamental para la computación científica en Python. Es una biblioteca de Python que proporciona un objeto de matriz multidimensional, varios objetos derivados (como matrices enmascaradas y matrices), y una variedad de rutinas para realizar operaciones rápidas en matrices, incluyendo operaciones matemáticas, lógicas, manipulación de formas, ordenamiento, selección, entrada/salida, transformadas de Fourier discretas, álgebra lineal básica, operaciones estadísticas básicas, simulación aleatoria y mucho más.
- **Sitio**: [Documentación de NumPy](https://numpy.org/doc/)
- **Instalación**: 
    ```bash
    pip install numpy
    ```

### Matplotlib
> Librería para realizar gráficas estéticas, también se emplea como auxiliar de un código para mejor eficacia.
- **Descripción**: Matplotlib es una biblioteca integral para crear visualizaciones estáticas, animadas e interactivas.
- **Sitio**: [Documentación de Matplotlib](https://matplotlib.org/stable/index.html)
- **Instalación**: 
    ```bash
    pip install matplotlib
    ```

### Itertools
> Librería para realizar iteraciones de manera eficaz sin consumir demasiada memoria.
- **Descripción**: Este módulo implementa una serie de bloques de construcción de iteradores inspirados en constructos de APL, Haskell y SML. Cada uno ha sido adaptado a una forma adecuada para Python.
- **Sitio**: [Documentación de Itertools](https://docs.python.org/3/library/itertools.html)
- **Instalación**: Viene incluida en la librería estándar de Python.

## Ejecución de las Simulaciones
Para ejecutar las simulaciones, asegúrate de tener instaladas todas las dependencias mencionadas anteriormente. Luego, puedes utilizar los siguientes comandos una vez te encuentres en el directorio que contiene los archivos:


## [`01-logistic_growth.py`](https://github.com/xRedDev/COMPUTATIONAL-CANCER-SIMULATIONS/blob/main/01-logistic_growth.py)
**Versión Animada**:
```bash
manim .\01-logistic_growth.py LogisticGrowth -pqh
```

**Versión Imágen Final**
```bash
manim .\01-logistic_growth.py LogisticGrowth -ps
```

## [`02-logistic_growth_matplotlib.py`](https://github.com/xRedDev/COMPUTATIONAL-CANCER-SIMULATIONS/blob/main/01-logistic_growth.py)
**Abrir una terminal y ejecutar**:
```bash
python.exe 02-logistic_growth_matplotlib.py
```

## [`with_treatment_cellular_automaton.py`](https://github.com/xRedDev/COMPUTATIONAL-CANCER-SIMULATIONS/blob/main/with_treatment_cellular_automaton.py)
**Versión Animada**:
```bash
manim .\with_treatment_cellular_automaton.py CellGridWithPlot -pqh --disable_caching
```


**Versión Imágen Final**:
```bash
anim .\with_treatment_cellular_automaton.py CellGridWithPlot -ps
```

## [`without_treatment_cellular_automaton.py`](https://github.com/xRedDev/COMPUTATIONAL-CANCER-SIMULATIONS/blob/main/without_treatment_cellular_automaton.py)
**Versión Animada**:
```bash
manim .\with_treatment_cellular_automaton.py CellGridWithPlot -pqh --disable_caching
```


**Versión Imágen Final**:
```bash
anim .\with_treatment_cellular_automaton.py CellGridWithPlot -ps
```
