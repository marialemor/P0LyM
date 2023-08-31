#comenzamos por crear el lector de archivos

def lector():
    
    input = input(".txt a revisar")
    archivo = open(input, mode="r")
    linea = archivo.read()
    
    #vamos a acondicionar el archivo de instrucciones
    
    espacio = linea.replace("\n"," ")
    tab = espacio.replace("\t"," ")
    
    revisar_sintaxis(tab)
    
    archivo.close()
    
def revisar_sintaxis (texto):
    return 7
    
def commands():
    simple_cmd = 