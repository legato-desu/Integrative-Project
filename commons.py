import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

def evaluar_funcion(funcion, x):
    funcion = funcion.replace("^", "**")
    funcion = funcion.replace("sin", "math.sin")
    funcion = funcion.replace("cos", "math.cos")
    funcion = funcion.replace("tan", "math.tan")

    return [eval(funcion, {"x": xi, "math": math, "np": np}) for xi in x]

def graficar(funcion1, funcion2):
    if not funcion1 and not funcion2:
        messagebox.showwarning("ERROR", "Debe ingresar al menos una función.")  
        return

    if funcion1 and not funcion2:
        subprocess.run(["py", "grafico.py", funcion1])  
    elif not funcion1 and funcion2:
        subprocess.run(["py", "grafico.py", funcion2])
    else:
        subprocess.run(["py", "grafico.py", funcion1, funcion2])
