import matplotlib.pyplot as plt

def ingresar_valores():
    valores = []
    while True:
        valor = input("Ingresa un valor (o 'fin' para terminar): ")
        if valor.lower() == 'fin':
            break
        try:
            valor = float(valor)
            valores.append(valor)
        except ValueError:
            print("Por favor, ingresa un valor numérico válido.")

    return valores

def mostrar_grafico_torta(valores):
    plt.pie(valores, autopct='%1.1f%%', startangle=90, colors=['blue', 'orange', 'green', 'red', 'purple'])
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Gráfico de Torta')
    plt.show()

def main():
    print("Ingresa valores para el gráfico de torta.")
    valores = ingresar_valores()

    if valores:
        mostrar_grafico_torta(valores)
    else:
        print("No se ingresaron valores para mostrar el gráfico.")

if __name__ == "__main__":
    main()
