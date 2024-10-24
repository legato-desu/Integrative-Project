from commons import *

window = tk.Tk()
window.title("Graficador de Funciones")
window.geometry("320x180")
window.configure(bg='lightgray')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

texto_funcion1 = ttk.Label(window, text="Funcion 1:", background='lightgray', font=("Arial", 10, "bold"))
texto_funcion1.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

entrada_texto1 = ttk.Entry(window, font=("Arial", 10))
entrada_texto1.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10, ipadx=30)

texto_funcion2 = ttk.Label(window, text="Funcion 2:", background='lightgray', font=("Arial", 10, "bold"))
texto_funcion2.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

entrada_texto2 = ttk.Entry(window, font=("Arial", 10))
entrada_texto2.grid(column=1, row=2, sticky=tk.W, padx=10, pady=10, ipadx=30)

def on_graficar():
    funcion1 = entrada_texto1.get()
    funcion2 = entrada_texto2.get()
    graficar(funcion1, funcion2)

informacion_texto = tk.Label(window, text="Andres Julian Granja \t\tIvan David Miranda", 
                            background='lightgray', font=("Arial", 8), fg="black", anchor="w")
informacion_texto.grid(column=0, row=4, columnspan=2, sticky=tk.W, padx=10, pady=5)

boton_graficar = ttk.Button(window, text="GRAFICAR", width=10, command=on_graficar)
boton_graficar.grid(column=1, row=3, sticky=tk.E, padx=10, pady=10)

boton_salir = ttk.Button(window, text="SALIR", width=10, command=window.quit)
boton_salir.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

window.mainloop()