Nombres: Nikolai Panchi, Josue Monta
Python version 3.11
Calculadora de Raíz Cuadrada
Este script en Python calcula la raíz cuadrada de un número ingresado por el usuario. Maneja números positivos y cero, y muestra un mensaje de error para números negativos.

Requisitos
Python 3.11
No se requieren paquetes adicionales de Python.

Uso

Clonar el repositorio:
git clone https://github.com/tu_usuario/calculadora-raiz-cuadrada.git

Navegar al directorio del proyecto:
cd calculadora-raiz-cuadrada

Ejecutar el script:
python calculadora_raiz_cuadrada.py
Sigue las instrucciones en pantalla para ingresar un número.

Ejemplo:
Si ingresas 9, el resultado será:
La raíz cuadrada de 9.0 es 3.00

Si ingresas -5, el resultado será:
No se puede calcular la raíz cuadrada de un número negativo.

Explicación del Código
Archivos
calculadora_raiz_cuadrada.py: Contiene el código en Python para calcular la raíz cuadrada.
Funciones
calcular_raiz_cuadrada(numero):

Calcula la raíz cuadrada del número dado usando math.sqrt().
Retorna None si el número es negativo, indicando que la raíz cuadrada no está definida para números negativos.
main():

Maneja la entrada del usuario y llama a calcular_raiz_cuadrada() para computar la raíz cuadrada.
Imprime el resultado o un mensaje de error si corresponde.
Manejo de Errores
El script verifica si el número ingresado es negativo y maneja este caso informando al usuario que la raíz cuadrada de números negativos no está definida.
Notas Adicionales
Asegúrate de tener instalado Python 3.x en tu sistema para ejecutar el script.
El script utiliza el módulo estándar math de Python para cálculos matemáticos.

Se adjunta captura de la ejecucción del archivo
![image](https://github.com/Josue-Monta/Python_square/assets/169925944/715eb13c-af09-4a86-a096-408243340a17)

