# entrada
patente = input("Ingrese la patente (sin espacios y caracteres especiales): ")
patente = patente.upper()

print("Clase de vehículo:\n 0: Motocicleta \n 1: Carro \n 2: camión")
clas_vehiculo = int(input("De las opciones anteriores, indicar que clase de vehículo es: "))

print("Método de pago:\n 0: manual \n 1: telepeaje")
form_pago = int(input("Indique de las opciones anteriores de que manera va a abonar el servicio: "))

print("País procedente: \n 0: Argentina \n 1: Bolivia \n 2: Brasil \n 3: Paraguay \n 4: Uruguay")
pais_cab_peaje = int(input("Ingrese de las opciones anteriores en qué país está atravesada la cabina del peaje: "))

distancia = float(input("Ingrese la distancia recorrida desde la ultima cabina de peaje (si ésta es la primera, indique con un 0): "))

# proceso
# -----------------------------------------------------------------------------------------------------------------#
# ejercicio 1
# -----------------------------------------------------------------------------------------------------------------#
if len(patente) == 7: # Define si pertenece o no al mercosur
    mercosur = "pertenece al mercosur"
else:
    mercosur = "no pertenece al mercosur"
    
    # País al cual pertenece la patente
if patente[0:2].isalpha() and patente[2:5].isnumeric() and patente[5:7].isalpha():
    pais = "Argentina"
elif patente[0:2].isalpha() and patente[2:7].isnumeric():
    pais = "Bolivia"
elif patente[0:3].isalpha() and patente[4].isalpha() and patente[3].isnumeric() and patente[5:7].isnumeric():
    pais = "Brasil"
elif patente[0:4].isalpha() and patente[4:7].isnumeric():
    pais = "Paraguay"
elif patente[0:3].isalpha() and patente[3:7].isnumeric():
    pais = "Uruguay"
else:
    pais= "otro país"

# -----------------------------------------------------------------------------------------------------------------#
# Ejercicio 2
# -----------------------------------------------------------------------------------------------------------------#

if pais_cab_peaje == 0: 
    valor_fijo = 300
elif pais_cab_peaje == 1:
    valor_fijo = 200
    if clas_vehiculo == 0:
        clas_vehiculo = "motocicleta"
        dto = valor_fijo * 50 // 100
        valor_total = valor_fijo - dto
    elif clas_vehiculo == 2:
        clas_vehiculo = "camión"
        dto = valor_fijo * 60 // 100  
elif pais_cab_peaje == 2:
    valor_fijo = 400
    if clas_vehiculo == 0:
        clas_vehiculo = "motocicleta"
        dto = valor_fijo * 50 // 100
        valor_total = valor_fijo - dto
        
    elif clas_vehiculo == 2:
        clas_vehiculo = "camión"
        dto = valor_fijo * 60 // 100
        valor_total = valor_fijo - dto
elif pais_cab_peaje == 3:
    valor_fijo = 300
    if clas_vehiculo == 0:
        clas_vehiculo = "motocicleta"
        dto = valor_fijo * 50 // 100
    elif clas_vehiculo == 2:
        clas_vehiculo = "camión"
        dto = valor_fijo * 60 // 100 
        valor_total = valor_fijo - dto
else:
    valor_fijo = 300
    if clas_vehiculo == 0:
        clas_vehiculo = "motocicleta"
        dto = valor_fijo * 50 // 100
        valor_total = valor_fijo - dto
    elif clas_vehiculo == 2:
        clas_vehiculo = "camión"
        dto = valor_fijo * 60 // 100  
        valor_total = valor_fijo - dto

# -----------------------------------------------------------------------------------------------------------------#
# Ejercicio 3
# -----------------------------------------------------------------------------------------------------------------#

desc = 0
if form_pago == 1:
   desc = valor_fijo * 0.90

# -----------------------------------------------------------------------------------------------------------------#
# Ejercicio 4
# -----------------------------------------------------------------------------------------------------------------#

if desc != 0:
    valor_prom = round(desc / distancia)
else:
    valor_prom = round(valor_fijo / distancia)


# salida
# 1
if len(patente) == 7:
    print("La patente pertenece al mercosur y es procedente de: ", pais)
else:
    print("La patente no pertenece al mercosur")
# 2
print("El valor de la etiqueta es: ", valor_fijo, ", ya que su vehículo es de tipo: ", clas_vehiculo, ", tiene un descuento que le modificará y le quedará un total de: ", valor_total)
# 3
if form_pago == 1:
    print("debido a su pago mediante telepeaje se le hizo un descuento del 10% quedando: ", desc)
else:
    print(("su pago fue manual, quedando un total de: ", valor_fijo))
   
# 4
if distancia == 0:
    print("la distancia es 0")
else:
    print("el valor promedio pagado por ese vehículo por cada kilómetro recorrido desde la última cabina es de: ", valor_prom)
