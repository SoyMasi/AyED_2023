import os, os.path, getpass, time
from colorama import init, Fore, Back, Style

# Algoritmos y Estructuras de Datos 2023:
# Comision 110 - T.T
# Maximiliano Jesús Gomez

# Variables
# indumentaria, perfumeria, comida, cRubroMax, cRubroMin, intentos , nro, Opc = int
# usuario_Admin, contraseña_Admin, nombre, ubicacion, rubro, maximo, minimo, usuario, contraseña = str
# crear, opci = char


def inicializar():
    global indumentariaC, perfumeriaC, comidaC, maximo, minimo, cRubroMin, cRubroMax, usuario_Admin, contraseña_Admin
    indumentariaC, perfumeriaC, comidaC , cRubroMax, cRubroMin= 0, 0, 0, 0, 0
    maximo = 'Ninguno, no hay locales ingresados'
    minimo = 'Ninguno, no hay locales ingresados'
    usuario_Admin = 'admin@shopping.com'
    contraseña_Admin = '12345'
    
    login()


def validarEnteros(nro, min, max):
    try:
        nro = int(nro)
        if nro >= min and nro <= max:
            return False
        else:
            return True
    except:
        return True
    

def longitudCaracteres(caracteres, caso, tipo):
    global nombre, ubicacion
    
    if tipo == True or tipo == False and caso == 1:
        if caracteres > 100:
            print(f'{Fore.RED+Style.BRIGHT}Error, el nombre debe contener menos de 100 caracteres.{Style.RESET_ALL}')
            while caracteres > 100:
                print(f'{Fore.RED+Style.BRIGHT}Error, el nombre debe contener menos de 100 caracteres.{Style.RESET_ALL}')
                nombre = str(input('Ingresa nuevamente el nombre del local: '))
                caracteres = len(nombre)
                tipo = nombre.isalnum()
                
    elif tipo == True or tipo == False and caso == 2:
        if caracteres > 50:
            print(f'{Fore.RED+Style.BRIGHT}Error, la ubicación debe contener menos de 50 caracteres')
            while caracteres > 50:
                print(f'{Fore.RED+Style.BRIGHT}Error, la ubicación debe contener menos de 50 caracteres.{Style.RESET_ALL}')
                ubicacion = str(input('Ingresa nuevamente la ubicación: '))
                caracteres = len(ubicacion)
                tipo = ubicacion.isalnum()
                
    else:
        print(f'{Fore.RED+Style.BRIGHT}Error, valor incorrecto{Style.RESET_ALL}')
        
        
def maximoRubro():
    global maximo , cRubroMax
    
    if perfumeriaC < comidaC > indumentariaC:
        maximo = 'comida'
        cRubroMax = comidaC
    elif comidaC < perfumeriaC > indumentariaC:
        maximo = 'perfumeria'
        cRubroMax = perfumeriaC
    elif comidaC < indumentariaC > perfumeriaC:
        maximo = 'indumentaria' 
        cRubroMax = indumentariaC
    elif comidaC == perfumeriaC > indumentariaC:
        maximo = 'comida y perfumeria'
        cRubroMax = comidaC
    elif comidaC == indumentariaC > perfumeriaC:
        maximo = 'comida e indumentaria'
        cRubroMax = comidaC
    elif perfumeriaC == indumentariaC > comidaC:
        maximo = 'perfumeria e indumentaria'
        cRubroMax = perfumeriaC


def minimoRubro():
    global minimo, cRubroMin

    if perfumeriaC > comidaC < indumentariaC:
        minimo = 'comida'
        cRubroMin = comidaC
    elif comidaC > perfumeriaC < indumentariaC:
        minimo = 'perfumeria'
        cRubroMin = perfumeriaC
    elif comidaC > indumentariaC < perfumeriaC:
        minimo = 'indumentaria'
        cRubroMin = indumentariaC
    elif comidaC == perfumeriaC < indumentariaC:
        minimo = 'comida y perfumeria'
        cRubroMin = comidaC
    elif comidaC == indumentariaC < perfumeriaC:
        minimo = 'comida e indumentaria'
        cRubroMin = comidaC
    elif perfumeriaC == indumentariaC < comidaC:
        minimo = 'perfumeria e indumentaria'
        cRubroMin = indumentariaC
    
 
def login():
    global intentos
    
    intentos = 0
    
    os.system('cls')
    while intentos < 3:
        usuario = str(input(f'Ingrese nombre de usuario: '))
        contraseña = getpass.getpass('Ingrese la contraseña: ') 
        if usuario == usuario_Admin and contraseña == contraseña_Admin:
            print(f'{Fore.BLUE+Style.BRIGHT}\nIngresando usuario como administrador exitosamente!{Style.RESET_ALL}')
            print(f'{Fore.GREEN+Style.BRIGHT}Bienvenido admin!{Style.RESET_ALL}')
            print('\nEntrando a menu de administracion ..')
            time.sleep(3)
            menu()
        else:
            intentos += 1
            print(f'\n{Fore.RED+Style.BRIGHT}Nombre de usuario o contraseña incorrectos, intentelo de nuevo{Style.RESET_ALL}')
    if intentos == 5:
        print('')
    else:
        print(f'\n{Fore.RED+Style.BRIGHT}Se han alcanzado el numero maximo de intentos fallidos, se cerrara el programa.{Style.RESET_ALL}')
            
    
def pantalla():
    print(f'''{Fore.BLUE+Style.BRIGHT}\n---------------MENU ADMINISTRADOR---------------''')
    print(f'''{Style.RESET_ALL}\n1.    Gestión de locales 
2.    Crear cuentas de dueños de locales 
3.    Aprobar / Denegar solicitud de descuento 
4.    Gestión de Novedades 
5.    Reporte de utilización de descuentos
0.    Salir del Programa\n
{Fore.BLUE+Style.BRIGHT}--------------------------------------------{Style.RESET_ALL}''')
    
    
def pantalla_GstLocal():
    print(f'''{Fore.CYAN+Style.BRIGHT}\n---------------GESTIÓN DE LOCALES---------------''')
    print(f'''{Style.RESET_ALL}\na)    Crear locales
b)    Modificar locales
c)    Eliminar local
d)    Volver\n
{Fore.CYAN+Style.BRIGHT}--------------------------------------------{Style.RESET_ALL}''')
    
    
def pantalla_GstNovedades():
    print(f'''{Fore.YELLOW+Style.BRIGHT}\n---------------GESTIÓN DE NOVEDADES---------------''')
    print(f'''{Style.RESET_ALL}\na)    Crear novedad 
b)    Modificar novedad
c)    Eliminar novedad
d)    Ver reporte de novedades  
e)    Volver\n
{Fore.YELLOW+Style.BRIGHT}--------------------------------------------{Style.RESET_ALL}''')
    

def pantalla_Construccion():

    opci = ''
    print(Fore.RED+Style.BRIGHT+'\nEsta funcionalidad se encuentra en construccion!')
    opci = str(input(Style.RESET_ALL +'Por favor ingrese * para volver al menu anterior: '))
    while opci != '*':
        print(Fore.RED+Style.BRIGHT+'Opcion incorrecta.')
        opci = str(input(Style.RESET_ALL +'Por favor ingrese * para volver al menu anterior: '))
    
    
def gestionLocales():
    
    Opci = '' 
    while (Opci.upper() != 'D'):
        os.system('cls')
        pantalla_GstLocal()   
        Opci = str(input(Fore.CYAN+Style.BRIGHT+'\nIngrese la opción que desea operar: '+Style.RESET_ALL).upper())
        while (Opci<'A' or Opci>'C') and (Opci!='D'):
            Opci = str(input(Fore.RED+Style.BRIGHT+f'Opción incorrecta {Style.RESET_ALL}- Entre A y D [D para Volver]: '+Style.RESET_ALL).upper())
        if(Opci == 'B') or (Opci == 'C'):
            pantalla_Construccion()
        elif(Opci == 'A'):
            crearLocales()
        

def gestionNovedades():
    
    Opci = '' 
    while (Opci.upper() != 'E'):
        os.system('cls')
        pantalla_GstNovedades()
        Opci = str(input(Fore.YELLOW+Style.BRIGHT+f'\nIngrese la opción que desea operar: {Style.RESET_ALL} ').upper())
        while (Opci<'A' or Opci>'D') and (Opci!='E'):
            Opci = str(input(Fore.RED+Style.BRIGHT+f'Opción incorrecta {Style.RESET_ALL}- Entre A y D [E para Volver]: a').upper())
        if(Opci == 'A') or (Opci == 'B') or (Opci == 'C') or (Opci == 'D'):
            pantalla_Construccion()
        
                       
def crearLocales():
    global indumentariaC, perfumeriaC, comidaC, maximo, minimo, caracteres, tipo, cRubroMax, cRubroMin
    
    print(f'{Fore.GREEN+Style.BRIGHT}Bienvenido al menu de ingreso de locales!{Style.RESET_ALL}\n')
    crear = input(f'Desea crear un local? [{Fore.GREEN+Style.BRIGHT}SI {Style.RESET_ALL}/ {Fore.RED+Style.BRIGHT}NO{Style.RESET_ALL}] : ').upper()
    
    while(crear != 'SI' and crear != 'NO'):
        print(f'{Fore.RED+Style.BRIGHT}Opcion Incorrecta.{Style.RESET_ALL}')
        crear = input(f'Ingrese [{Fore.GREEN+Style.BRIGHT}SI / {Fore.RED+Style.BRIGHT}NO{Style.RESET_ALL}] : ').upper()
    while(crear != 'NO' and crear == 'SI'):
        nombre = str(input('Ingrese el nombre del local: '))
        caracteres = len(nombre)
        tipo = nombre.isalnum()
        longitudCaracteres(caracteres, 1, tipo)
        opci = str(input(f'El nombre del local es [{Fore.BLUE+Style.BRIGHT}{nombre}{Style.RESET_ALL}] si quiere modificarlo pulse [{Fore.GREEN+Style.BRIGHT}S{Style.RESET_ALL}] si no , pulse [{Fore.CYAN+Style.BRIGHT}C{Style.RESET_ALL}]: ')).upper()
        if opci == 'S':
            nombre = str(input('Ingrese el nombre del local: '))
            caracteres = len(nombre)
            tipo = nombre.isalnum()
            longitudCaracteres(caracteres, 1, tipo)
            print(f'{Fore.GREEN+Style.BRIGHT}\nNombre del local ingresado, proceda a ingresar la ubicación!{Style.RESET_ALL}')
        else: 
            print(f'{Fore.GREEN+Style.BRIGHT}\nNombre del local ingresado, proceda a ingresar la ubicación!\n{Style.RESET_ALL}')
        
        ubicacion = str(input('Ingrese la ubicación del local: '))
        caracteres = len(ubicacion)
        tipo = ubicacion.isalnum()
        longitudCaracteres(caracteres, 2, tipo)
        opci = str(input(f'La ubicación del local es [{Fore.BLUE+Style.BRIGHT}{ubicacion}{Style.RESET_ALL}] si quiere modificarlo pulse [{Fore.GREEN+Style.BRIGHT}S{Style.RESET_ALL}] si no , pulse [{Fore.CYAN+Style.BRIGHT}C{Style.RESET_ALL}]: ')).upper()
        
        if opci == 'S':
            ubicacion = str(input('Ingrese la ubicación local: '))
            caracteres = len(ubicacion)
            tipo = ubicacion.isalnum()
            longitudCaracteres(caracteres, 1, tipo)
            print(f'{Fore.GREEN+Style.BRIGHT}\nUbicación ingresada con exito, proceda a ingresar el rubro!\n{Style.RESET_ALL}')
        else: 
            
            print(f'{Fore.GREEN+Style.BRIGHT}\nUbicación ingresada con exito, proceda a ingresar el rubro!{Style.RESET_ALL}')
        rubro = input(f'\nIngrese el rubro del local {Fore.BLUE+Style.BRIGHT}(indumentaria, perfumeria o comida){Style.RESET_ALL}: ').lower()
        
        while(rubro != 'indumentaria' and rubro !='perfumeria' and rubro !='comida'):
            rubro = input(f'{Fore.RED+Style.BRIGHT}Rubro inexistente{Style.RESET_ALL}, ingrese un rubro válido ({Fore.GREEN+Style.BRIGHT}indumentaria, perfumeria o comida{Style.RESET_ALL}): ')
            
        if (rubro == 'comida'):
            comidaC = comidaC + 1
        elif(rubro == 'perfumeria'):
            perfumeriaC = perfumeriaC + 1
        elif(rubro == 'indumentaria'):
            indumentariaC = indumentariaC + 1
        
        print (f'{Fore.GREEN+Style.BRIGHT}\nLocal Ingresado exitosamente!{Style.RESET_ALL}\n')
        crear = input(f'\nDesea crear otro local? [{Fore.GREEN+Style.BRIGHT}SI{Style.RESET_ALL}/{Fore.RED+Style.BRIGHT}NO{Style.RESET_ALL}]: ').upper()
        while (crear != 'NO' and crear != 'SI'):
            print('Opcion Incorrecta')
            crear = input(f'Desea crear otro local? [{Fore.GREEN+Style.BRIGHT}SI{Style.RESET_ALL}/{Fore.RED+Style.BRIGHT}NO{Style.RESET_ALL}]: ').upper()
        if crear == 'SI': 
            print (f'{Fore.GREEN+Style.BRIGHT}\nLocal Ingresado exitosamente!{Style.RESET_ALL}\n')
            print('Ingresando nuevo local ..')

    if comidaC == perfumeriaC == indumentariaC != 0:
        print(f'Todos los rubros tienen la misma cantidad de locales [{comidaC}]')
        input('Ingrese una tecla para volver: ')
        
    else:
        maximoRubro()
        minimoRubro()
        
        print(f'Los rubros con más locales en esto momentos son [{Fore.BLUE+Style.BRIGHT}{maximo}{Style.RESET_ALL}] con una cantidad de [{Fore.GREEN+Style.BRIGHT}{cRubroMax}{Style.RESET_ALL}]')
        print(f'Los rubros con menos locales en estos momentos son [{Fore.BLUE+Style.BRIGHT}{minimo}{Style.RESET_ALL}] con una cantidad de [{Fore.GREEN+Style.BRIGHT}{cRubroMin}{Style.RESET_ALL}]\n')
        input('Ingrese una tecla para volver: ')


def menu():
    global intentos
    
    Opc = -1 
    while(Opc != 0):
        os.system('cls')
        pantalla()
        Opc= input(Fore.BLUE+Style.BRIGHT+f'\nIngrese la opción que desea operar:{Style.RESET_ALL} ')
        while (validarEnteros(Opc, 0, 5)):
            Opc = input(Fore.RED+Style.BRIGHT+f'Opción incorrecta - Entre 0 y 5:{Style.RESET_ALL} ')
            print(Style.RESET_ALL)
        Opc = int(Opc)
        if (Opc == 1):
            gestionLocales()
        elif (Opc == 2):
            pantalla_Construccion()
        elif (Opc == 3):
            pantalla_Construccion()
        elif (Opc == 4):
            gestionNovedades()
        elif (Opc == 5):
            pantalla_Construccion()
        else:
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
            elif (Confirmacion =='C'):
                Opc= -1
        
        
### Programa Principal ###
inicializar()