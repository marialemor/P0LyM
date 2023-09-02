#comenzamos por crear el lector de archivos

def lector(input):
    archivo = open(input, mode="r")
    linea = archivo.read()
    
    #vamos a acondicionar el archivo de instrucciones
    
    espacio = linea.replace("\n"," ")
    tab = espacio.replace("\t"," ")
    
    revisar_sintaxis(tab)
    
    archivo.close()
    
def revisar_sintaxis (texto):
    instruccion = ""
    instruc = []
    corchetes = 0   
    for i in texto: 
        if i == "{":#verificar si empieza un bloque 
            corchetes += 1
        elif i == "}":     
            corchetes -= 1 
        if i != "" and i != ";" and i !="}" and i !="{":#separar comandos internos
            instruccion += i.lower()
        elif i == ";" or i == "}" or i == "{":#termina instruccion
            if instruccion != " ":#para que no meta instrucciones vacias
                instruc.append(instruccion)
                instruccion = ""       
    instruc.remove("")
    if corchetes == 0:
        try:
            i = 0
            correcto = 0
            while i < len(instruc):#recorrer instrucciones
                error = rev_instru(i,instruc)#verificar error
                
                if error != 0:    
                    print("La sintaxis NO es correcta!")
                    break 
                else:
                    correcto += 1
                i += 1
        except:
            print("La sintaxis NO es correcta!")
             
    if correcto == len(instruc):
        print("La sintaxis es correcta")          
    
def rev_instru(i, instruc):
    com_1par = ["walk","leap","turn","turnto","drop","get","grab","letgo",":","nop()"]
    com_2par = ["leap","walk","jump", "defvar","defproc"]
    cond = ["facing","can","not"]
    control = ["if","else", "while","repeat","times"]
    dirs = ["left","right","front","back"]
    D = ["left","right","around"]
    orient = ["north","south","east","west"]
    
    evaluar = instruc[i]
    evaluar = evaluar.replace(" ( ", "(")
    evaluar = evaluar.replace(" ) ", ")")
    evaluar = evaluar.replace("  ", "")
    print(instruc)
    evaluar = evaluar.split("(")
    print(evaluar)
    n = 0
    while n < len(evaluar):
        word = evaluar[n]
        error = 0
        v = bloque(n,evaluar,word, com_1par,com_2par,cond,control,dirs,orient,D)  
        if v != 0: 
            error += 1
            break
        n += 1
    return error

def bloque (n, ev, word, com_1par, com_2par, cond, control, dirs, orient,D):
    error = 0
    var = []
    word = word.split("(")
    wordmod = word[0].strip()
    
    if wordmod in com_1par:#verificar que los de 1 parametro esten bien
        if len(word) == 2:
            if wordmod == "walk" or wordmod == "leap" or wordmod == "drop" or wordmod == "leap" or wordmod == "get" or wordmod == "grab" or wordmod == "letgo":
                if n<len(ev) and (ev[n+1][-1]== ")"):
                    param = int(ev[n+1].replace(")",""))
                    if isinstance(param, int) == False:
                        error +=1
            elif wordmod == "turn":
                error = parametros(n,ev,D)
            elif wordmod == "turnto":
                error = parametros(n,ev,orient)
            elif wordmod == "nop":
                if ev[n+1] !=")":
                    error += 1                                 
    elif wordmod in com_2par:#verificar sintaxis de 2 param
        if wordmod == "defvar":
            name = ev[n+1]
            val = int(ev[n+2])
            if (isinstance(name,str) and isinstance(val,int)) == False:#ambos parametros sean lo que deben ser
                error +=1
                print("mal")
            var.append(val)
            print("bien")
        elif wordmod == "defproc":
            name = ev[n+1]
            if ev[n+2][0] != "(" or ev[-1][-1] != ")":
                error +=1
            print("bien")  

    return error

def parametros(n,ev,par):
    error = 0
    evv = ev[n+1].replace(")","")
    if (evv.strip() in par) == False:
        error += 1
    return error
                
x = input(".txt a revisar:")

lector(x)
    