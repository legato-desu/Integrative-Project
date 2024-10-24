from commons import *

def main():
    funciones = sys.argv[1:]

    x = np.linspace(-10, 10, 400)

    for funcion in funciones:
        y = evaluar_funcion(funcion, x)
        plt.plot(x, y, label=funcion)

    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.legend()
    plt.title("Graficador de Funciones")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()