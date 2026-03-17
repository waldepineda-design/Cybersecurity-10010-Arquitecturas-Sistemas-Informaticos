import numpy as np
import time
import random

# Tamaño del arreglo (se puede subir si se quiere más diferencia)
SIZE = 10_000_000

# Crear arreglo
array = np.zeros(SIZE, dtype=np.int32)

# -----------------------------
# Acceso secuencial
# -----------------------------
start = time.time()

for i in range(SIZE):
    array[i] += 1

end = time.time()
sequential_time = end - start

print(f"Tiempo acceso secuencial: {sequential_time:.4f} segundos")

# -----------------------------
# Acceso aleatorio
# -----------------------------
indices = list(range(SIZE))
random.shuffle(indices)

start = time.time()

for i in indices:
    array[i] += 1

end = time.time()
random_time = end - start

print(f"Tiempo acceso aleatorio: {random_time:.4f} segundos")
