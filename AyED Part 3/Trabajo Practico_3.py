import os, os.path, pickle, msvcrt, time
from datetime import datetime, date
from colorama import Fore, Back, Style, init
init(autoreset=True)

global cods, codLoc, comidaC, indumentariaC, perfumeriaC, localescreados
codLoc, comidaC, indumentariaC, perfumeriaC, localescreados = 0, 0, 0, 0, 0

# Integrantes Algoritmos y Estructuras de Datos 2023:
# Comision 110 - T.T
# Juan Manuel Foronda, Maximiliano Jesús Gomez

# codLoc, comidaC, indumentariaC, perfumeriaC, localescreados : int
# flag : boolean

# Definición de estructuras de datos
class Usuario:
    def __init__(self):
        self.codUsuario = 0
        self.nombreUsuario = ""
        self.claveUsuario = ""
        self.tipoUsuario = ""


class Local:
    def __init__(self):
        self.codLocal = 0
        self.nombreLocal = ""
        self.ubicacionLocal = ""
        self.rubroLocal = ""
        self.codUsuario = 0
        self.estado = "A"


class Promocion:
    def __init__(self):
        self.codPromo = 0
        self.textoPromo = ""
        self.fechaDesdePromo = ""
        self.fechaHastaPromo = ""
        self.diasSemana = [0]*7
        self.estado = ""
        self.codLocal = 0


class Novedad:
    def __init__(self):
        self.codNovedad = 0
        self.textoNovedad = ""
        self.fechaDesdeNovedad = ""
        self.fechaHastaNovedad = ""
        self.tipoUsuario = ""
        self.estado = "A"


class UsoPromocion:
    def __init__(self):
        self.codCliente = 0
        self.codPromo = 0
        self.fechaUsoPromo = ""


def cargar_usuarios():
    global cods, afusuario, alusuario
    afusuario = "c:\\tp3\\USUARIOS.dat"
    if not os.path.exists(afusuario):
        alusuario = open(afusuario, "w+b")
    else:
        alusuario = open(afusuario, "r+b")

    regUsuario = Usuario()
    regUsuario.codUsuario = 1
    cods = 1
    regUsuario.nombreUsuario = "admin@shopping.com".ljust(100)
    regUsuario.claveUsuario = "12345".ljust(8)
    regUsuario.tipoUsuario = "administrador".ljust(20)
    pickle.dump(regUsuario, alusuario)
    alusuario.flush()
    # Cargar usuarios desde el archivo USUARIOS.DAT
    

def cargar_locales():
    global aflocales, allocales
    aflocales = "c:\\tp3\\LOCALES.dat"
    if not os.path.exists(aflocales):
        allocales = open(aflocales, "w+b")
    else:
        allocales = open(aflocales, "r+b")
    # Cargar locales desde el archivo LOCALES.DAT
    

def cargar_promociones():
    global alpromociones, afpromociones
    afpromociones = "c:\\tp3\\PROMOCIONES.dat"
    if not os.path.exists(afpromociones):
        alpromociones = open(afpromociones, "w+b")
    else:
        alpromociones = open(afpromociones, "r+b")
    # Cargar promociones desde el archivo PROMOCIONES.DAT
    

def cargar_novedades():
    global afnovedades, alnovedades
    afnovedades = "c:\\tp3\\NOVEDADES.dat"
    if not os.path.exists(afnovedades):
        alnovedades = open(afnovedades, "w+b")
    else:
        alnovedades = open(afnovedades, "r+b")
    # Cargar novedades desde el archivo NOVEDADES.DAT
    

def cargar_usos_promocion():
    global afusopromo, alusopromo
    afusopromo = "c:\\tp3\\USO_PROMOCIONES.dat"
    if not os.path.exists(afusopromo):
        alusopromo = open(afusopromo, "w+b")
    else:
        alusopromo = open(afusopromo, "r+b")
    # Cargar usos de promociones desde el archivo USO_PROMOCIONES.DAT
    
    
def validarEnteros(nro, min, max):
    try:
        nro = int(nro)
        if nro >= min and nro <= max:
            return False
        else:
            return True
    except:
        return True
    

def BuscarCon(nom, con):
    global afusuario, alusuario
    intentos = 3
    t = os.path.getsize(afusuario)
    pos = 0
    
    while intentos > 1:
        alusuario.seek(0, 0)  
        encontrado = False
        
        while alusuario.tell() < t:
            vrUsu = pickle.load(alusuario)            
            if vrUsu.nombreUsuario == nom.ljust(100) and vrUsu.claveUsuario == con.ljust(8):
                return vrUsu.tipoUsuario            
            pos = alusuario.tell()
        
        if not encontrado:
            print(f"\n{Fore.RED+Style.BRIGHT}Nombre de usuario o contraseña incorrectos")
            intentos -= 1
            print(f"Quedan {Fore.RED+Style.BRIGHT}{intentos}{Style.RESET_ALL} intentos. Intente nuevamente.")
            nom = input("\nIngrese su nombre de usuario: ")
            con = ocultar("Ingrese su contraseña: ")
    
    print(f"\n{Fore.RED+Style.BRIGHT}Se agotaron los intentos, acceso denegado.")
    return None


def Buscar(nom):
    global afusuario, alusuario
    t = os.path.getsize(afusuario)
    pos=0
    alusuario.seek(0, 0)  
    vrUsu = Usuario()
    if t>0:
        vrUsu = pickle.load(alusuario)
        while (alusuario.tell()<t) and (nom != vrUsu.nombreUsuario):
            pos = alusuario.tell()
            vrUsu = pickle.load(alusuario)
        if vrUsu.nombreUsuario == nom:        
         return pos
        else:
         return -1
    else:
        return -1
       
        
def ocultar(contra):
    print(contra, end='', flush=True)
    password = []
    
    for i in range(100):  #Maximo 100 caracteres
        char = msvcrt.getch()
        
        if char == b'\r' or char == b'\n':
            password_str = b''.join(password).decode('utf-8')
            print('')  #En caso de que se apriete en enter
            return password_str
        
        elif char == b'\x08':  #En caso de que se apriete borrar
            if password:
                password.pop()
                print('\b \b', end='', flush=True)
        
        else:
            password[i:i+1] = [char] 
            print('*', end='', flush=True)


def BuscaDico(nom):
 global aflocales, allocales 
 if (os.path.getsize(aflocales)) == 0:
     return -1
 else:
     allocales.seek (0, 0)
     aux = pickle.load(allocales)
     tamReg = allocales.tell() 
     cantReg = int(os.path.getsize(aflocales) / tamReg)
     inferior = 0
     superior = cantReg-1
     medio = (inferior + superior) // 2 					
     allocales.seek(medio*tamReg, 0)
     regLoc= pickle.load(allocales) 					
     while str(regLoc.nombreLocal)!= nom and (inferior < superior):
         if nom < str(regLoc.nombreLocal):
             superior = medio - 1
         else:
             inferior = medio + 1
         medio = (inferior + superior) // 2 
         allocales.seek(medio*tamReg, 0)
         regLoc= pickle.load(allocales)
     if str(regLoc.nombreLocal) == nom:						
         return medio*tamReg							
     else:
         return -1


def buscar_Cod_dueño(cod):
    global afusuario, alusuario
    regUsu = Usuario()
    t = os.path.getsize(afusuario)
    alusuario.seek(0, 0)
    regUsu = pickle.load(alusuario)
    while alusuario.tell() < t and regUsu.codUsuario != cod:
        pos = alusuario.tell()
        regUsu = pickle.load(alusuario)
    if regUsu.codUsuario == cod:
        if regUsu.tipoUsuario == "Dueño de local".ljust(20):
            return pos
        else:
            return -1
    else:
        return -1


def buscar_Cod_promo(cod, desde, hasta):
    global afusopromo, alusopromo
    reg = UsoPromocion()
    t = os.path.getsize(afusopromo)
    alusopromo.seek(0, 0)
    uso = 0
    while alusopromo.tell() < t:
        reg = pickle.load(alusopromo)
        if reg.codPromo == cod and reg.fechaUsoPromo >= desde.strftime("%d/%m/%Y") and reg.fechaUsoPromo <= hasta.strftime("%d/%m/%Y"):
            uso += 1
    return uso


def buscar_promo_por_cod(cod):
    global afpromociones, alpromociones
    reg = Promocion()
    t = os.path.getsize(afpromociones)
    alpromociones.seek(0, 0)
    while alpromociones.tell() < t and reg.codPromo != cod:
        pos = alpromociones.tell()
        reg = pickle.load(alpromociones)
    if reg.codPromo == cod:
        return pos
    else:
        return -1


def buscar_Cod_local(cod):
    global aflocales, allocales
    reg = Local()
    t = os.path.getsize(aflocales)
    allocales.seek(0, 0)
    while allocales.tell() < t and reg.codLocal != cod:
        pos = allocales.tell()
        reg = pickle.load(allocales)
    if reg.codLocal == cod:
        return pos
    else:
        return -1


def buscar_local_por_cod(cod):
    global aflocales, allocales
    reg = Local()
    t = os.path.getsize(aflocales)
    allocales.seek(0, 0)
    while allocales.tell() < t and reg.codUsuario != cod:
        pos = allocales.tell()
        reg = pickle.load(allocales)
    if reg.codUsuario == cod:
        return pos
    else:
        return -1
  
    
def cargaCod():
    global alusuario, afusuario
    reg = Usuario()
    aux = Usuario()
    alusuario.seek(0, 0)
    t = os.path.getsize(afusuario)
    alusuario.seek(0,0)
    reg = pickle.load(alusuario)
    tamReg = alusuario.tell()
    cantReg= t//tamReg
    alusuario.seek ((cantReg-1)*tamReg,0)
    aux = pickle.load(alusuario)
    ultimo= int(aux.codUsuario)
    reg.codUsuario= ultimo +1
    return reg.codUsuario


def cargaCodLocal():
    global allocales, aflocales
    reg = Local()
    aux = Local()
    allocales.seek(0, 0)
    t = os.path.getsize(aflocales)
    allocales.seek(0, 0)

    if t == 0:
        reg.codLocal = 1
    else:
        reg = pickle.load(allocales)
        tamReg = allocales.tell()
        cantReg = t // tamReg
        allocales.seek((cantReg - 1) * tamReg, 0)
        aux = pickle.load(allocales)
        ultimo = int(aux.codLocal)
        reg.codLocal = ultimo + 1
    codLoc = reg.codLocal

    return codLoc


def confirmar(sec):
    print(f'\n¿Está seguro de que desea ingresar a [ {Fore.MAGENTA+Style.BRIGHT}{sec}{Style.RESET_ALL} ] ?') 
    Confirmacion=str(input(f'{Style.RESET_ALL}\nIngrese {Fore.RED+Style.BRIGHT}*{Style.RESET_ALL} para {Fore.RED+Style.BRIGHT}Salir{Style.RESET_ALL} o pulse la tecla {Fore.GREEN+Style.BRIGHT}ENTER{Style.RESET_ALL} para continuar: ').upper())
    while(Confirmacion!='*' and Confirmacion!=''):
        print('')
        Confirmacion=str(input(Fore.RED+Style.BRIGHT+f'Opción incorrecta, intentalo nuevamente{Style.RESET_ALL}: ').upper())  
    if (Confirmacion =='*'):
        return -1
    elif (Confirmacion==''):
        return 0
    

def mostrar_locales():
    global aflocales, allocales
    regLoc = Local()
    t = os.path.getsize(aflocales)
    if t == 0:
        print(f"\n{Fore.RED+Style.BRIGHT}No hay locales cargados en este momento.")
    else:
        allocales.seek(0, 0)
        regLoc = pickle.load(allocales)
        tamReg = allocales.tell()
        cantReg = int(t // tamReg)
        for i in range(0, cantReg-1):
            for j in range(i+1, cantReg):
                allocales.seek(i*tamReg, 0)
                auxi = pickle.load(allocales)
                allocales.seek(j*tamReg, 0)
                auxj = pickle.load(allocales)
                if (str(auxi.nombreLocal) > str(auxj.nombreLocal)):
                    allocales.seek(i*tamReg, 0)
                    pickle.dump(auxj, allocales)
                    allocales.seek(j*tamReg, 0)
                    pickle.dump(auxi, allocales)
                    allocales.flush()        
        print("\n----Locales cargados hasta el momento----")
        allocales.seek(0, 0)
        while allocales.tell()<t:
            regLoc = pickle.load(allocales)
            print(Fore.BLUE+Style.BRIGHT+f"\nNombre: {Style.RESET_ALL}",regLoc.nombreLocal,
                  Fore.BLUE+Style.BRIGHT+f"\nUbicacion: {Style.RESET_ALL} ", regLoc.ubicacionLocal,
                  Fore.BLUE+Style.BRIGHT+f"\nRubro: {Style.RESET_ALL}", regLoc.rubroLocal,                    
                  Fore.BLUE+Style.BRIGHT+f"\nCodigo del dueño: {Style.RESET_ALL}", regLoc.codUsuario,
                  Fore.BLUE+Style.BRIGHT+f"\nCodigo del local: {Style.RESET_ALL}", regLoc.codLocal,
                  Fore.GREEN+Style.BRIGHT+f"\nActivo(A) {Style.RESET_ALL}", "/// ", Fore.RED+Style.BRIGHT+f"Dado de baja(B): {Style.RESET_ALL}", regLoc.estado)

    
def crear_locales():
    global aflocales, allocales, codLoc, perfumeriaC, indumentariaC, comidaC, localescreados
    os.system("cls")
    mostrar_locales()
    seguro = confirmar('Crear Locales')
    if (seguro == 0):
        print(f'\n{Fore.BLUE+Style.BRIGHT}Entrando a [ Crear Locales ] ...{Style.RESET_ALL}')
        time.sleep(2)
        os.system("cls")
        mostrar_locales()
        print(f"\n{Fore.GREEN+Style.BRIGHT}---- Crear un local ---- {Style.RESET_ALL}")
        regLoc = Local()
        regLoc.nombreLocal = input("\nIngrese el nombre del local: ").capitalize().ljust(50)
        while BuscaDico(regLoc.nombreLocal) != -1:
            regLoc.nombreLocal = input(f"\n{Fore.RED+Style.BRIGHT}Ya existe un local con ese nombre, intente de nuevo:{Style.RESET_ALL} ").capitalize().ljust(50)
        regLoc.ubicacionLocal = input("Ingrese la ubicación del local: ").ljust(50)
        regLoc.rubroLocal = input("Ingrese el rubro del local(indumentaria, comida o perfumería): ").ljust(50)
        while regLoc.rubroLocal != "comida".ljust(50) and regLoc.rubroLocal != "indumentaria".ljust(50) and regLoc.rubroLocal != "perfumería".ljust(50):
            regLoc.rubroLocal = input(f"\n{Fore.RED+Style.BRIGHT}Rubro no existente. Ingrese un rubro válido:{Style.RESET_ALL} ")
        if regLoc.rubroLocal == "comida".ljust(50):
             comidaC = comidaC + 1
        elif regLoc.rubroLocal == "indumentaria".ljust(50):
             indumentariaC = indumentariaC +1
        elif regLoc.rubroLocal == "perfumería".ljust(50):
             perfumeriaC = perfumeriaC + 1
        regLoc.codUsuario = int(input("Ingrese el codigo del dueño del local: "))
        while buscar_Cod_dueño(regLoc.codUsuario) == -1:
            regLoc.codUsuario = int(input(f"{Fore.RED+Style.BRIGHT}Código de dueño inválido o no existente, intente de nuevo:{Style.RESET_ALL} "))
        aux = Local()
        allocales.seek(0, 0)
        t = os.path.getsize(aflocales)
        allocales.seek(0, 0)
        if t == 0:
            regLoc.codLocal = 1
        else:
            aux = pickle.load(allocales)
            tamReg = allocales.tell()
            cantReg = t // tamReg
            regLoc.codLocal = cantReg + 1
        regLoc.codLocal = str(regLoc.codLocal)
        regLoc.codLocal = regLoc.codLocal.ljust(3)
        regLoc.estado = "A"
        localescreados += 1
        t = os.path.getsize(aflocales)
        allocales.seek(0, 2)
        pickle.dump(regLoc, allocales)
        allocales.flush()
        allocales.seek(0, 0)
        regLoc = pickle.load(allocales)
        tamReg = allocales.tell()
        cantReg = int(t // tamReg)
        for i in range(0, cantReg-1):
                for j in range(i+1, cantReg):
                    allocales.seek(i*tamReg, 0)
                    auxi = pickle.load(allocales)
                    allocales.seek(j*tamReg, 0)
                    auxj = pickle.load(allocales)
                    if (str(auxi.nombreLocal) > str(auxj.nombreLocal)):
                        allocales.seek(i*tamReg, 0)
                        pickle.dump(auxj, allocales)
                        allocales.seek(j*tamReg, 0)
                        pickle.dump(auxi, allocales)
                        allocales.flush()       

        print(f"{Fore.GREEN+Style.BRIGHT}\nLocal creado exitosamente!{Style.RESET_ALL}\n")

        print("---- RUBROS ----")    
        RUBROSSTR = ["Comida", "Indumentaria", "Perfumería"]
        RUBROSINT = [comidaC, indumentariaC, perfumeriaC]
        n = 3
        for i in range(n-1):
            for j in range(i+1, n):
                if RUBROSINT[i] < RUBROSINT[j]:
                    au = RUBROSINT[i]
                    au2 = RUBROSSTR[i]
                    RUBROSINT[i] = RUBROSINT[j]
                    RUBROSSTR[i] = RUBROSSTR[j]
                    RUBROSINT[j] = au
                    RUBROSSTR[j] = au2
        print()
        print(RUBROSSTR[0], "tiene", RUBROSINT[0], "locales")
        print()
        print(RUBROSSTR[1], "tiene", RUBROSINT[1], "locales")
        print()
        print(RUBROSSTR[2], "tiene", RUBROSINT[2], "locales")
        print()
        input("Digite cualquier tecla para salir: ")
    elif (seguro == -1):
        print(Fore.GREEN+Style.BRIGHT+'\nVolviendo al menu anterior!\n')
        time.sleep(2)
        os.system("cls")
    

def modificar_local():
    global aflocales, allocales
    os.system("cls")
    mostrar_locales()
    seguro = confirmar('Modificar Local')
    if (seguro == 0):
        print(f'\n{Fore.BLUE+Style.BRIGHT}Entrando a [ Modificar Local ] ...{Style.RESET_ALL}')
        time.sleep(2)
        os.system("cls")
        regLoc = Local()
        print(f"\n{Fore.YELLOW+Style.BRIGHT}---- Modificar un local ----{Style.RESET_ALL}")
        mostrar_locales()
        local = str(input("\nIngrese el codigo de local a modificar: ")).ljust(3)
        posi = buscar_Cod_local(local)
        while posi == -1:
            local = str(input(f"{Fore.RED+Style.BRIGHT}Código de local no existente, intente de nuevo:{Style.RESET_ALL} ")).ljust(3)
            posi = buscar_Cod_local(local)
        allocales.seek(posi, 0)
        regLoc = pickle.load(allocales)
        print("---- Local a modificar ---")
        print("Nombre: ", regLoc.nombreLocal)
        print("Ubicación: ", regLoc.ubicacionLocal)
        print("Rubro: ", regLoc.rubroLocal)
        localcod = regLoc.codLocal
        usu = regLoc.codUsuario
        opc = "S"
        if regLoc.estado == "B":
            opc = input(f"{Fore.RED+Style.BRIGHT}\nEl local seleccionado está dado de baja{Style.RESET_ALL}, deseas activarlo? (S/N): ").upper()
            while opc != "S" and opc != "N":
                opc = input(f"{Fore.RED+Style.BRIGHT}Opción no válida. Ingrese S para activarlo o N para volver:{Style.RESET_ALL} ").upper()
        while opc != "N":
            nombre = input("Ingrese el nuevo nombre del local(Enter para mantener el actual): ").capitalize()
            ubi = input("Ingrese la nueva ubicacion del local(Enter para mantener la acutal): ")
            rubro = input("Ingrese el rubro del local(Enter para mantener el actual): ")
            while rubro != "comida" and rubro != "indumentaria" and rubro !="perfumería" and rubro != "":
                rubro = input(f"{Fore.RED+Style.BRIGHT}Rubro inválido, intente de nuevo(comida, perfumería o indumentaria):{Style.RESET_ALL} ")
            if nombre != "":
                nombre = nombre.ljust(50)
                regLoc.nombreLocal = nombre
            if ubi != "":
                ubi = ubi.ljust(50)
                regLoc.ubicacionLocal = ubi
            if rubro != "":
                rubro = rubro.ljust(50)
                regLoc.rubroLocal = rubro
            regLoc.codLocal = localcod
            regLoc.codUsuario = usu
            allocales.seek(posi, 0)
            pickle.dump(regLoc, allocales)
            allocales.flush()
            print(f"{Fore.GREEN+Style.BRIGHT}Local modificado exitosamente!{Style.RESET_ALL}")
            opc = "N"
        print(f"{Fore.RED+Style.BRIGHT}Volviendo...{Style.RESET_ALL}")
        time.sleep(3)
    elif (seguro == -1):
        print(Fore.GREEN+Style.BRIGHT+'\nVolviendo al menu anterior!\n')
        time.sleep(2)
        os.system("cls")
    

def eliminar_local():
    global aflocales, allocales, comidaC, indumentariaC, perfumeriaC
    os.system("cls")
    mostrar_locales()
    seguro = confirmar('Eliminar Local')
    if (seguro == 0):   
        print(f'\n{Fore.BLUE+Style.BRIGHT}Entrando a [ Eliminar Local ] ...{Style.RESET_ALL}')
        time.sleep(2)
        os.system("cls")
        regLoc = Local()
        print(f"{Fore.RED+Style.BRIGHT}----Eliminar local----{Style.RESET_ALL}")
        mostrar_locales()
        local = str(input("\nIngrese el codigo de local a eliminar: ")).ljust(3)
        posi = buscar_Cod_local(local)
        while posi == -1:
            local = str(input(f"\n{Fore.RED+Style.BRIGHT}Código de local no existente, intente de nuevo:{Style.RESET_ALL} ")).ljust(3)
            posi = buscar_Cod_local(local)
        allocales.seek(posi, 0)
        regLoc = pickle.load(allocales)
        if regLoc.estado == "A":
            print("----Local a eliminar---")
            print("Nombre: ", regLoc.nombreLocal)
            print("Ubicación: ", regLoc.ubicacionLocal)
            print("Rubro: ", regLoc.rubroLocal)
            op = input(f"\n{Fore.RED+Style.BRIGHT}Está seguro que quiere dar de baja este local? (S/N): {Style.RESET_ALL}").upper()
            while op != "S" and op !="N":
                op = input(f"\n{Fore.RED+Style.BRIGHT}Opcion invalida, ingrese S para eliminar el local o N para volver:{Style.RESET_ALL} ").upper()
            if op == "S":
                if regLoc.rubroLocal == "comida".ljust(50):
                    comidaC -= 1
                elif regLoc.rubroLocal == "indumentaria".ljust(50):
                    indumentariaC -= 1
                elif regLoc.rubroLocal == "perfumería".ljust(50):
                    perfumeriaC -= 1
                regLoc.estado = "B"
                allocales.seek(posi, 0)
                pickle.dump(regLoc, allocales)
                allocales.flush()
                print(f"\n{Fore.RED+Style.BRIGHT}Local dado de baja exitosamente.{Style.RESET_ALL}")   
                time.sleep(2)
            else:
                print(f"\n{Fore.RED+Style.BRIGHT}Volviendo...{Style.RESET_ALL}")
                time.sleep(2)
        else:
            print(f"\n{Fore.RED+Style.BRIGHT}El local seleccionado ya esta dado de baja{Style.RESET_ALL}, para modificarlo, dirigirse a -Modificar local-")
            time.sleep(2)
            
    elif (seguro == -1):
        print(Fore.GREEN+Style.BRIGHT+'\nVolviendo al menu anterior!\n')
        time.sleep(2)
        os.system("cls")


def mostrar_mapa_locales():
    global aflocales, allocales, localescreados
    os.system('cls')
    print("\n+--------+---- Mapa de Locales -----+--------+")
    filas, cols = 10, 5
    mapa_locales = [[' ' for _ in range(cols)] for _ in range(filas)]

    allocales.seek(0, 0)
    reg = pickle.load(allocales)
    tamReg = allocales.tell()
    t = os.path.getsize(aflocales)
    cantReg = t // tamReg
    allocales.seek(0, 0)
    for i in range(cantReg):
        regLoc = pickle.load(allocales) 
        fila = i // cols
        columna = i % cols
        if regLoc.estado == "A":
            mapa_locales[fila][columna] = regLoc.codLocal.strip()
        elif regLoc.estado == "B":
            mapa_locales[fila][columna] = "  " + regLoc.codLocal.strip()

    for fila in mapa_locales:
        print("+" + "+".join(["-" * 8 for _ in range(cols)]) + "+")
        for codigo in fila:
            if codigo.startswith("  "):
                color = Back.RED + Fore.BLACK
            else:
                color = Back.YELLOW + Fore.BLACK
                if codigo != ' ':
                    color = Back.GREEN + Fore.BLACK
            print(f"{color}{codigo:^8}", end="")
            print("|", end="")
        print()
    print("+" + "+".join(["-" * 8 for _ in range(cols)]) + "+")
    print(f"Note que los locales en {Fore.RED+Style.BRIGHT}rojo{Style.RESET_ALL} están dados de baja, mientras que los {Fore.GREEN+Style.BRIGHT}verdes{Style.RESET_ALL} están activos")
    input("Digite cualquier tecla para volver: ")
    pantalla1()
    time.sleep(4)


def gestionar_locales(): 
 Opci = '' 
 while (Opci.upper() != 'E'):
        os.system('cls')
        print(f"{Fore.CYAN+Style.BRIGHT}-----------{Style.RESET_ALL} Gestión de locales {Fore.CYAN+Style.BRIGHT}--------------")
        print(F"\n{Fore.GREEN+Style.BRIGHT}a{Style.RESET_ALL}. Crear locales")
        print(F"{Fore.YELLOW+Style.BRIGHT}b{Style.RESET_ALL}. Modificar local")
        print(F"{Fore.RED+Style.BRIGHT}c{Style.RESET_ALL}. Eliminar local")
        print(F"{Fore.MAGENTA+Style.BRIGHT}d{Style.RESET_ALL}. Mapa de locales")
        print(F"{Fore.RED+Style.BRIGHT}e{Style.RESET_ALL}. Volver")  
        print(Fore.CYAN+Style.BRIGHT + '\n---------------------------------------------')
        Opci = str(input('\nIngrese la opción que desea operar: ').upper())
        while (Opci<'A' or Opci>'D') and (Opci!='E'):
            Opci = str(input(f'{Fore.RED+Style.BRIGHT}Opción incorrecta {Style.RESET_ALL}- Entre A y E [E para Volver]:{Style.RESET_ALL} ').upper())
        if Opci == "A":
            crear_locales() 
        elif Opci == "B":
            modificar_local() 
        elif Opci == "C":
            eliminar_local() 
        elif Opci == "D":
            mostrar_mapa_locales()


def crear_dueños(): 
    os.system("cls")
    seguro = confirmar('Registrar Dueños')
    if (seguro == 0):
        print(f'\n{Fore.BLUE+Style.BRIGHT}Entrando a [ Registrar Dueños ] ...{Style.RESET_ALL}')
        time.sleep(2)
        os.system("cls")
        global cods, afusuario, alusuario
        print(f"{Fore.BLUE+Style.BRIGHT}-----------{Style.RESET_ALL} Registrar Dueño {Fore.BLUE+Style.BRIGHT}--------------")
        correo = input("\nIngrese su correo electronico: ").ljust(100)
        regUsuario = Usuario()
        while Buscar(correo) != -1:
            correo = input(f"{Fore.RED+Style.BRIGHT}Ya existe un usuario con ese correo, vuelva a intentarlo {Style.RESET_ALL}: ")
        regUsuario.codUsuario = cargaCod()
        regUsuario.nombreUsuario = correo
        clave = ocultar("Ingrese su contraseña(8 caracteres): ")
        while len(clave) != 8:
            clave = ocultar(f"{Fore.RED+Style.BRIGHT}La clave debe tener 8 caracteres, intente de nuevo {Style.RESET_ALL}: ")
        regUsuario.claveUsuario = clave
        print(f"\nEl codigo de este dueño es: {regUsuario.codUsuario}")
        regUsuario.tipoUsuario = "Dueño de local".ljust(20)
        alusuario.seek(0, 2)
        pickle.dump(regUsuario, alusuario)
        alusuario.flush()
        print("\n-------------------------------------------")
        print(f"|{Fore.GREEN+Style.BRIGHT} Dueño de local registrado correctamente {Style.RESET_ALL}|")
        print ("-------------------------------------------\n")
        time.sleep(2)
        
    elif (seguro == -1):
        print(Fore.GREEN+Style.BRIGHT+'\nVolviendo al menu anterior!\n')
        time.sleep(2)
        os.system("cls")


def aprobar_descuento():
    
    global afpromociones, alpromociones, aflocales, allocales
    regPromo = Promocion()
    regLocal = Local()
    os.system("cls")
    seguro = confirmar('Aprobar/Denegar Solicitud de Descuentos')
    if (seguro == 0):
        print(f'\n{Fore.BLUE+Style.BRIGHT}Entrando a [ Aprobar/Denegar Solicitud de Descuentos ] ...{Style.RESET_ALL}')
        time.sleep(2)
        os.system("cls")
        print(f"{Fore.GREEN+Style.BRIGHT}---- Promociones ----{Style.RESET_ALL}")
        t = os.path.getsize(afpromociones)
        alpromociones.seek(0, 0)
        if t == 0:
            print(f"{Fore.RED+Style.BRIGHT}No existen promociones{Style.RESET_ALL}")
        else:
            while alpromociones.tell() < t:
                regPromo = pickle.load(alpromociones)
                if regPromo.estado == "pendiente".ljust(10):
                    print("-" * 20)
                    print("Codigo de promoción: ", regPromo.codPromo, "\nTexto: ", regPromo.textoPromo, "\nFecha de inicio: ", regPromo.fechaDesdePromo,
                           "\nFecha final: ", regPromo.fechaHastaPromo, "\nCodigo del local: ", regPromo.codLocal,)
                    pos = buscar_Cod_local(regPromo.codLocal)
                    allocales.seek(pos, 0)
                    regLocal = pickle.load(allocales)
                    print("Nombre del local: ", regLocal.nombreLocal)
                    print("-" * 20)
            cod = str(input("\nIngrese un codigo de promoción para ser aceptado o rechazado: "))
            cod = cod.ljust(3)
            pos = buscar_promo_por_cod(cod)
            while pos == -1:
                cod = str(input(f"{Fore.RED+Style.BRIGHT}\nCodigo de promoción inexistente, intente de nuevo:{Style.RESET_ALL} "))
                cod = cod.ljust(3)
                pos = buscar_promo_por_cod(cod)
            alpromociones.seek(pos, 0)
            regPromo = pickle.load(alpromociones)
            if regPromo.estado != "pendiente".ljust(10):
                print(f"\n{Fore.YELLOW+Style.BRIGHT}La promoción seleccionada no se encuentra en estado pendiente, volviendo...{Style.RESET_ALL}")
            else:
                opc = input("\nIngrese A para aceptar la promoción seleccionada o R para rechazarla: ").upper()
                while opc != "A" and opc != "R":
                    opc = input(f"\n{Fore.RED+Style.BRIGHT}Opción inválidañ{Style.RESET_ALL}, ingrese A para aceptar o R para rechazar: ")
                if opc == "A":
                    regPromo.estado = "aprobada".ljust(10)
                else:
                    regPromo.estado = "rechazada".ljust(10)
                alpromociones.seek(pos, 0)
                pickle.dump(regPromo, alpromociones)
                alpromociones.flush()
                print(f"\n{Fore.GREEN+Style.BRIGHT}Actualización exitosa, volviendo...{Style.RESET_ALL}")
        time.sleep(2)
        
    elif (seguro == -1):
        print(Fore.GREEN+Style.BRIGHT+'\nVolviendo al menu anterior!\n')
        time.sleep(2)
        os.system("cls")
                             

def construccion():
    print(f"\n{Fore.YELLOW}Esta funcionalidad esta Diagramada en chapin")
    print(f'\n{Fore.GREEN+Style.BRIGHT}Volviendo...{Style.RESET_ALL}')
    time.sleep(2)


def mostrar_lista_desc(nombre):
    global afusuario, alusuario, aflocales, allocales, alpromociones, afpromociones
    t = os.path.getsize(afpromociones)
    if t == 0:
        print(f'\n{Fore.RED+Style.BRIGHT}Aun no hay promociones vigentes{Style.RESET_ALL}')
        input(f'Porfavor ingrese una tecla para poder continuar: ')
    else:   
        pos = Buscar(nombre)
        alusuario.seek(pos, 0)
        regUsuario = Usuario()
        regUsuario = pickle.load(alusuario)
        cod = regUsuario.codUsuario
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        regLocal = Local()
        regPromo = Promocion()
        tam = os.path.getsize(aflocales)
        allocales.seek(0, 0)
        while allocales.tell()< tam:
            regLocal = pickle.load(allocales)
            if regLocal.codUsuario == cod:
                alpromociones.seek(0, 0)
                while alpromociones.tell()< t:
                    regPromo = pickle.load(alpromociones)
                    if regPromo.codLocal == regLocal.codLocal and regPromo.fechaDesdePromo <= fecha_actual and regPromo.fechaHastaPromo >= fecha_actual and regLocal.estado == 'A':
                        print('Los descuentos disponibles son:')
                        print("\nLocal: ", regLocal.nombreLocal)
                        print("Codigo promo: ", regPromo.codPromo)
                        print("Texto: ", regPromo.textoPromo)
                        print("Fecha desde: ", regPromo.fechaDesdePromo)
                        print("Fecha Hasta: ", regPromo.fechaHastaPromo)
                        print("-" * 20)
        


def crear_descuento(nombre): 
    global afusuario, alusuario, aflocales, allocales, alpromociones, afpromociones
    
    os.system("cls")
    seguro = confirmar('Crear Descuento')
    if seguro == 0:
        print(f'\n{Fore.BLUE+Style.BRIGHT}Entrando a [ Crear Descuento ] ...{Style.RESET_ALL}')
        time.sleep(2)
        os.system("cls")
        mostrar_lista_desc(nombre)
        local_cod = input("\nIngrese el código de local: ")
        str(local_cod)
        local_cod = local_cod.ljust(3)
    
        while buscar_Cod_local(local_cod) == -1:
            local_cod = input(f"\n{Fore.RED+Style.BRIGHT}Codigo de local incorrecto, porfavor ingrese un codigo de local valido:{Style.RESET_ALL} ")
            str(local_cod)
            local_cod = local_cod.ljust(3)
       
        aux = Promocion()
        nueva_promocion = Promocion()
        nueva_promocion.codLocal = local_cod
        nueva_promocion.textoPromo = input("Ingrese el texto de la promoción: ")
    
        flag = False
        while not flag:
        
            fecha_hoy = datetime.now().strftime("%d/%m/%Y")  
            datetime.strptime(fecha_hoy, "%d/%m/%Y")
            fecha_desde = input("Ingrese la fecha de inicio (DD/MM/YYYY): ")
            datetime.strptime(fecha_desde,  "%d/%m/%Y")
            fecha_hasta = input("Ingrese la fecha de fin (DD/MM/YYYY): ")
            datetime.strptime(fecha_hasta, "%d/%m/%Y")
        
            if fecha_desde <= fecha_hasta and fecha_desde >= fecha_hoy: 
                nueva_promocion.fechaDesdePromo = fecha_desde
                nueva_promocion.fechaHastaPromo = fecha_hasta
                flag = True
            else:
                print(f"\n{Fore.RED+Style.BRIGHT}Fecha no válida. La fecha de inicio debe ser mayor o igual a la fecha actual y menor o igual a la fecha de fin.{Style.RESET_ALL}")
       
        for i in range(7):
            dia_valido = input(f"¿La promoción es válida el día {i+1} (1 para Sí, 0 para No)? ")
            nueva_promocion.diasSemana[i] = int(dia_valido)
    
        nueva_promocion.estado = "pendiente".ljust(10)
    
        t = os.path.getsize(afpromociones)
        alpromociones.seek(0, 0)
        if t == 0:
            nueva_promocion.codPromo = 1
        else:
            aux = pickle.load(alpromociones)
            tamReg = alpromociones.tell()
            cantReg = t // tamReg
            nueva_promocion.codPromo = cantReg + 1
        nueva_promocion.codPromo = str(nueva_promocion.codPromo)
        nueva_promocion.codPromo = nueva_promocion.codPromo.ljust(3)
        alpromociones.seek(0,2)
        pickle.dump(nueva_promocion, alpromociones)
        alpromociones.flush()

        print(f"\n{Fore.GREEN+Style.BRIGHT}Promoción creada con éxito y está pendiente de aprobación.{Style.RESET_ALL}")
        
    elif (seguro == -1):
        
        print(Fore.GREEN+Style.BRIGHT+'\nVolviendo al menu anterior!\n')
        time.sleep(2)
        os.system("cls")
    
    

def reporte_descuento(tipo_usuario, nombre):
    global afpromociones, alpromociones, afusopromo, alusopromo, alusuario, afusuario, allocales, aflocales
    regPromo = Promocion()
    regUso = UsoPromocion()
    regUsu = Usuario()
    regLoc = Local()
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")  
    datetime.strptime(fecha_hoy, "%d/%m/%Y")
    
    seguro = confirmar('Reporte de uso Descuentos')
    if seguro == 0:
        print(f'\n{Fore.BLUE+Style.BRIGHT}Entrando a [ Reporte de uso Descuentos ] ...{Style.RESET_ALL}')
        time.sleep(2)
        os.system("cls")
        if tipo_usuario =="administrador" or tipo_usuario =="dueño":
        # Solicita rango de fechas    
            flag = False
            while not flag:
            
                fecha_desde = input("\nIngrese la fecha de inicio (DD/MM/YYYY): ")
                datetime.strptime(fecha_desde,  "%d/%m/%Y")
                fecha_hasta = input("Ingrese la fecha de fin (DD/MM/YYYY): ")
                datetime.strptime(fecha_hasta, "%d/%m/%Y")
        
                if fecha_desde <= fecha_hasta: 
                    flag = True
                else:
                    print(f"\n{Fore.RED+Style.BRIGHT}Fecha no válida. La fecha de inicio debe ser mayor o igual a la fecha actual y menor o igual a la fecha de fin.{Style.RESET_ALL}")
            
        alpromociones.seek(0, 0)
        t = os.path.getsize(afpromociones)
        if tipo_usuario == "administrador":
                print(f"{Fore.BLUE+Style.BRIGHT}---- Reporte de uso de descuentos ----{Style.RESET_ALL}")
                print()
                while alpromociones.tell() < t:
                    regPromo = pickle.load(alpromociones)
                    if regPromo.estado =="aprobada".ljust(10) and fecha_desde <= regPromo.fechaDesdePromo and fecha_hasta >= regPromo.fechaHastaPromo:
                        usos = buscar_Cod_promo(regPromo.codPromo, fecha_desde, fecha_hasta)
                        print(f"Código Promo: {regPromo.codPromo}")
                        print(f"Texto: {regPromo.textoPromo}")
                        print(f"Fecha Desde: {regPromo.fechaDesdePromo}")
                        print(f"Fecha Hasta: {regPromo.fechaHastaPromo}")
                        print(f"Cantidad de Usos: {usos}")
                        print("-" * 20)
        elif tipo_usuario =="dueño":
                print(f"\n{Fore.BLUE+Style.BRIGHT}---- Reporte de uso de descuentos ----{Style.RESET_ALL}")
                print()
                posi = Buscar(nombre)
                alusuario.seek(posi, 0)
                regUsu = pickle.load(alusuario)
                cod = regUsu.codUsuario
                tam = os.path.getsize(aflocales)
                allocales.seek(0, 0)
                while allocales.tell()< tam:
                    regLoc = pickle.load(allocales)
                    if regLoc.codUsuario == cod:
                        print("\nLocal: ", regLoc.nombreLocal)
                        alpromociones.seek(0, 0)
                        while alpromociones.tell()< t:
                            regPromo = pickle.load(alpromociones)
                            if regPromo.codLocal == regLoc.codLocal and regPromo.fechaDesdePromo >= fecha_desde and regPromo.fechaHastaPromo <= fecha_hasta and regPromo.estado == "aprobada".ljust(10):
                                print("Codigo promo: ", regPromo.codPromo)
                                print("Texto: ", regPromo.textoPromo)
                                print("Fecha desde: ", regPromo.fechaDesdePromo)
                                print("Fecha Hasta: ", regPromo.fechaHastaPromo)
                                print("Cantidad de usos: ", buscar_Cod_promo(regPromo.codPromo, fecha_desde, fecha_hasta))
                                print("-" * 20)
        elif tipo_usuario == "cliente":
                print(f"\n{Fore.GREEN+Style.BRIGHT}---- Buscar descuentos ----{Style.RESET_ALL}")
                print()
                cod = input("\nIngrese el codigo del local a buscar: ").ljust(3)
                while buscar_Cod_local(cod) == -1:
                    cod = input(f"\n{Fore.RED+Style.BRIGHT}Codigo del local inexistente, ingrese uno válido:{Style.RESET_ALL} ").ljust(3)
                pos = buscar_Cod_local(cod)
                allocales.seek(pos, 0)
                regLoc = pickle.load(allocales)
                print(f"Local seleccionado: {regLoc.nombreLocal}")
                ok = False
                while not ok:
                    try:
                        fecha_desde = input("Ingrese la fecha (DD/MM/YYYY): ")
                        fecha_desde = datetime.strptime(fecha_desde, "%d/%m/%Y").date()
                        if fecha_desde < date.today():
                            print(f"{Fore.RED+Style.BRIGHT}La fecha ingresada ya pasó{Style.RESET_ALL}")
                        else:
                            ok = True
                    except:
                        print(f"\n{Fore.RED+Style.BRIGHT}Fecha no válida. Recuerde utilizar el formato DD/MM/YYYY.{Style.RESET_ALL}")
                DIAS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

                fecha_actual = datetime.now().date()
                nombre_dia_semana = fecha_actual.strftime("%A").lower()
                t = os.path.getsize(afpromociones)
                alpromociones.seek(0, 0)
                print("--Promociones disponibles--")
                while alpromociones.tell() < t:
                    regPromo = pickle.load(alpromociones)
                    if regPromo.codLocal == cod and regPromo.fechaDesdePromo <= fecha_hoy and fecha_hoy <= regPromo.fechaHastaPromo and regPromo.estado == "aprobada".ljust(10) and regPromo.diasSemana[DIAS.index(nombre_dia_semana)] == 1:
                            print(f"Código Promo: {regPromo.codPromo}")
                            print(f"Texto: {regPromo.textoPromo}")
                            print(f"Fecha Desde: {regPromo.fechaDesdePromo}")
                            print(f"Fecha Hasta: {regPromo.fechaHastaPromo}")
                            print("-" * 20)
        input("\nDigite cualquier tecla para volver: ")
        
    elif (seguro == -1):
        
        print(Fore.GREEN+Style.BRIGHT+'\nVolviendo al menu anterior!\n')
        time.sleep(2)
        os.system("cls")
    

def guardar_usuarios():
    alusuario.close()
    
def guardar_locales():
    allocales.close()

def guardar_promociones():
    alpromociones.close()

def guardar_novedades():
    alnovedades.close()

def guardar_usos_promocion():
    alusopromo.close()


def solicitar_descuento(nombre):
    global afpromociones, alpromociones, afusopromo, alusopromo, afusuario, alusuario
    regPromo = Promocion()
    regUso = UsoPromocion()
    regUsu = Usuario()
    os.system("cls")
    seguro = confirmar('Solicitar Descuento')
    if (seguro == 0):
        print(f'\n{Fore.BLUE+Style.BRIGHT}Entrando a [ Solicitar Descuento ] ...{Style.RESET_ALL}')
        time.sleep(2)
        os.system("cls")
        print("---- Solicitar descuento ----")
        cod = str(input("\nIngrese el codigo de promoción que quiere utilizar: "))
        cod = cod.ljust(3)
        posi = buscar_promo_por_cod(cod)
        while posi == -1:
            cod = str(input(f"\n{Fore.RED+Style.BRIGHT}Codigo de promoción inexistente, intente de nuevo:{Style.RESET_ALL} "))
            cod = cod.ljust(3)
            posi = buscar_promo_por_cod(cod)
        fecha_actual = datetime.now().date()
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")  
        datetime.strptime(fecha_hoy, "%d/%m/%Y")
        nombre_dia_semana = fecha_actual.strftime("%A").lower()
        t = os.path.getsize(afpromociones)
        alpromociones.seek(posi, 0)
        regPromo = pickle.load(alpromociones)
        DIAS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        if regPromo.estado == "aprobada".ljust(10) and regPromo.fechaDesdePromo <= fecha_hoy and regPromo.fechaHastaPromo >= fecha_hoy and regPromo.diasSemana[DIAS.index(nombre_dia_semana)] == 1:
            pos = Buscar(nombre)
            alusuario.seek(pos, 0)
            regUsu = pickle.load(alusuario)
            cod = regUsu.codUsuario
            regUso.codCliente = cod
            regUso.codPromo = cod
            regUso.fechaUsoPromo = fecha_actual
            alusopromo.seek(0, 2)
            pickle.dump(regUso, alusopromo)
            alusopromo.flush()
            print(f"\n{Fore.GREEN+Style.BRIGHT}-- Uso registrado correctamente --{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED+Style.BRIGHT}La promoción que quiere utilizar no está disponible el dia de hoy{Style.RESET_ALL}")
        input("Digite cualquier tecla para volver: ")
    elif (seguro == -1):
        print(Fore.GREEN+Style.BRIGHT+'\nVolviendo al menu anterior!\n')
        time.sleep(2)
        os.system("cls")


def ingresar(): # Opcion 1
    global afusuario, alusuario
    os.system("cls")
    print(f"{Fore.YELLOW+Style.BRIGHT}-----------{Style.RESET_ALL} Inicio de Sesión {Fore.YELLOW+Style.BRIGHT}-----------")
    nombre = input("\nIngrese su nombre de usuario: ").ljust(100)
    clave = ocultar("Ingrese su contraseña: ").ljust(8)
    usuarios_encontrados = BuscarCon(nombre, clave)
    if usuarios_encontrados:
        print(f"{Fore.GREEN+Style.BRIGHT}\nBienvenido!")
        time.sleep(2)
        mostrar_menu(usuarios_encontrados, nombre)
    else:
        print(f"\n{Fore.RED+Style.BRIGHT}Se ha superado el numero maximo de intentos.")
        print(f'{Fore.RED+Style.BRIGHT}Volviendo ... ')
        time.sleep(2)
        

def registrar_cliente(): # Opcion 2
    os.system("cls")
    global cods, afusuario, alusuario  
    print(f"{Fore.CYAN+Style.BRIGHT}-----------{Style.RESET_ALL} Registrarse {Fore.CYAN+Style.BRIGHT}----------")
    correo = input("\nIngrese su correo electronico: ").ljust(100)
    regUsuario = Usuario()
    while Buscar(correo) != -1:
        correo = input(f"{Fore.RED+Style.BRIGHT}Ya existe un usuario con ese correo, vuelva a intentarlo {Style.RESET_ALL}: ")

    regUsuario.codUsuario = cargaCod()
    regUsuario.nombreUsuario = correo
    clave = ocultar("Ingrese su contraseña (8 caracteres): ")
    while len(clave) != 8:
        clave = ocultar(f"{Fore.RED+Style.BRIGHT}La clave debe tener 8 caracteres, intente de nuevo {Style.RESET_ALL}: ")
    regUsuario.claveUsuario = clave
    regUsuario.tipoUsuario = "cliente".ljust(20)
    alusuario.seek(0, 2)
    pickle.dump(regUsuario, alusuario)
    alusuario.flush()
    print ("\n------------------------------------")
    print(f"|{Fore.GREEN+Style.BRIGHT} Usuario registrado correctamente {Style.RESET_ALL}|")
    print ("------------------------------------")
    time.sleep(3)
       
        
def mostrar_menu(tipo_usuario,nombre):
    if tipo_usuario == "administrador".ljust(20):
        ingresar_como_administrador()
    elif tipo_usuario == "cliente".ljust(20):
        ingresar_como_cliente(nombre)
    elif tipo_usuario == "Dueño de local".ljust(20): 
        ingresar_como_dueño(nombre)


def ingresar_como_cliente(nombre):
    os.system("cls")
    opcion=-1
    
    while opcion!=0:
        print(f"{Fore.GREEN+Style.BRIGHT}-----------{Style.RESET_ALL} Menu Clientes {Fore.GREEN+Style.BRIGHT}-----------")
        print(f"\n{Fore.BLUE+Style.BRIGHT}1{Style.RESET_ALL}. Buscar descuentos en local")
        print(f"{Fore.GREEN+Style.BRIGHT}2{Style.RESET_ALL}. Solicitar descuento")
        print(f"{Fore.YELLOW+Style.BRIGHT}3{Style.RESET_ALL}. Ver novedades")
        print(f"{Fore.RED+Style.BRIGHT}0{Style.RESET_ALL}. Salir" + Style.RESET_ALL)
        print(f'\n{Fore.GREEN+Style.BRIGHT}-------------------------------------')

        opcion = int(input(f"\nIngrese una opción: "))
        while(validarEnteros(opcion, 0, 3)):
            opcion = input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Entre 0 y 3:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
        

        if opcion == 1:
            reporte_descuento("cliente", "xd") 
        elif opcion == 2:
            solicitar_descuento(nombre)           
        elif opcion == 3:
            construccion()# En chapin
        else:
            print(Fore.RED+Style.BRIGHT + "\nVolviendo al Menu Principal" + Style.RESET_ALL)
            time.sleep(2)
            
            
def ingresar_como_administrador(): #menuadmin
    opcion=-1
    while opcion!=0:
        os.system("cls")
        print(f"{Fore.YELLOW+Style.BRIGHT}-----------{Style.RESET_ALL} Menu Administrador {Fore.YELLOW+Style.BRIGHT}--------------")
        print(f"\n{Fore.CYAN+Style.BRIGHT}1{Style.RESET_ALL}. Gestión de Locales")
        print(f"{Fore.MAGENTA+Style.BRIGHT}2{Style.RESET_ALL}. Crear cuentas de dueños de locales")
        print(f"{Fore.GREEN+Style.BRIGHT}3{Style.RESET_ALL}. {Fore.GREEN+Style.BRIGHT}Aprobar{Style.RESET_ALL} / {Fore.RED+Style.BRIGHT}Denegar{Style.RESET_ALL} solicitud de descuento")
        print(f"{Fore.YELLOW+Style.BRIGHT}4{Style.RESET_ALL}. Gestión de Novedades")
        print(f"{Fore.BLUE+Style.BRIGHT}5{Style.RESET_ALL}. Reporte de utilización de descuentos")
        print(f"{Fore.RED+Style.BRIGHT}0{Style.RESET_ALL}. Salir")
        print(Fore.YELLOW+Style.BRIGHT + '\n---------------------------------------------')

        opcion = int(input("\nIngrese una opción: "))
        while(validarEnteros(opcion, 0, 5)):
            opcion = input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Entre 0 y 5:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
        

        if opcion == 1:
            gestionar_locales() 
        elif opcion == 2:         
            crear_dueños()            
        elif opcion == 3:
            aprobar_descuento() 
        elif opcion== 4:
            construccion() 
        elif opcion==5:
            reporte_descuento('administrador', 'xd')   
        else:
            print(Fore.RED+Style.BRIGHT + "\nVolviendo al Menu Principal" + Style.RESET_ALL)
            time.sleep(2)
    

def ingresar_como_dueño(nombre): #dueño
    os.system("cls")
    opcion=-1
    while opcion!=0:
        print(f"{Fore.BLUE+Style.BRIGHT}-----------{Style.RESET_ALL} Menu Dueños {Fore.BLUE+Style.BRIGHT}--------------")
        print(f"\n{Fore.GREEN+Style.BRIGHT}1{Style.RESET_ALL}. Crear descuento")
        print(f"{Fore.GREEN+Style.BRIGHT}2{Style.RESET_ALL}. Reporte de uso de descuentos")
        print(f"{Fore.YELLOW+Style.BRIGHT}3{Style.RESET_ALL}. Ver novedades")
        print(f"{Fore.RED+Style.BRIGHT}0{Style.RESET_ALL}. Salir")
        print(Fore.BLUE+Style.BRIGHT + '\n---------------------------------------')

        opcion = int(input("\nIngrese una opción: "))
        while(validarEnteros(opcion, 0, 3)):
            opcion = input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Entre 0 y 3:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
        

        if opcion == 1:
            crear_descuento(nombre) 
        elif opcion == 2:
            reporte_descuento("dueño", nombre)          
        elif opcion == 3:
            construccion() # En chapin
        else:
            print(Fore.RED+Style.BRIGHT + "\nVolviendo al Menu Principal" + Style.RESET_ALL)
            time.sleep(2)
    
def pantalla1():
    print(f'''{Fore.GREEN+Style.BRIGHT}\n Good Ending, no se crasheo el Mapa de Locales{Style.RESET_ALL}\n
    ⢀⣻⡿⣝⢿⣟⣯⡷⡈⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣿⣎⢮⡟⡌⢻⡱⡀⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⣿⡿⢟⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣬⣿⣿⣶⣕⡘⣆⢷⡵⡐⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⢿⣄⠀⢈⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⡹⣿⣿⣿⣿⣬⡳⢿⢷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣧⠙⢿⣟⡿⣧⠋⢴⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⠀⠀⠀⠀
⡀⠀⠀⠀⠀⠀⠹⣿⣿⣯⣽⣻⣷⢯⡟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠈⢿⣿⣇⢠⣿⡶⡼⡀⠹⣮⣽⣿⣿⣿⣿⣿⡟⣰⡾⡄⠀⠀⠀⠀
⠱⡀⠀⠀⠀⠀⠀⢈⣿⣿⡇⣿⣿⢸⢿⡏⣿⡧⣿⣿⣿⣿⡇⣿⣿⣷⡾⡟⣿⠉⣠⣷⣼⣥⣤⡗⠋⠙⠿⣿⣿⡿⢰⣧⢳⡸⡄⠀⠀⠀
⠀⡱⡄⠀⠀⠀⠀⠀⠹⣿⣿⡟⣿⣼⣾⠳⣻⣷⠻⣿⡟⣿⣧⠃⣹⣷⣤⣼⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⢿⣿⢁⣯⣌⢀⡇⡇⠀⠀⠀
⠀⠈⠙⣆⠀⠀⠀⠀⠀⠙⢿⣾⣧⣿⣿⣦⣬⣿⣄⡹⣷⠹⣿⣼⣿⣿⣿⣿⠿⠟⠋⢀⡠⣥⡀⠀⠀⠀⠀⢸⣿⠘⣿⢟⡸⡱⠀⠀⠀⠀
⠀⠠⡾⠋⢆⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⣿⣿⣿⢿⣿⡟⠣⡀⣹⢟⣿⢽⣯⣭⣭⣽⣶⣿⡿⣿⠇⠀⠀⢠⣾⢷⠸⣯⢈⣾⣷⡀⠀⠀⠀
⠀⢊⠄⣠⡊⣦⠀⠀⠀⠀⠀⠈⣧⢙⣦⠤⢤⣲⣬⣿⡷⡀⠀⡇⠈⠛⠋⠑⠊⠉⠉⠈⠁⠈⢕⢅⡀⠀⠟⠃⣺⡞⠁⣸⢿⣿⣯⠀⠀⠀
⢂⢍⣜⡟⢩⣬⣧⡀⠀⠀⠀⠀⠘⣖⢽⠿⠛⠛⠘⠡⡇⣇⣀⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠋⠀⠀⠀⠀⣺⣷⣶⡟⢸⣿⣯⡑⠀⠀
⢻⣾⣿⣫⣖⠛⠁⢳⡀⠀⠀⠀⠀⢻⢷⠇⠀⠀⠀⠨⡀⡇⠀⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠈⡇⢨⢿⡏⠛⠀⠀
⠀⢻⣿⣿⢆⠀⣀⡴⢳⡄⠀⠀⠀⠈⢏⢉⠁⠀⠀⠀⢱⡇⠀⢀⡄⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⢺⡇⢀⠇⠂⠙⣿⡀⠀⠀
⠀⠀⢻⣿⣧⣾⠟⠀⠀⢹⣆⠀⠀⠀⠈⢧⡀⣀⠀⠀⠘⠧⣀⣨⣴⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠇⣰⠀⠀⠀⢻⣧⠀⠀
⠀⠀⠀⠳⣿⣿⣆⣴⣾⠏⠙⢦⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠙⢁⣀⣀⣀⣀⡀⣀⡤⠟⠀⠀⠀⠀⢀⣼⣿⡟⢀⡿⠀⠀⡠⠋⢾⡆⠀
⠀⠀⠀⠀⠹⡏⣿⡿⡏⠀⣠⢈⣷⡀⠀⠀⠸⣷⡀⠀⠓⠚⠛⠛⠓⠛⠊⠉⠉⣉⠀⠀⠀⠀⠀⠀⣴⣿⣿⡟⠀⢰⠃⠀⠀⠀⠀⠹⣷⣿
⠀⠀⠀⠀⠀⣷⣿⣿⣾⣟⣿⣞⣀⠹⣄⠀⠀⢳⠻⣄⠀⠀⢲⣶⣲⠶⠾⠿⠿⠓⠀⠀⠀⠀⣠⣾⣿⣿⡿⠀⠀⣰⠁⠀⢠⢳⣤⣤⣯⠏
⠀⠀⢀⣀⢴⣻⣿⢿⣿⣿⣷⣱⣿⢀⣼⣶⣶⣾⣷⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⡿⠁⠀⣰⡏⠀⣰⢏⡀⢻⣿⣷⣷
⢰⣌⠉⣬⣾⣿⡟⣿⣿⣿⡇⣿⣷⣿⣿⣿⣿⣿⣿⣧⠹⣷⣄⠰⡄⠀⠀⠀⣀⣀⣠⣶⣿⢿⣿⣿⠏⠀⢀⣀⣟⣡⢾⣵⣿⣷⣶⢻⣿⣿
⣠⣼⣷⣜⣿⣿⣧⣾⣿⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣋⣀⣠⣞⣈⣿⣿⣿⣿⣿⣿⣷⣶⣽⣿ 
''')
    
# Función principal del programa
def main():
    
    cargar_usuarios()
    cargar_locales()
    cargar_promociones()
    cargar_novedades()
    cargar_usos_promocion()
    
    
    opc = -1
    while opc != 3:
        os.system("cls")
        # Mostrar menú principal y obtener la opción del usuario
        print(f"{Fore.CYAN+Style.BRIGHT}-----------{Style.RESET_ALL} Menu Principal {Fore.CYAN+Style.BRIGHT}-----------")
        print(f"\n{Fore.YELLOW+Style.BRIGHT}1{Style.RESET_ALL}. Ingresar con usuario registrado")
        print(f"{Fore.GREEN+Style.BRIGHT}2{Style.RESET_ALL}. Registrarse como cliente")
        print(f"{Fore.RED+Style.BRIGHT}3{Style.RESET_ALL}. Salir")
        print(Fore.CYAN+Style.BRIGHT + '\n-------------------------------------')
        opc = int(input("\nIngrese la opción: "))
        while validarEnteros(opc, 1, 3):
            opc = int(input("Opción no válida, intente nuevamente: "))
        if opc == 1:
            ingresar()                      
        elif opc == 2:
             registrar_cliente()
        elif opc == 3:
            print('\n¿Está seguro de que desea salir del programa?')
            print(Fore.RED+Style.BRIGHT+f'Recuerde que esta acción NO se puede deshacer\n')
            print(f'{Fore.RED+Style.BRIGHT}S {Style.RESET_ALL}- Salir')
            print(f'{Fore.GREEN+Style.BRIGHT}C {Style.RESET_ALL}- Cancelar')
            Confirmacion=str(input(Style.RESET_ALL+'\nIngrese una opción: ').upper())
            while(Confirmacion!='S' and Confirmacion!='C'):
                print('')
                Confirmacion=str(input(Fore.RED+Style.BRIGHT+f'Opción incorrecta, intentalo nuevamente{Style.RESET_ALL}: ').upper())  
            if (Confirmacion =='S'):
                print(Fore.GREEN+Style.BRIGHT+'\nGracias por usar este programa!')
                opc = 3
            elif (Confirmacion=="C"):
                opc=-1
                
                
    guardar_usuarios()
    guardar_locales()
    guardar_promociones()
    guardar_novedades()
    guardar_usos_promocion()


if __name__ == "__main__":
    main()
