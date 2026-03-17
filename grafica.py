import matplotlib.pyplot as plt

# Datos (tamaño en KB vs latencia en ns)

sizes_kb = [
    4, 32, 256, 8192, 65536
]

latency_ns = [
    4.5,   # promedio 4K
    5.0,   # promedio 32K
    6.5,   # promedio 256K
    7.0,   # promedio 8M
    8.5    # promedio 64M
]

plt.figure()
plt.plot(sizes_kb, latency_ns, marker='o')

plt.xlabel("Tamaño del bloque (KB)")
plt.ylabel("Latencia (ns)")
plt.title("Latencia de memoria vs tamaño de bloque")

plt.xscale("log")  # MUY IMPORTANTE (escala logarítmica)

plt.grid()
plt.show()
