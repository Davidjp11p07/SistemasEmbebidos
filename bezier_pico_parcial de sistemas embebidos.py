# Archivo: bezier_pico_parcial de sistemas embebidos.py
# Juan David Palacios
#importamos librerias
import utime
import uarray

# Creamos una funcion que define la curva de bezier
def bezier_curve(p_dir, n):
    
    # Se crea una lista vacia para guardar los puntos que se crean 
    LR = []

    for i in range(n + 1):
        t = i / n

        #se utiliza dir para que se lean los puntos de la memoria
        x = (1 - t)**3 * p_dir[0][0] + 3 * (1 - t)**2 * t * p_dir[1][0] + \
            3 * (1 - t) * t**2 * p_dir[2][0] + t**3 * p_dir[3][0]

        y = (1 - t)**3 * p_dir[0][1] + 3 * (1 - t)**2 * t * p_dir[1][1] + \
            3 * (1 - t) * t**2 * p_dir[2][1] + t**3 * p_dir[3][1]

        LR.append((x, y))

    return LR

#se guardan en la posicion de memoria elegida por el usuario
base_address = 0xA
p_dir = []

for i in range(4):
    addr = base_address + i * 8
    p_dir.append(uarray.array('f', [0.0, 0.0])) 

#Se definen los puntos de la curva los elige el usuario
p_dir[0][0], p_dir[0][1] = 0.0, 0.0
p_dir[1][0], p_dir[1][1] = 1.0, 3.0
p_dir[2][0], p_dir[2][1] = 2.0, 4.0
p_dir[3][0], p_dir[3][1] = 4.0, 1.0

# Nivel de resolucion de la curva de forma que bota n+1 puntos
n = 5


LR = bezier_curve(p_dir, n)

# Imprimir los puntos que generamos de forma que i es el numero del punto en cuestion y puntosBezier es la pareja coordenada x,y
print("\nPuntos de la curva Bezier:")
for i, puntosBezier in enumerate(LR):
    print(f"Punto {i}: ({puntosBezier[0]:.3f}, {puntosBezier[1]:.3f})")
