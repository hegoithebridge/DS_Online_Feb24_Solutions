#IMPORTS
import numpy as np
import sys

# VARIABLES Y CONSTANTES GLOBALES
from variables import *

# DEFINICIÓN DE FUNCIONES
from funcion1 import *
from funcion2 import *
#from funciones import * 

# DEFINICIÓN DE CLASES
from claseA import *
#from clases import *


# CÓDIGO PRINCIPAL
def main():
    #args = sys.argv[1:]
    #for arg in args:
    #    print(f"Has llamado al main con argumento {arg}")

    print("Hello World!")
    
    print(f"La dimensión del tablero es {DIMENSION_TABLERO}")
    
    funcion1()
    print(funcion2(10,10))
    
    objeto = ClaseA()


if __name__ == '__main__':
    main()