# Proyecto Integrador - Graficador de Funciones

Este proyecto es una aplicación gráfica desarrollada en Python que permite graficar funciones matemáticas. La aplicación utiliza la biblioteca `Tkinter` para crear una interfaz gráfica (GUI) desde donde se ingresan las funciones, y `Matplotlib` para graficarlas. Además, permite evaluar y graficar múltiples funciones de manera simultánea.

## Funcionalidades

- **Ingreso de Funciones**: Los usuarios pueden ingresar hasta dos funciones matemáticas en la interfaz.
- **Evaluación y Graficación**: El programa evalúa y grafica las funciones ingresadas dentro de un rango predefinido de valores para la variable `x`.
- **Manejo de errores**: Si no se ingresan funciones o si se intenta graficar una expresión inválida, se muestra un mensaje de error.
- **Salida Gráfica**: La salida gráfica incluye la representación de las funciones junto con los ejes y una cuadrícula.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto.
- **Tkinter**: Para crear la interfaz gráfica de usuario (GUI).
- **Matplotlib**: Para la visualización y graficación de las funciones.
- **Numpy**: Para la manipulación eficiente de datos numéricos.

## Estructura del Proyecto

```bash
- ├── integrador.
- │   ├── commons.py           # Codigo para almacenar los import y def.
- │   ├── grafico.py           # Código para graficar las funciones ingresadas.
- │   ├── ventana.py           # Código para ingresar las funciones.
- │   ├── README.md            # Descripción del proyecto.
- │   ├── requirements.txt     # Lista de dependencias necesarias.
```
## Cómo Ejecutar el Proyecto

### Requisitos previos

1. Asegurese de tener instalado Python en tu sistema.
2. Instale las dependencias necesarias ejecutando el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```
## Ejecución
1. Abra una terminal en el directorio raíz del proyecto.
2. Ejecute el archivo ventana.py para iniciar la interfaz gráfica:
   ```bash
   python integrador/ventana.py
3. Ingrese una o dos funciones matemáticas en los cuadros de texto y presiona el botón "GRAFICAR".
4. La gráfica se generará y se mostrará en una nueva ventana.

## Ejemplos de Uso

### Entrada
- Supongamos que ingresas las siguientes funciones en la interfaz gráfica:
- - sin(x)
- - x^2
### Salida
- La aplicación generará un gráfico con ambas funciones, mostrando la sinusoide de sin(x) y la parábola de x^2 dentro del rango de x de -10 a 10.

### Explicación:

- Bajo "Requisitos previos", menciona el archivo `requirements.txt` y el comando necesario para instalar las dependencias.
- También puede listar las bibliotecas (en este caso, `matplotlib` y `numpy`) para que quede claro qué se está instalando.

```bash
pip install matplotlib
pip install numpy
```

## Capturas de Pantalla
<img width="378" height="214" src= "https://github.com/user-attachments/assets/3bba4e60-c7bb-44a1-b3cc-23f87ef6aa49"/>
<img width="318" height="124" src= "https://github.com/user-attachments/assets/0c00c981-4ebb-4574-8466-88b90ae91d7f"/>
<img width="378" height="214" src= "https://github.com/user-attachments/assets/73fe1dd5-4e7f-4ad2-9c88-0bbc9e087715"/>
<img width="564" height="433" src= "https://github.com/user-attachments/assets/65f12f62-e076-4c2c-823e-e77432f03c11"/>

## Problemas Conocidos
- **Errores de sintaxis:** Si iingresa una función con un formato incorrecto, el programa no podrá graficarla.
- **Rango de gráficos:** Actualmente, las gráficas están limitadas a un rango de -10 a 10 tanto para x como para y. En futuras versiones se podría hacer ajustable.

## Contribuciones
Si desea contribuir al proyecto, sientase libre de hacer un fork y abrir un pull request. También puedes abrir un issue si encuentra algún bug o tiene sugerencias de mejoras.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.