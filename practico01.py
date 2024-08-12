import pandas as pd
import numpy as np

# Configurar la semilla para reproducibilidad
np.random.seed(42)

# Generar datos de peso y estatura
def generate_data(num_samples=100):
    weights = np.random.uniform(50, 100, num_samples)  # Peso en kg
    heights = np.random.uniform(1.5, 2.0, num_samples)  # Estatura en metros
    
    # Evitar combinaciones extremas
    for i in range(num_samples):
        if heights[i] < 1.6 and weights[i] > 80:
            weights[i] = np.random.uniform(50, 80)
        elif heights[i] > 1.9 and weights[i] < 60:
            weights[i] = np.random.uniform(60, 100)
    
    return weights, heights

weights, heights = generate_data()

# Crear DataFrame
df = pd.DataFrame({
    'Peso': weights,
    'Estatura': heights
})

# Guardar en archivo CSV
df.to_csv('datos.csv', index=False)

print("Datos generados y guardados en 'datos.csv'.")