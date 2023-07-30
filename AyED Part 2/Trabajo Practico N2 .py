from colorama import Fore, Back, Style, init
from tqdm import tqdm, trange
import os, os.path, getpass, time

# Algoritmos y Estructuras de Datos 2023:
# Comision 110 - T.T
# Maximiliano Jesús Gomez

# Tipo de dato estructurado
# vec = arreglo[0..49,0..3] de string
# num = arreglo[0..49,0..1] de integer
# us = arreglo[0..3, 0..2] de string
# rub = arreglo[0..2] de string
# rubint = arreglo[0..2] de integer

# Variables
# LOCALESTTR_ : vec
# LOCALESINT : num
# RUBROSSTR : rub
# RUBROSINT: rubint

# comidaC, perfumeriaC, indumentariaC, cod_dueño_local, cod_local, inf, sup , med , n , localescreados, cod_dueño_local2 , fila: integer
# nombre_local, ubi_local, rubro_local, nombre_local2,ubicacion_local2 : string
# ban, bandera : boolean



# Constantes para los tipos de usuario
ADMINISTRADOR = 'administrador'
DUEÑO_LOCALA = 'dueñoLocalA'
DUEÑO_LOCALB = "dueñoLocalB"
CLIENTE = 'cliente'

def inicializar():
    global localescreados, comidaC, indumentariaC, perfumeriaC, nombre_local, ubicacion_local, rubro_local, cod_dueño_local, cod_local
    comidaC, indumentariaC, perfumeriaC, cod_local, cod_dueño_local = 0, 0, 0, 0, 0
    nombre_local, ubicacion_local, rubro_local = "", "", ""
    localescreados = 0

# Listas para almacenar datos de usuarios y locales
USUARIOSSTR = [
    ['admin@shopping.com', '12345', ADMINISTRADOR],
    ['localA@shopping.com', 'AAAA1111', DUEÑO_LOCALA],
    ['localB@shopping.com', 'BBBB2222', DUEÑO_LOCALB],
    ['unCliente@shopping.com', '33xx33', CLIENTE,]
]
USUARIOSCOD = [1, 4, 6, 9]


LOCALESSTR_=[[""]*4 for i in range (50)]
LOCALESINT=[[0]*2 for j in range (50)]

# Barra
def cargando():
    pbar = tqdm(total=100)
    print = (Style.RESET_ALL +''+ Back.GREEN)
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)
    pbar.close()
    
# Funciones para buscar usuarios y locales

def buscar_local_por_nombre(listaloc, nombre, tam):
    global bandera
    inf = 0
    sup = tam 
    med = (inf + sup) // 2

    for i in range(tam):
        for j in range(i + 1, tam):
            if listaloc[i][0] > listaloc[j][0]:
                for k in range(4):
                    aux = listaloc[i][k]
                    listaloc[i][k] = listaloc[j][k]
                    listaloc[j][k] = aux

    bandera = False
    while (listaloc[med][0] != nombre) and (inf <= sup):
        if (nombre > listaloc[med][0]):
            inf = med + 1
        else:
            sup = med - 1
        med = (inf + sup) // 2
    if (listaloc[med][0] == nombre):
        bandera = True
    return bandera

def buscar_local_por_codigo(codigo):
    for i in range (localescreados):
        if LOCALESINT[i][0] == codigo:
            fila = i
            return LOCALESSTR_[i], LOCALESINT[i], fila
        

def mostrar_cantidad_locales_por_rubro(listalocales, tamaño):
    global comidaC, indumentariaC, perfumeriaC
    rubros=[]
    cantidad=[]
    for i in range (tamaño):
        if listalocales[i][2] == "comida":
            comidaC = comidaC + 1
        elif listalocales[i][2] == "indumentaria":
            indumentariaC = indumentariaC + 1
        elif listalocales[i][2] == "perfumeria":
            perfumeriaC = perfumeriaC + 1

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
    return RUBROSINT, RUBROSSTR

def mostrar_locales():
    print("-- Locales creados --")
    for i in range (localescreados):
            print(Fore.BLUE+Style.BRIGHT+f"\nNombre: {Style.RESET_ALL}",LOCALESSTR_[i][0],"   ",
                   Fore.BLUE+Style.BRIGHT+f"Ubicacion: {Style.RESET_ALL} ", LOCALESSTR_[i][1],"   ",
                     Fore.BLUE+Style.BRIGHT+f"Rubro: {Style.RESET_ALL}", LOCALESSTR_[i][2],"   ",                    
                      Fore.BLUE+Style.BRIGHT+f"Codigo: {Style.RESET_ALL}", LOCALESINT[i][0],"   ",
                       Fore.GREEN+Style.BRIGHT+f"Activo(A) {Style.RESET_ALL}", "/// ", Fore.RED+Style.BRIGHT+f"Dado de baja(B): {Style.RESET_ALL}", LOCALESSTR_[i][3] )
            
def validarEnteros(nro, min, max):
    try:
        nro = int(nro)
        if nro >= min and nro <= max:
            return False
        else:
            return True
    except:
        return True
    
def construccionadm():
    opci = ''
    print(Fore.RED+Style.BRIGHT+'\nEsta funcionalidad se encuentra en construccion!')
    opci = str(input(Style.RESET_ALL +'Por favor ingrese * para volver al menu anterior: '))
    while opci != '*':
        print(Fore.RED+Style.BRIGHT+'Opcion incorrecta.')
        opci = str(input(Style.RESET_ALL +'Por favor ingrese * para volver al menu anterior: '))

def verificar_clave(usuario, clave):
    intentos = 3
    while intentos > 0:
        for i in range(len(USUARIOSSTR)):
            if usuario == USUARIOSSTR[i][0] and clave == USUARIOSSTR[i][1]:
                return USUARIOSSTR[i][2]
        print(Fore.RED+Style.BRIGHT +"\nNombre de usuario o contraseña incorrectos."+ Style.RESET_ALL)
        intentos -= 1
        if intentos > 0:
            print(f"Quedan {Fore.RED+Style.BRIGHT}{intentos}{Style.RESET_ALL} intentos. Intente nuevamente.")
            usuario = input("\nIngrese su nombre de usuario: ")
            clave = input("Ingrese su contraseña: ")
    return None

def mostrar_menu(tipo_usuario, usuario):
    if tipo_usuario == 'administrador':
        menu_administrador()       
    elif tipo_usuario == 'dueñoLocalA':
        menu_dueño_local(usuario)     
    elif tipo_usuario == 'cliente':
        menu_cliente()     
    else:
        print("Tipo de usuario desconocido.")



# Funciones para el inicio de sesión y menús
def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    clave_usuario = input("Ingrese su contraseña: ")

    usuarios_encontrados = verificar_clave(nombre_usuario, clave_usuario)

    if usuarios_encontrados:
        cargando()
        print('\n')
        print(Fore.GREEN + "Bienvenido!\n"+Style.RESET_ALL)
        mostrar_menu(usuarios_encontrados, nombre_usuario)
    else:
        print("Se ha superado el numero maximo de intentos. Saliendo del programa")


# Menús para cada tipo de usuario
def menu_administrador():
    opcion=-1
    while opcion!=0:
        print(Fore.CYAN + "\n--- Menú Administrador ---")
        print("1. Gestión de Locales")
        print("2. Crear cuentas de dueños de locales")
        print("3. Aprobar / Denegar solicitud de descuento")
        print("4. Gestión de Novedades")
        print("5. Reporte de utilización de descuentos")
        print("0. Salir" + Style.RESET_ALL)

        opcion = input("Ingrese una opción: ")
        while(validarEnteros(opcion, 0, 5)):
            opcion = input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Entre 0 y 5:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
        

        if opcion == 1:
            gestionar_locales()
        elif opcion == 2:
            construccionadm()            
        elif opcion == 3:
            construccionadm()
        elif opcion== 4:
            gestionar_novedades()
        elif opcion==5:
            construccionadm()
        else:
            print(Fore.RED + "Saliendo" + Style.RESET_ALL)
            opcion = 0
            

def gestionar_locales():
    Opci = '' 
    while (Opci.upper() != 'D'):
        os.system('cls')
        print("--Gestión de locales--")
        print(Fore.CYAN + "\na. Crear locales")
        print("b. Modificar local")
        print("c. Eliminar local")
        print("d. Mapa de locales")
        print("e. Volver" + Style.RESET_ALL)  
        Opci = str(input(Fore.CYAN+Style.BRIGHT+'\nIngrese la opción que desea operar: '+Style.RESET_ALL).upper())
        while (Opci<'A' or Opci>'D') and (Opci!='E'):
            Opci = str(input(Fore.RED+Style.BRIGHT+f'Opción incorrecta {Style.RESET_ALL}- Entre A y E [E para Volver]: '+Style.RESET_ALL).upper())
        if Opci == "A":
            crear_locales()
        elif Opci == "B":
            modificar_local()
        elif Opci == "C":
            eliminar_local()
        elif Opci == "D":
            mostrar_mapa_locales()
        elif Opci =="E":
            menu_administrador()

    
def gestionar_novedades():
    Opci = '' 
    while (Opci.upper() != 'E'):
        os.system('cls')
        print(Fore.YELLOW+"--Gestion de Novedades--"+Style.RESET_ALL)
        print("a) Crear novedades")
        print("b) Modificar novedad")
        print("c) Eliminar novedad")
        print("d) Ver reporte de novedades")
        print("e) Volver")
        Opci = str(input(Fore.YELLOW+Style.BRIGHT+f'\nIngrese la opción que desea operar: {Style.RESET_ALL} ').upper())
        while (Opci<'A' or Opci>'D') and (Opci!='E'):
            Opci = str(input(Fore.RED+Style.BRIGHT+f'Opción incorrecta {Style.RESET_ALL}- Entre A y D [E para Volver]: a').upper())
        if(Opci == 'A') or (Opci == 'B') or (Opci == 'C') or (Opci == 'D'):
            construccionadm()
   
    
def crear_locales():
    global localescreados
    global comidaC, indumentariaC, perfumeriaC
    if localescreados!=0:

        opc=input("¿Desea ver los locales cargados hasta el momento?(SI/NO): ").upper()
        while (opc!= "SI" and opc !="NO"):
         print(f'{Fore.RED+Style.BRIGHT}Opcion Incorrecta.{Style.RESET_ALL}')
         opc = input(f'Ingrese [{Fore.GREEN+Style.BRIGHT}SI / {Fore.RED+Style.BRIGHT}NO{Style.RESET_ALL}] : ').upper()
         
         mostrar_locales()


    crear = input(f'\nDesea crear un local? [{Fore.GREEN+Style.BRIGHT}SI {Style.RESET_ALL}/ {Fore.RED+Style.BRIGHT}NO{Style.RESET_ALL}] : ').upper()
    
    while(crear != 'SI' and crear != 'NO'):
        print(f'{Fore.RED+Style.BRIGHT}Opcion Incorrecta.{Style.RESET_ALL}')
        crear = input(f'Ingrese [{Fore.GREEN+Style.BRIGHT}SI / {Fore.RED+Style.BRIGHT}NO{Style.RESET_ALL}] : ').upper()
    while(crear != 'NO' and crear == 'SI'):
     print(Fore.CYAN + "Creando nuevo local:" + Style.RESET_ALL)

     nombre_local = input("Ingrese el nombre del local: ")

     #Validacion del nombre
     if localescreados != 0:
          ban=True
          while ban==True:
             ban = buscar_local_por_nombre(LOCALESSTR_, nombre_local, localescreados)
             if ban==True:
                nombre_local=input(Fore.RED + "Nombre de ya existente, ingrese otro nombre: " + Style.RESET_ALL)
             
              
            

     ubicacion_local = input("Ingrese la ubicación del local: ")

     print("Rubros disponibles: 'indumentaria', 'perfumería', 'comida'")
     rubro_local = input("Ingrese el rubro del local: ")
     # Validacion del rubro
     rubros_disponibles = ['indumentaria', 'perfumería', 'comida']
     while rubro_local not in rubros_disponibles:
        print(Fore.RED + "Rubro inválido. Intente nuevamente." + Style.RESET_ALL)
        rubro_local = input("Ingrese un rubro válido: ")
     if rubro_local == "comida":
         comidaC = comidaC + 1
     elif rubro_local == "indumentaria":
         indumentariaC = indumentariaC +1
     elif rubro_local == "perfumería":
         perfumeriaC = perfumeriaC + 1
    

     cod_dueño_local = int(input("Ingrese el código del dueño del local: "))
     while cod_dueño_local != 4 and cod_dueño_local != 6:
         cod_dueño_local=input(Fore.RED+Style.BRIGHT + "Codigo invalido, vuelva a intentar: " + Style.RESET_ALL)

     # Validar que el código del dueño del local corresponda a un dueño existente

     localescreados=localescreados+1

     # Asignar automáticamente el código del nuevo local
     cod_local = localescreados

     # Crear y agregar el nuevo local a la lista LOCALES
     nuevo_localstr = [nombre_local, ubicacion_local, rubro_local, "A"]
     nuevo_localint = [cod_local, cod_dueño_local]
     LOCALESSTR_[localescreados-1] = nuevo_localstr
     LOCALESINT[localescreados-1] = nuevo_localint

     print(Fore.GREEN + "Local creado exitosamente." + Style.RESET_ALL)

     #Ordenamiento de los arrays
     for i in range(localescreados-1):
        for j in range(i + 1, localescreados):
            if LOCALESSTR_[i][0] > LOCALESSTR_[j][0]:
                for h in range (2):
                    aux2 = LOCALESINT[i][h]
                    LOCALESINT[i][h] = LOCALESINT[j][h]
                    LOCALESINT[j][h] = aux2
                for k in range(4):
                    aux = LOCALESSTR_[i][k]
                    LOCALESSTR_[i][k] = LOCALESSTR_[j][k]
                    LOCALESSTR_[j][k] = aux

      #ORDENAMIENTO DE RUBROS   

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
    
     print("-- Rubros --")
     print()
     print(RUBROSSTR[0], "tiene", RUBROSINT[0], "locales")
     print()
     print(RUBROSSTR[1], "tiene", RUBROSINT[1], "locales")
     print()
     print(RUBROSSTR[2], "tiene", RUBROSINT[2], "locales")
     print()

     crear = input("¿Desea crear otro local? (SI/NO)").upper()
     while (crear != 'NO' and crear != 'SI'):
            print(Fore.RED+Style.BRIGHT+'Opcion Incorrecta'+Style.RESET_ALL)
            crear = input(f'Desea crear otro local? [{Fore.GREEN+Style.BRIGHT}SI{Style.RESET_ALL}/{Fore.RED+Style.BRIGHT}NO{Style.RESET_ALL}]: ').upper()
        


def modificar_local():
    global nombre_local, cod_local
    print(Fore.GREEN + "Modificando local existente:" + Style.RESET_ALL)
    cod_local = int(input("Ingrese el código del local a modificar: "))

    # Buscar el local por su código
    locales_encontrados, codigos_encontrados, fila = buscar_local_por_codigo(cod_local)

    if not locales_encontrados:
        print(Fore.RED + "No se encontró un local con ese código." + Style.RESET_ALL)
        return
    
    if locales_encontrados[3] == "B":
        opc = input(Fore.RED+Style.BRIGHT+"Este local está dado de baja ¿Deseas activarlo?(SI/NO)"+Style.RESET_ALL).upper()
        while opc != "SI" or opc != "NO":
            opc = input("Opción incorrecta, escriba SI o NO")
        if opc == "SI":
            locales_encontrados[3] = "A"
            print(Fore.GREEN + "Local activado exitosamente. Volviendo al menú anterior" + Style.RESET_ALL)
            time.sleep(3)
            gestionar_locales()
        else:
            print(Fore.CYAN + "Volviendo al menú anterior" + Style.RESET_ALL)
            time.sleep(3)
            gestionar_locales()

    print("Datos actuales del local:")
    print(f"Código de usuario: {codigos_encontrados[1]}")
    print(f"Nombre: {locales_encontrados[0]}")
    print(f"Ubicación: {locales_encontrados[1]}")
    print(f"Rubro: {locales_encontrados[2]}")

    nombre_local2, ubicacion_local2, rubro_local2 = "", "", ""

    nombre_local2 = input("Ingrese el nuevo nombre del local (Enter para mantener el actual): ")
    #Validacion del nombre
    if localescreados != 0:
          ban=True
          while ban==True:
             ban = buscar_local_por_nombre(LOCALESSTR_, nombre_local, localescreados)
             if ban==True:
                nombre_local=input(Fore.RED+"Nombre de ya existente, ingrese otro nombre: "+Style.RESET_ALL)
             else:
                 print("else")

    if nombre_local2 == "":
        nombre_local2 = nombre_local


    ubicacion_local2 = input("Ingrese la nueva ubicación del local (Enter para mantener la actual): ")
    if ubicacion_local2 == "":
        ubicacion_local2 = ubicacion_local


    rubro_local2 = input("Ingrese el nuevo rubro del local (Enter para mantener el actual): ")

    # Validar que el rubro sea válido
    if rubro_local2 and rubro_local2 not in ['indumentaria', 'perfumería', 'comida']:
        print(Fore.RED + "Rubro inválido. Intente nuevamente." + Style.RESET_ALL)
        return
    if rubro_local2 == "":
        rubro_local2 = rubro_local
    
    cod_dueño_local = int(input("Ingrese el código del dueño del local: "))
    while cod_dueño_local != 4 and cod_dueño_local != 6:
     cod_dueño_local=input(Fore.RED+"Codigo invalido, vuelva a intentar: "+Style.RESET_ALL)

    # Actualizar los datos del local
    LOCALESSTR_[fila][0] = nombre_local2
    LOCALESSTR_[fila][1] = ubicacion_local2
    LOCALESSTR_[fila][2] = rubro_local2
    LOCALESINT[fila][1] = cod_dueño_local
    LOCALESINT[fila][0] = cod_local

    print(Fore.GREEN + "Local modificado exitosamente. Volviendo al menú anterior" + Style.RESET_ALL)
    time.sleep(3)

def eliminar_local():
    print(Fore.RED + "Eliminando local:" + Style.RESET_ALL)
    cod_local = int(input("Ingrese el código del local a eliminar: "))

    # Buscar el local por su código
    locales_encontrados, codigos_encontrados, fila = buscar_local_por_codigo(cod_local)

    if not locales_encontrados:
        print(Fore.RED + "No se encontró un local con ese código." + Style.RESET_ALL)
        return

    # Preguntar confirmación antes de eliminar el local
    confirmacion = input(f"¿Está seguro que desea eliminar el local '{locales_encontrados[fila][0]}'? (S/N): ").upper()
    while confirmacion != "S" or confirmacion != "N":
        confirmacion = input(Fore.RED +"Opción incorrecta, seleccione una opción válida(S/N): "+ Style.RESET_ALL)

    if confirmacion.upper() == 'S':
        # Eliminar el local de forma lógica
        LOCALESSTR_[fila][3] = 'B'
        print(Fore.GREEN + "Local eliminado exitosamente." + Style.RESET_ALL)
        time.sleep(3)
    else:
        print(Fore.YELLOW + "Operación de eliminación cancelada." + Style.RESET_ALL)
        time.sleep(3)

# Función para mostrar el mapa de locales
def mostrar_mapa_locales():
    print("\n--- Mapa de Locales ---")

   # Filtra los locales activos del array LOCALESSTR_
    n=localescreados
    for i in range(n):
        for j in range(i + 1, n):
            if LOCALESSTR_[i][0] > LOCALESSTR_[j][0]:
                for k in range(4):
                    aux = LOCALESSTR_[i][k]
                    LOCALESSTR_[i][k] = LOCALESSTR_[j][k]
                    LOCALESSTR_[j][k] = aux

    locales_activos = [local for local in LOCALESSTR_ if local[3] == "A"]

    filas, cols = 10, 5
    mapa_locales = [[' ' for _ in range(cols)] for _ in range(filas)]

    # Coloca los codigos de los locales activos en el mapa consecutivamente
    for i in range(localescreados):
        fila = i // cols
        columna = i % cols
        mapa_locales[fila][columna] = str(LOCALESINT[i][0])  # Usa LOCALESINT para conseguir el codigo del local

    # Muestra el mapa con colores y los codigos de los locales
    for fila in mapa_locales:
        print("+" + "+".join(["-" * 6 for _ in range(cols)]) + "+")
        for codigo in fila:
            color = Back.YELLOW + Fore.BLACK
            if codigo != ' ':
                color = Back.GREEN + Fore.BLACK
            print(f"{color}{codigo:^6}", end="")
            print("|", end="")
        print()
    print("+" + "+".join(["-" * 6 for _ in range(cols)]) + "+")

def gestionar_descuentos():
    construccionadm()

def aceptar_rechazar_pedido_descuento():
    construccionadm()

def reporte_uso_descuentos():
    construccionadm()

def menu_dueño_local(usuario):
    opcion = -1
    
    
    while opcion != 0:   
        print(Fore.CYAN + "\n--- Menú Dueño de Local ---" + Style.RESET_ALL)
        print("1. Gestión de descuentos")
        print("2. Aceptar / Rechazar pedido de descuento")
        print("3. Reporte de uso de descuentos")
        print("0. Volver")
        opcion = input("Ingrese una opción: ")
        
        while (validarEnteros(opcion, 0, 3)):
            opcion = input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Entre 0 y 3:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
        opcion = int(opcion)

        if opcion == 1:
            ver_mis_locales(usuario)
        elif opcion == 2:
            ver_informacion_local()
        elif opcion == 0:
            print("Volviendo al menú anterior.")
            
        else:
            print(Fore.RED + "Opción inválida. Intente nuevamente." + Style.RESET_ALL)

def ver_mis_locales(usuario):
    print(Fore.CYAN + "\n--- Mis Locales ---" + Style.RESET_ALL)
    mis_locales = [local for local in LOCALESSTR_ if local[4] == usuario[0]]

    if not mis_locales:
        print(Fore.YELLOW + "Usted no es dueño de ningún local." + Style.RESET_ALL)
    else:
        for local in mis_locales:
            print(f"Nombre: {local[1]}")
            print(f"Ubicación: {local[2]}")
            print(f"Rubro: {local[3]}")
            print()

def ver_informacion_local():
    print(Fore.CYAN + "Información de un Local" + Style.RESET_ALL)
    cod_local = int(input("Ingrese el código del local: "))

    # Buscar el local por su código
    locales_encontrados = buscar_local_por_codigo(cod_local)

    if not locales_encontrados:
        print(Fore.RED + "No se encontró un local con ese código." + Style.RESET_ALL)
    else:
        local = locales_encontrados[0]
        print(f"Código: {local[0]}")
        print(f"Nombre: {local[1]}")
        print(f"Ubicación: {local[2]}")
        print(f"Rubro: {local[3]}")

# Funciones para el menú de cliente
def menu_cliente():
    opcion = -1
    
    while opcion != 0:
        print(Fore.CYAN + "\n--- Menú Cliente ---" + Style.RESET_ALL)
        print("1. Registrarme")
        print("2. Buscar descuentos en locales")
        print("3. Solicitar descuento")
        print("4. Ver novedades")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")
        while (validarEnteros(opcion, 0, 4)):
            opcion = input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Entre 0 y 4:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
        opcion = int(opcion)
        if opcion == 1:
            registrarme_como_cliente()
        elif opcion == 2:
            buscar_descuentos_en_locales()
        elif opcion == 3:
            solicitar_descuento()
        elif opcion == 4:
            ver_novedades()
        elif opcion == 0:
            print("Volviendo al menú principal.")
        else:
            print(Fore.RED + "Opción inválida. Intente nuevamente." + Style.RESET_ALL)

def registrarme_como_cliente():
    construccionadm()

def buscar_descuentos_en_locales():
    construccionadm()

def solicitar_descuento():
    construccionadm()

def ver_novedades():
    construccionadm()

# Programa principal
def main():
    inicializar()
    # Inicializar colorama para los colores en la consola
    init(autoreset=True)
    global intentos

    Opc = -1 
    while(Opc != 0):
        os.system('cls')
        print("--Bienvenido--")
        print("1. Iniciar sesión")
        print("2. Salir")
        Opc= input(Fore.BLUE+Style.BRIGHT+f'\nIngrese la opción que desea operar:{Style.RESET_ALL} ')
        while (validarEnteros(Opc, 1, 2)):
            Opc = input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Entre 1 y 2:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
        Opc = int(Opc)
        if (Opc == 1):
            Opc = int(Opc)
            iniciar_sesion()
        elif (Opc == 2):
            print(Style.RESET_ALL+'')
            print('¿Está seguro de que desea salir del programa?')
            print(Fore.RED+Style.BRIGHT+f'\nRecuerde que esta acción NO se puede deshacer\n')
            print(f'S - {Style.RESET_ALL}Salir')
            print(f'{Fore.GREEN+Style.BRIGHT}C - {Style.RESET_ALL}Cancelar')
            Confirmacion=str(input(Style.RESET_ALL+'\nIngrese una opción: ').upper())
            while(Confirmacion!='S' and Confirmacion!='C'):
                print('')
                Confirmacion=str(input(Fore.RED+Style.BRIGHT+f'Opción incorrecta, intentalo nuevamente{Style.RESET_ALL}: ').upper())  
            if (Confirmacion =='S'):
                print(Fore.GREEN+Style.BRIGHT+'\nGracias por usar este programa!')
                intentos = 5
                Opc = 0
            elif (Confirmacion=="C"):
                Opc=-1
        else:
            print(Style.RESET_ALL+'')
            input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Ingrese una tecla para volver:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
            Opc = -1
                
if __name__ == "__main__":
    main()