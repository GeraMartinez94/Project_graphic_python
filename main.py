import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo CSV
archivo_csv = 'datos.csv'
datos = pd.read_csv(archivo_csv)

# Mostrar gráfico de torta
plt.pie(datos['valor'], labels=datos['categoria'], autopct='%1.1f%%', startangle=90, colors=['blue', 'orange', 'green', 'red', 'purple'])
plt.axis('equal')  # Igualar la proporción asegura que la torta se dibuje como un círculo.

plt.title('Gráfico de Torta desde datos CSV')
plt.show()
