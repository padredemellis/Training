'''
Objetivo: Aprender a trabajar con argumentos pasados al ejecutar el programa.

Instrucciones:

Importa el módulo sys
Crea una función main() que lea sys.argv
Si el primer argumento es "sumar", suma los dos siguientes argumentos
Si el primer argumento es "multiplicar", multiplica los dos siguientes
Imprime el resultado
Maneja errores si no se proporcionan suficientes argumentos
'''
import sys

def main():
    try:
        if len(sys.argv) < 4:
            print('Error no se proporcionaron suficientes argumentos')
            return
    
        operacion = sys.argv[1]
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
        
        if operacion == 'sumar':
            print(num1 + num2)
        elif operacion == 'multiplicar':
            print(num1 * num2)
        else:
            print('Solo debes sumar o multiplicar es facil ¿no lo entendiste?')
    except ValueError:
        print("Error: Los argumentos deben ser números válidos")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    main()