import random
from datetime import datetime, timedelta

# Constantes
TIPOS_SOCIO = ["Junior/Menor", "Standard", "Platino", "ORO", "Vitalicio"]
PRECIOS_CUOTA = {"Junior/Menor": 5000, "Standard": 8000, "Platino": 6000, "ORO": 4000, "Vitalicio": 0}
PASES = ["Recreativo", "Tenis", "Futbol"]
PRECIOS_PASES = {"Recreativo": {"Junior/Menor": 500, "Standard": 800, "Platino": 600, "ORO": 400, "Vitalicio": 300},
                 "Tenis": {"Junior/Menor": 1500, "Standard": 1500, "Platino": 800, "ORO": 800, "Vitalicio": 500},
                 "Futbol": {"Junior/Menor": 1200, "Standard": 1200, "Platino": 1000, "ORO": 1000, "Vitalicio": 700}}
COSTOS_MANTENIMIENTO = {"Junior/Menor": 300, "Standard": 500, "Platino": 350, "ORO": 250, "Vitalicio": 200}

MESES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

def generar_datos(mes, año):
    """Genera datos aleatorios para el mes y año especificados."""
    datos = []
    num_socios = random.randint(2000, 5000)
    
    # Calcula el 30% de los socios que deben tener al menos una actividad
    min_socios_con_actividad = int(num_socios * 0.3)
    socios_con_actividad = 0
    
    for i in range(num_socios):
        id_socio = 1000 + i  # ID de cliente de 4 dígitos, comenzando desde 1000
        tipo_socio = random.choice(TIPOS_SOCIO)
        
        # Determina si el socio tendrá actividad
        if socios_con_actividad < min_socios_con_actividad:
            tiene_actividad = True
            socios_con_actividad += 1
        else:
            tiene_actividad = random.random() < 0.3  # 30% de probabilidad
            
        if tiene_actividad:
            # Calcula la cantidad de actividades del socio (entre 1 y 5)
            num_actividades = random.randint(1, 5)
        else:
            num_actividades = 0
            
        # Genera las actividades del socio
        for _ in range(num_actividades):
            # Genera una fecha válida dentro del mes
            while True:
                dia = random.randint(1, 31)
                try:
                    fecha = datetime(año, mes, dia).date()
                    break  # Sale del bucle si la fecha es válida
                except ValueError:
                    pass  # Intenta con otro día si la fecha no es válida
                    
            pase_comprado = random.choice(PASES)
            datos.append({
                "fecha": fecha,
                "id_socio": id_socio,
                "tipo_socio": tipo_socio,
                "pase_comprado": pase_comprado
            })
            
    return datos

def totales_mes(datos, mes, año):
    """Calcula y muestra los totales del mes."""
    total_facturado = 0
    total_ingresos = 0
    socios_unicos = set()
    actividades_tenis = 0
    actividades_futbol = 0
    actividades_recreativo = 0
    total_costo_mantenimiento = 0
    
    for dato in datos:
        if dato["fecha"].month == mes and dato["fecha"].year == año:
            id_socio = dato["id_socio"]
            tipo_socio = dato["tipo_socio"]
            pase_comprado = dato["pase_comprado"]
            
            # Calcula la facturación del socio (cuota social + pase)
            facturacion_socio = PRECIOS_CUOTA[tipo_socio] + PRECIOS_PASES[pase_comprado][tipo_socio]
            total_facturado += facturacion_socio
            
            # Suma el costo de mantenimiento del socio
            total_costo_mantenimiento += COSTOS_MANTENIMIENTO[tipo_socio]
            
            # Suma el costo del pase comprado
            total_ingresos += PRECIOS_PASES[pase_comprado][tipo_socio]
            
            # Agrega el ID del socio al conjunto de socios únicos
            socios_unicos.add(id_socio)
            
            # Suma las actividades según el tipo de pase
            if pase_comprado == "Tenis":
                actividades_tenis += 1
            elif pase_comprado == "Futbol":
                actividades_futbol += 1
            else:
                actividades_recreativo += 1
    
    num_socios_unicos = len(socios_unicos)
    
    nombre_mes = MESES[mes]  # Obtiene el nombre del mes del diccionario
    print(f"Mes: {nombre_mes} {año}")
    print(f"Total facturado: ${total_facturado}")
    print(f"Total ingresos al club registrados: {total_ingresos}")
    print(f"Total socios únicos: {num_socios_unicos}")
    print(f"Total actividades PASE tenis registradas: {actividades_tenis}")
    print(f"Total actividades PASE futbol registradas: {actividades_futbol}")
    print(f"Total actividades PASE recreativo: {actividades_recreativo}")
    print(f"Total Costo mantenimiento: ${total_costo_mantenimiento}")

def total_por_tipo_socio(datos, mes, año):
    """Calcula y muestra los totales por tipo de socio."""
    print("Seleccione el tipo de socio:")
    print()
    for i, tipo in enumerate(TIPOS_SOCIO):
        print(f"{i+1}. {tipo}")
    print()
        
    while True:
        try:
            opcion = int(input("Ingrese el número del tipo de socio: "))
            print()
            if 1 <= opcion <= len(TIPOS_SOCIO):
                tipo_socio_seleccionado = TIPOS_SOCIO[opcion-1]
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
    
    total_facturado = 0
    total_ingresos = 0
    socios_unicos = set()
    actividades_tenis = 0
    actividades_futbol = 0
    actividades_recreativo = 0
    total_costo_mantenimiento = 0
    
    for dato in datos:
        if dato["fecha"].month == mes and dato["fecha"].year == año and dato["tipo_socio"] == tipo_socio_seleccionado:
            id_socio = dato["id_socio"]
            tipo_socio = dato["tipo_socio"]
            pase_comprado = dato["pase_comprado"]
            
            # Calcula la facturación del socio (cuota social + pase)
            facturacion_socio = PRECIOS_CUOTA[tipo_socio] + PRECIOS_PASES[pase_comprado][tipo_socio]
            total_facturado += facturacion_socio
            
            # Suma el costo de mantenimiento del socio
            total_costo_mantenimiento += COSTOS_MANTENIMIENTO[tipo_socio]
            
            # Suma el costo del pase comprado
            total_ingresos += PRECIOS_PASES[pase_comprado][tipo_socio]
            
            # Agrega el ID del socio al conjunto de socios únicos
            socios_unicos.add(id_socio)
            
            # Suma las actividades según el tipo de pase
            if pase_comprado == "Tenis":
                actividades_tenis += 1
            elif pase_comprado == "Futbol":
                actividades_futbol += 1
            else:
                actividades_recreativo += 1
    
    num_socios_unicos = len(socios_unicos)
    
    nombre_mes = MESES[mes]  # Obtiene el nombre del mes del diccionario
    print(f"Mes: {nombre_mes} {año}")
    print(f"TIPO SOCIO: {tipo_socio_seleccionado}")
    print(f"Total facturado: ${total_facturado}")
    print(f"Total ingresos al club registrados: {total_ingresos}")
    print(f"Total socios únicos: {num_socios_unicos}")
    print(f"Total actividades PASE tenis registradas: {actividades_tenis}")
    print(f"Total actividades PASE futbol registradas: {actividades_futbol}")
    print(f"Total actividades PASE recreativo: {actividades_recreativo}")
    print(f"Total Costo mantenimiento: ${total_costo_mantenimiento}")
    print()

def detalle_por_clientes(datos, mes, año):
    """Muestra un resumen por cliente, ordenado por total facturado descendente."""
    detalles = {}
    
    for dato in datos:
        if dato["fecha"].month == mes and dato["fecha"].year == año:
            id_socio = dato["id_socio"]
            tipo_socio = dato["tipo_socio"]
            pase_comprado = dato["pase_comprado"]
            
            # Calcula la facturación del socio (cuota social + pase)
            facturacion_socio = PRECIOS_CUOTA[tipo_socio] + PRECIOS_PASES[pase_comprado][tipo_socio]
            
            # Agrega la facturación al diccionario de detalles por cliente
            if id_socio in detalles:
                detalles[id_socio]["total_facturado"] += facturacion_socio
                detalles[id_socio]["total_ingresos"] += PRECIOS_PASES[pase_comprado][tipo_socio]
                detalles[id_socio]["total_actividades"] += 1
            else:
                detalles[id_socio] = {
                    "total_facturado": facturacion_socio,
                    "total_ingresos": PRECIOS_PASES[pase_comprado][tipo_socio],
                    "total_actividades": 1
                }
    
    # Ordena los clientes por total facturado descendente
    clientes_ordenados = sorted(detalles.items(), key=lambda x: x[1]["total_facturado"], reverse=True)
    
    print(f"Mes: {mes}/{año}")
    print("ID Cliente\tTotal ingresos al mes\tTotal facturado\tTotal actividades")
    for id_socio, detalle in clientes_ordenados:
        print(f"{id_socio}\t\t${detalle['total_ingresos']}\t\t${detalle['total_facturado']}\t\t{detalle['total_actividades']}")

def detalle_por_dia(datos, mes, año):
    """Muestra un resumen por día, ordenado por día ascendente."""
    detalles = {}
    
    for dato in datos:
        if dato["fecha"].month == mes and dato["fecha"].year == año:
            fecha = dato["fecha"]
            tipo_socio = dato["tipo_socio"]
            pase_comprado = dato["pase_comprado"]
            
            # Calcula la facturación del socio (cuota social + pase)
            facturacion_socio = PRECIOS_CUOTA[tipo_socio] + PRECIOS_PASES[pase_comprado][tipo_socio]
            
            # Agrega la facturación al diccionario de detalles por día
            if fecha in detalles:
                detalles[fecha]["total_facturado"] += facturacion_socio
                detalles[fecha]["total_ingresos"] += PRECIOS_PASES[pase_comprado][tipo_socio]
                detalles[fecha]["total_actividades"] += 1
            else:
                detalles[fecha] = {
                    "total_facturado": facturacion_socio,
                    "total_ingresos": PRECIOS_PASES[pase_comprado][tipo_socio],
                    "total_actividades": 1
                }
    
    # Ordena los días por fecha ascendente
    dias_ordenados = sorted(detalles.items(), key=lambda x: x[0])
    
    print(f"Mes: {mes}/{año}")
    print("Día\tTotal ingresos por día\tTotal facturado\tTotal actividades")
    for fecha, detalle in dias_ordenados:
        print(f"{fecha.strftime('%d/%m/%Y')}\t\t${detalle['total_ingresos']}\t\t${detalle['total_facturado']}\t\t{detalle['total_actividades']}")

def detalle_del_dia(datos, mes, año):
    """Muestra un detalle de los socios que asistieron a un día específico."""
    while True:
        try:
            dia = int(input("Ingrese el día que desea consultar: "))
            fecha_consulta = datetime(año, mes, dia).date()
            break
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")
    
    detalles = []
    
    for dato in datos:
        if dato["fecha"] == fecha_consulta:
            detalles.append(dato)
    
    # Ordena los detalles por ID de cliente ascendente
    detalles_ordenados = sorted(detalles, key=lambda x: x["id_socio"])
    
    print(f"Día elegido: {fecha_consulta.strftime('%d de %B de %Y')}")
    print("ID Cliente\tTipo SOCIO\tActividad realizada")
    for detalle in detalles_ordenados:
        print(f"{detalle['id_socio']}\t\t{detalle['tipo_socio']}\t\t{detalle['pase_comprado']}")

def dia_con_mayor_ingresos(datos, mes, año):
    """Muestra el día con mayor ingresos en el mes."""
    detalles = {}
    
    for dato in datos:
        if dato["fecha"].month == mes and dato["fecha"].year == año:
            fecha = dato["fecha"]
            tipo_socio = dato["tipo_socio"]
            pase_comprado = dato["pase_comprado"]
            
            # Calcula la facturación del socio (cuota social + pase)
            facturacion_socio = PRECIOS_CUOTA[tipo_socio] + PRECIOS_PASES[pase_comprado][tipo_socio]
            
            # Agrega la facturación al diccionario de detalles por día
            if fecha in detalles:
                detalles[fecha]["total_facturado"] += facturacion_socio
                detalles[fecha]["total_ingresos"] += PRECIOS_PASES[pase_comprado][tipo_socio]
                detalles[fecha]["total_actividades"] += 1
                if pase_comprado in detalles[fecha]["pases"]:
                    detalles[fecha]["pases"][pase_comprado] += 1
                else:
                    detalles[fecha]["pases"][pase_comprado] = 1
            else:
                detalles[fecha] = {
                    "total_facturado": facturacion_socio,
                    "total_ingresos": PRECIOS_PASES[pase_comprado][tipo_socio],
                    "total_actividades": 1,
                    "pases": {pase_comprado: 1}
                }
    
    # Encuentra el día con mayor ingresos
    dia_mayor_ingresos = None
    mayor_ingreso = 0
    
    for fecha, detalle in detalles.items():
        if detalle["total_ingresos"] > mayor_ingreso:
            mayor_ingreso = detalle["total_ingresos"]
            dia_mayor_ingresos = fecha
    
    # Encuentra el tipo de pase más comprado en ese día
    pases = detalles[dia_mayor_ingresos]["pases"]
    pase_mas_comprado = max(pases, key=pases.get)
    
    nombre_mes = MESES[mes]  # Obtiene el nombre del mes del diccionario
    print(f"Mes: {nombre_mes} {año}")
    # Formatea la fecha usando el diccionario para el nombre del mes
    nombre_mes_dia = MESES[dia_mayor_ingresos.month]
    print(f"Día con mayor ingresos: {dia_mayor_ingresos.day} de {nombre_mes_dia} de {dia_mayor_ingresos.year}")
    print(f"Total facturado: ${detalles[dia_mayor_ingresos]['total_facturado']}")
    print(f"Cantidad total de ingresos: {detalles[dia_mayor_ingresos]['total_actividades']}")
    print(f"Tipo de pase más comprado: {pase_mas_comprado}")
def ver_actividades_socio(datos, id_socio):
    # Muestra las actividades de un socio específico.
    actividades = [dato for dato in datos if dato["id_socio"] == id_socio]
    
    if not actividades:
        print(f"No se encontraron actividades para el socio con ID {id_socio}.")
        return
    
    print(f"Actividades del socio ID {id_socio}:")
    for actividad in actividades:
        fecha = actividad["fecha"].strftime('%d/%m/%Y')
        tipo_socio = actividad["tipo_socio"]
        pase_comprado = actividad["pase_comprado"]
        print(f"Fecha: {fecha}, Tipo Socio: {tipo_socio}, Pase Comprado: {pase_comprado}")
def menu_principal(datos, mes, año):
    """Muestra el menú principal y gestiona las opciones."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Totales mes")
        print("2. Total por tipo de Socio")
        print("3. Detalle por Clientes")
        print("4. Detalle por día")
        print("5. Detalle del día")
        print("6. Día con mayor ingresos")
        print("7. Buscar socio y ver sus actividades")
        print("8. Salir")
        print()
        
        opcion = input("Seleccione una opción: ")
        print()
        
        if opcion == "1":
            totales_mes(datos, mes, año)
        elif opcion == "2":
            total_por_tipo_socio(datos, mes, año)
        elif opcion == "3":
            detalle_por_clientes(datos, mes, año)
        elif opcion == "4":
            detalle_por_dia(datos, mes, año)
        elif opcion == "5":
            detalle_del_dia(datos, mes, año)
        elif opcion == "6":
            dia_con_mayor_ingresos(datos, mes, año)
        elif opcion == "7":
            while True:
                try:
                    id_socio = int(input("Ingrese el ID del socio (4 dígitos): "))
                    if 1000 <= id_socio < 10000:
                        ver_actividades_socio(datos, id_socio)
                        break
                    else:
                        print("ID inválido. Debe ser un número de 4 dígitos.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número.")
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Inicio del programa
if __name__ == "__main__":
    while True:
        try:
            mes = int(input("Ingrese el mes (1-12): "))
            año = int(input("Ingrese el año: "))
            if 1 <= mes <= 12:
                break
            else:
                print("Mes inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            
    datos = generar_datos(mes, año)
    menu_principal(datos, mes, año)