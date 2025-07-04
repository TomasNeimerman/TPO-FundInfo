import random

LISTA_TIPOS_SOCIO = ["Junior/Menor", "Standard", "Platino", "ORO", "Vitalicio"]
LISTA_PRECIOS_CUOTA = [5000, 8000, 6000, 4000, 0]
LISTA_COSTOS_MANTENIMIENTO = [300, 500, 350, 250, 200]

LISTA_PASES = ["Recreativo", "Tenis", "Futbol"]
MATRIZ_PRECIOS_PASES = [
    [500, 800, 600, 400, 300],
    [1500, 1500, 800, 800, 500],
    [1200, 1200, 1000, 1000, 700]
]

def leer_entero(mensaje, minimo, maximo):
    n = int(input(mensaje))
    while n < minimo or n > maximo:
        print("Valor fuera de rango. Debe estar entre", minimo, "y", maximo)
        n = int(input(mensaje))
    return n
def cant_dias_mes(mes,anio):
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            if (anio % 4 == 0):
                return 29
            else:
                return 28
def generar_datos_aleatorios(mes, anio, cant_dias):
    fechas_dia = []
    fechas_mes = []
    fechas_anio = []
    ids_socio = []
    indices_tipo_socio = []
    indices_pase = []
    datos = []

    cantidad_socios = random.randint(2000, 5000)
    cantidad_minima_actividad = int(cantidad_socios * 0.3)
    socios_con_actividad = 0

    for i in range(cantidad_socios):
        id_socio_actual = 1000 + i
        indice_socio = random.randint(0, len(LISTA_TIPOS_SOCIO) - 1)
        
        tiene_actividad = False
        if socios_con_actividad < cantidad_minima_actividad:
            tiene_actividad = True
            socios_con_actividad = socios_con_actividad + 1
        else:
            if random.randint(1, 10) <= 3:
                tiene_actividad = True

        if tiene_actividad:
            cantidad_actividades = random.randint(1, 5)
            for j in range(cantidad_actividades):
                dia = random.randint(1, cant_dias)
                indice_pase_actual = random.randint(0, len(LISTA_PASES) - 1)
                datos.append({
                    "fecha": f"{dia}/{mes}/{anio}",
                    "id_socio": id_socio_actual,
                    "tipo_socio": LISTA_TIPOS_SOCIO[indice_socio],
                    "pase_comprado": LISTA_PASES[indice_pase_actual]
                })
                fechas_dia.append(dia)
                fechas_mes.append(mes)
                fechas_anio.append(anio)
                ids_socio.append(id_socio_actual)
                indices_tipo_socio.append(indice_socio)
                indices_pase.append(indice_pase_actual)
                
    return fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, datos

def obtener_nombre_mes(numero_mes):
    match numero_mes:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return "Mes Invalido"

def totales_mes(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio):
    total_facturado = 0
    total_ingresos_pases = 0
    total_costo_mantenimiento = 0
    actividades_tenis = 0
    actividades_futbol = 0
    actividades_recreativo = 0
    socios_unicos = []

    for i in range(len(fechas_dia)):
        if fechas_mes[i] == mes and fechas_anio[i] == anio:
            indice_socio = indices_tipo_socio[i]
            indice_pase = indices_pase[i]
            
            precio_cuota = LISTA_PRECIOS_CUOTA[indice_socio]
            precio_pase = MATRIZ_PRECIOS_PASES[indice_pase][indice_socio]
            costo_mantenimiento = LISTA_COSTOS_MANTENIMIENTO[indice_socio]

            total_facturado = total_facturado + precio_cuota + precio_pase
            total_ingresos_pases = total_ingresos_pases + precio_pase
            total_costo_mantenimiento = total_costo_mantenimiento + costo_mantenimiento

            if ids_socio[i] not in socios_unicos:
                socios_unicos.append(ids_socio[i])
            
            if indice_pase == 1:
                actividades_tenis = actividades_tenis + 1
            elif indice_pase == 2:
                actividades_futbol = actividades_futbol + 1
            else:
                actividades_recreativo = actividades_recreativo + 1
    
    print("Mes:", obtener_nombre_mes(mes), anio)
    print("Total facturado: $", total_facturado)
    print("Total ingresos al club por pases: $", total_ingresos_pases)
    print("Total socios unicos:", len(socios_unicos))
    print("Total actividades PASE tenis:", actividades_tenis)
    print("Total actividades PASE futbol:", actividades_futbol)
    print("Total actividades PASE recreativo:", actividades_recreativo)
    print("Total Costo mantenimiento: $", total_costo_mantenimiento)

def total_por_tipo_socio(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio):
    print("Seleccione el tipo de socio:")
    for i in range(len(LISTA_TIPOS_SOCIO)):
        print(i + 1, ". ", LISTA_TIPOS_SOCIO[i])
    
    opcion = leer_entero("Ingrese el numero del tipo de socio: ", 1, len(LISTA_TIPOS_SOCIO))
    indice_socio_seleccionado = opcion - 1
    
    total_facturado = 0
    total_ingresos_pases = 0
    total_costo_mantenimiento = 0
    actividades_tenis = 0
    actividades_futbol = 0
    actividades_recreativo = 0
    socios_unicos = []

    for i in range(len(fechas_dia)):
        if fechas_mes[i] == mes and fechas_anio[i] == anio and indices_tipo_socio[i] == indice_socio_seleccionado:
            indice_pase = indices_pase[i]
            
            precio_cuota = LISTA_PRECIOS_CUOTA[indice_socio_seleccionado]
            precio_pase = MATRIZ_PRECIOS_PASES[indice_pase][indice_socio_seleccionado]
            costo_mantenimiento = LISTA_COSTOS_MANTENIMIENTO[indice_socio_seleccionado]

            total_facturado = total_facturado + precio_cuota + precio_pase
            total_ingresos_pases = total_ingresos_pases + precio_pase
            total_costo_mantenimiento = total_costo_mantenimiento + costo_mantenimiento

            if ids_socio[i] not in socios_unicos:
                socios_unicos.append(ids_socio[i])

            if indice_pase == 1:
                actividades_tenis = actividades_tenis + 1
            elif indice_pase == 2:
                actividades_futbol = actividades_futbol + 1
            else:
                actividades_recreativo = actividades_recreativo + 1

    print("Mes:", obtener_nombre_mes(mes), anio)
    print("TIPO SOCIO:", LISTA_TIPOS_SOCIO[indice_socio_seleccionado])
    print("Total facturado: $", total_facturado)
    print("Total ingresos al club por pases: $", total_ingresos_pases)
    print("Total socios unicos:", len(socios_unicos))
    print("Total actividades PASE tenis:", actividades_tenis)
    print("Total actividades PASE futbol:", actividades_futbol)
    print("Total actividades PASE recreativo:", actividades_recreativo)
    print("Total Costo mantenimiento: $", total_costo_mantenimiento)
    print()

def ordenar_listas_paralelas_desc(lista_a_ordenar, l1, l2, l3):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(lista_a_ordenar) - 1):
            if lista_a_ordenar[i] < lista_a_ordenar[i+1]:
                aux = lista_a_ordenar[i]
                lista_a_ordenar[i] = lista_a_ordenar[i+1]
                lista_a_ordenar[i+1] = aux

                aux = l1[i]
                l1[i] = l1[i+1]
                l1[i+1] = aux

                aux = l2[i]
                l2[i] = l2[i+1]
                l2[i+1] = aux

                aux = l3[i]
                l3[i] = l3[i+1]
                l3[i+1] = aux
                
                intercambio = True
    return lista_a_ordenar, l1, l2, l3

def detalle_por_clientes(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio):
    reporte_ids = []
    reporte_ingresos = []
    reporte_facturado = []
    reporte_actividades = []
    
    for i in range(len(fechas_dia)):
        if fechas_mes[i] == mes and fechas_anio[i] == anio:
            id_actual = ids_socio[i]
            indice_socio = indices_tipo_socio[i]
            indice_pase = indices_pase[i]
            
            precio_cuota = LISTA_PRECIOS_CUOTA[indice_socio]
            precio_pase = MATRIZ_PRECIOS_PASES[indice_pase][indice_socio]
            facturacion = precio_cuota + precio_pase
            
            pos = -1
            for j in range(len(reporte_ids)):
                if reporte_ids[j] == id_actual:
                    pos = j
            
            if pos != -1:
                reporte_facturado[pos] = reporte_facturado[pos] + facturacion
                reporte_ingresos[pos] = reporte_ingresos[pos] + precio_pase
                reporte_actividades[pos] = reporte_actividades[pos] + 1
            else:
                reporte_ids.append(id_actual)
                reporte_facturado.append(facturacion)
                reporte_ingresos.append(precio_pase)
                reporte_actividades.append(1)

    reporte_facturado, reporte_ids, reporte_ingresos, reporte_actividades = ordenar_listas_paralelas_desc(reporte_facturado, reporte_ids, reporte_ingresos, reporte_actividades)
    
    print("Mes:", mes, "/", anio)
    print("ID Cliente", "Total ingresos al mes", "Total facturado", "Total actividades")
    for i in range(len(reporte_ids)):
        print(reporte_ids[i], " $", reporte_ingresos[i], " $", reporte_facturado[i], " ", reporte_actividades[i])

def ver_actividades_socio(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, id_buscado):
    encontrado = False
    print("Actividades del socio ID", id_buscado, ":")
    for i in range(len(ids_socio)):
        if ids_socio[i] == id_buscado:
            dia = fechas_dia[i]
            mes = fechas_mes[i]
            anio = fechas_anio[i]
            tipo_socio = LISTA_TIPOS_SOCIO[indices_tipo_socio[i]]
            pase = LISTA_PASES[indices_pase[i]]
            
            print("Fecha: ", dia, "/", mes, "/", anio, ", Tipo Socio: ", tipo_socio, ", Pase Comprado: ", pase)
            encontrado = True
    
    if not encontrado:
        print("No se encontraron actividades para el socio con ID", id_buscado)
def detalle_por_dia(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio, cant_dias):
    daily_summary = {}

    for i in range(len(fechas_dia)):
        if fechas_mes[i] == mes and fechas_anio[i] == anio:
            day = fechas_dia[i]
            
            indice_socio = indices_tipo_socio[i]
            indice_pase = indices_pase[i]
            
            precio_cuota = LISTA_PRECIOS_CUOTA[indice_socio]
            precio_pase = MATRIZ_PRECIOS_PASES[indice_pase][indice_socio]
            costo_mantenimiento = LISTA_COSTOS_MANTENIMIENTO[indice_socio]

            if day not in daily_summary:
                daily_summary[day] = {
                    'total_actividades': 0,
                    'total_facturado': 0,
                    'total_costo': 0
                }
            
            daily_summary[day]['total_actividades'] += 1
            daily_summary[day]['total_facturado'] += precio_cuota + precio_pase
            daily_summary[day]['total_costo'] += costo_mantenimiento
    
    sorted_daily_summary = sorted(daily_summary.items())

    print(f"\n--- Detalle por Día para {obtener_nombre_mes(mes)} {anio} ---")
    print(f"{'Día'} {'Total ingresos por dia'} {'Total facturado'} {'Total costo'}")
    print("-" * 75)

    for day, data in sorted_daily_summary:
        print(f"{day}/{mes}/{anio} {data['total_actividades']} ${data['total_facturado']} ${data['total_costo']}")
    print("-" * 75)
    print()

def detalle_actividades_por_dia(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio, cant_dias):

    dia_elegido = leer_entero(f"Ingrese el día (1-{cant_dias}) para ver las actividades: ", 1, cant_dias)
    
    actividades_del_dia = []
    for i in range(len(fechas_dia)):
        if fechas_dia[i] == dia_elegido and fechas_mes[i] == mes and fechas_anio[i] == anio:
            actividades_del_dia.append({
                'id': ids_socio[i],
                'tipo_socio': LISTA_TIPOS_SOCIO[indices_tipo_socio[i]],
                'pase': LISTA_PASES[indices_pase[i]]
            })
    
    
    print(f"Día elegido: {dia_elegido} de {obtener_nombre_mes(mes)} {anio}")
    print("ID Cliente\tTipo SOCIO\tActividad realizada")
    for actividad in actividades_del_dia:
        print(f"{actividad['id']}\t\t{actividad['tipo_socio']}\t\t{actividad['pase']}")

def ver_actividades_socio(datos, id_socio_a_buscar):

    actividades_encontradas = []
    encontrado = False 
    for actividad in datos:
        
        if actividad["id_socio"] == id_socio_a_buscar:
            actividades_encontradas.append(actividad)
            encontrado = True 

    if not encontrado:
        print(f"No se encontraron actividades para el socio con ID {id_socio_a_buscar}.")
        return

    print(f"Actividades del socio ID {id_socio_a_buscar}:")
    for actividad in actividades_encontradas:
        fecha = actividad["fecha"]
        tipo_socio = actividad["tipo_socio"]
        pase_comprado = actividad["pase_comprado"]
        print(f"Fecha: {fecha}, Tipo Socio: {tipo_socio}, Pase Comprado: {pase_comprado}")


def dia_con_mayor_ingresos(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio, cant_dias):

    daily_data = {}

    for i in range(len(fechas_dia)):
        if fechas_mes[i] == mes and fechas_anio[i] == anio:
            dia_actual = fechas_dia[i]
            indice_socio = indices_tipo_socio[i]
            indice_pase = indices_pase[i]

            precio_cuota = LISTA_PRECIOS_CUOTA[indice_socio]
            precio_pase = MATRIZ_PRECIOS_PASES[indice_pase][indice_socio]
            
            if dia_actual not in daily_data:
                daily_data[dia_actual] = {
                    'total_facturado': 0,
                    'total_ingresos_pases': 0,
                    'pass_counts': {'Recreativo': 0, 'Tenis': 0, 'Futbol': 0}
                }
            
            daily_data[dia_actual]['total_facturado'] += (precio_cuota + precio_pase)
            daily_data[dia_actual]['total_ingresos_pases'] += precio_pase
            daily_data[dia_actual]['pass_counts'][LISTA_PASES[indice_pase]] += 1
    
    if not daily_data:
        print(f"No se encontraron actividades para el mes de {obtener_nombre_mes(mes)} {anio}.")
        return

    dia_max_ingresos = -1
    max_ingresos = -1

    for dia, data in daily_data.items():
        if data['total_ingresos_pases'] > max_ingresos:
            max_ingresos = data['total_ingresos_pases']
            dia_max_ingresos = dia

    if dia_max_ingresos != -1:
        data_max_dia = daily_data[dia_max_ingresos]
        
        most_purchased_pass = ""
        max_pass_count = -1

        for pass_type, count in data_max_dia['pass_counts'].items():
            if count > max_pass_count:
                max_pass_count = count
                most_purchased_pass = pass_type
            elif count == max_pass_count and most_purchased_pass == "": 
                most_purchased_pass = pass_type

        print(f"Día con mayor ingresos: {dia_max_ingresos} de {obtener_nombre_mes(mes)} {anio}")
        print(f"Total facturado: ${data_max_dia['total_facturado']}")
        print(f"Cantidad total de ingresos: ${data_max_dia['total_ingresos_pases']}")
        print(f"Tipo de pase más comprado: {most_purchased_pass}")
    else:
        print("No se pudieron determinar el día con mayores ingresos.")

def menu_principal(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio, cant_dias):
    opcion = ""
    while opcion != "8":
        print()
        print("--- Menu Principal ---")
        print("1. Totales mes")
        print("2. Total por tipo de Socio")
        print("3. Detalle por Clientes")
        print("4. Detalle por dia")
        print("5. Detalle de actividades por día")
        print("6. Día con mayor ingresos") 
        print("7. Ver actividades de un socio") 
        print("8. Salir") 
        print()
        
        opcion = input("Seleccione una opcion: ")
        print()
        
        if opcion == "1":
            totales_mes(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio)
        elif opcion == "2":
            total_por_tipo_socio(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio)
        elif opcion == "3":
            detalle_por_clientes(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio)
        elif opcion == "4":
            detalle_por_dia(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio, cant_dias)
        elif opcion == "5":
            detalle_actividades_por_dia(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio, cant_dias)
        elif opcion == "6":
            dia_con_mayor_ingresos(fechas_dia, fechas_mes, fechas_anio, ids_socio, indices_tipo_socio, indices_pase, mes, anio, cant_dias)
        elif opcion == "7":
            id_a_buscar = leer_entero("Ingrese el ID del socio (4 digitos entre 1000 y 9999): ", 1000, 9999)
            ver_actividades_socio(datos, id_a_buscar)
        elif opcion == "8":
            print("Saliendo del programa...")
        else:
            print("Opcion invalida. Intente nuevamente.")

mes = leer_entero("Ingrese el mes (1-12): ", 1, 12)
anio = leer_entero("Ingrese el anio: ", 1900, 2100)

cant_Dias = cant_dias_mes(mes, anio)
f_dia, f_mes, f_anio, id_s, ind_tipo_s, ind_pase, datos = generar_datos_aleatorios(mes, anio, cant_Dias)
menu_principal(f_dia, f_mes, f_anio, id_s, ind_tipo_s, ind_pase, mes, anio, cant_Dias)
