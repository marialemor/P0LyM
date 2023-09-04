import re

class RobotParser:
    def __init__(self):
        # Inicializamos un conjunto para rastrear los nombres de las variables.
        self.variables = set()
        
        # Inicializamos un diccionario para rastrear las definiciones de funciones.
        self.funciones = {}

    def analizar(self, programa):
        # Tokenizamos el programa utilizando expresiones regulares.
        tokens = re.findall(r'\S+', programa)

        # Comenzamos el análisis sintáctico del programa.
        if self.analizar_programa(tokens):
            print("La sintaxis es correcta.")
        else:
            print("Error de sintaxis.")

    def analizar_programa(self, tokens):
        # Verificamos si no quedan tokens para analizar, lo que significa que el programa está sintácticamente correcto.
        if not tokens:
            return True
        # Verificamos si el primer token es "definir", lo que indica una definición de variable o función.
        elif tokens[0] == "definir":
            return self.analizar_definicion(tokens[1:])
        # Verificamos si el primer token es el nombre de una función definida previamente.
        elif tokens[0] in self.funciones:
            return self.analizar_llamada_funcion(tokens)
        # Verificamos si el primer token es el nombre de una variable definida previamente.
        elif tokens[0] in self.variables:
            return self.analizar_asignacion(tokens)
        # Si ninguna de las condiciones anteriores se cumple, hay un error de sintaxis.
        else:
            return False

    def analizar_definicion(self, tokens):
        # Verificamos si hay suficientes tokens y si el tercer token es "=", lo que indica una definición válida.
        if len(tokens) < 3 or tokens[1] != "=":
            return False
        
        # Obtenemos el nombre de la variable o función.
        nombre = tokens[0]
        
        # Tomamos todos los tokens después del "=" como la expresión a analizar.
        expr = tokens[2:]
        
        # Agregamos el nombre a la lista de variables definidas.
        self.variables.add(nombre)
        
        # Llamamos recursivamente para analizar la expresión después de "=".
        return self.analizar_programa(expr)

    def analizar_llamada_funcion(self, tokens):
        # Verificamos si hay suficientes tokens y si el segundo token es "(", lo que indica el inicio de los argumentos de la función.
        if len(tokens) < 2 or tokens[1] != "(":
            return False
        
        # Obtenemos el nombre de la función.
        nombre_funcion = tokens[0]
        
        # Inicializamos una lista para los argumentos de la función.
        argumentos_funcion = []
        
        # Inicializamos una variable de profundidad para rastrear paréntesis.
        profundidad = 0
        
        # Inicializamos un contador para iterar a través de los tokens después del "(".
        i = 2
        
        # Iteramos a través de los tokens de los argumentos hasta encontrar el paréntesis de cierre correspondiente.
        while i < len(tokens):
            if tokens[i] == "(":
                profundidad += 1
            elif tokens[i] == ")":
                profundidad -= 1
            
            argumentos_funcion.append(tokens[i])
            i += 1
            
            # Si la profundidad llega a cero, hemos encontrado el paréntesis de cierre y terminamos.
            if profundidad == 0:
                break
        
        # Si la profundidad no es cero o hemos llegado al final de los tokens, hay un error de sintaxis.
        if profundidad != 0 or i == len(tokens):
            return False
        
        # Eliminamos el último ")" de la lista de argumentos.
        argumentos_funcion = argumentos_funcion[:-1]
        
        # Verificamos que la función llamada esté definida en self.funciones y llamamos recursivamente para analizar los argumentos de la función.
        if nombre_funcion not in self.funciones:
            return False
        
        return all(self.analizar_programa(argumentos_funcion))

    def analizar_asignacion(self, tokens):
        # Verificamos si hay suficientes tokens y si el segundo token es "=", lo que indica una asignación válida.
        if len(tokens) < 2 or tokens[1] != "=":
            return False
        
        # Llamamos recursivamente para analizar la expresión después de "=".
        return self.analizar_programa(tokens[2:])

if __name__ == "__main__":
    # Ejemplo de programa de robot.
    programa_robot = """
    defVar nom 0
    defVar x 0
    defVar y 0
    defVar one 0
    defProc putCB (c , b )
    {
        drop c ) ;
        letGo ( b ) ;
        walk( n )
    }
    defProc goNorth ()
    {
        wh i le can(walk(1 , north ) ) { walk(1 , north ) }
    }
    defProc goWest ()
    {
        if can(walk(1 , west ) ) { walk(1 , west ) } else nop ()
    }
    {  
        jump (3 ,3) ;
        putCB (2 ,1)
    }
    """

    # Creamos una instancia de RobotParser.
    analizador = RobotParser()
    
    # Llamamos al método analizar para analizar el programa de robot.
    analizador.analizar(programa_robot)