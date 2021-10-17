SMLV = 877802 #Const

class Empleado:
    def __init__(self, nombre, edad, escolaridad, genero, salario = SMLV, porcentaje = 0):
        self.nombre = nombre
        self.edad = edad
        self.escolaridad = escolaridad
        self.genero = genero
        self.salario = salario * self.escolaridad
#End of Class 'Empleado'


empleados = {
    '001': Empleado('Juan Esteban Aristizabal', 37,1,'M'),
    '002': Empleado('Miriam Herminda Díaz', 31,2,'F'),
    '003': Empleado('Adriana Maecha', 30,3,'F'),
    '004': Empleado('Sansa Stark', 70,1,'F'),
    '005': Empleado('Loras Tyrell', 19,2,'M'),
    '006': Empleado('Homero Simpson', 26,3,'M'),
    '007': Empleado('Dany Targaryen', 43,3,'F'),
    '008': Empleado('Jon Snow', 88,4,'M'),
    '009': Empleado('Rihanna Eminem', 76,3,'F'),
    '010': Empleado('Valenti San Juan', 58,3,'M'),
    '011': Empleado('Marco Bucci', 46,4,'M'),
    '012': Empleado('Marcos Raya', 23,3,'M'),
    '013': Empleado('Naruto Uzumaki', 25,4,'M'),
    '014': Empleado('Hinata Hiuga', 18,3,'F'),
    '015': Empleado('Lupiita Molano', 99,3,'F')
}

##El total de dinero que la empresa Universidad de Pamplona gasta en su
##nómina de empleados
def presupuestoEmpleados(obj):
    result = 0
    for i in obj:
        result = result + obj[i].salario

    return str(result)

##Calcular del porcentaje de dinero que le corresponde a cada empleado del
##monto total.
def porcentaje(obj):
    montoTotal = int(presupuestoEmpleados(obj))
    for i in obj:
        porcentaje = (obj[i].salario / montoTotal) *100
        obj[i].porcentaje = porcentaje
        print('El % que ocupa {} del presupuesto para docentes es {:.2f}'.format(obj[i].nombre, obj[i].porcentaje))


##Guardar los datos de los 15 empleados en una lista e imprimirlos en pantalla,
##usar la función sort o sorted para ordenar los nombres en orden alfabético.
def orderAlfabetico(obj):
    arr = []
    for i in obj:
        arr.append(obj[i].nombre)

    return sorted(arr)

##Guardar los ingresos de cada empleado en una lista e imprimir en orden
##ascendente usando la función anterior.
def obtenerIngresos(obj):
    arr = []
    for i in obj:
        arr.append(obj[i].salario)

    return sorted(arr)



def obtenerEdades(obj):
    arr = []
    for i in obj:
        arr.append(obj[i].edad)

    return sorted(arr)


#Changing some variables so I can print them
INGRESOS_EMPLEADOS = obtenerIngresos(empleados)
EDAD_EMPLEADOS = obtenerEdades(empleados)

ascendente = INGRESOS_EMPLEADOS

mayorSalario = max(INGRESOS_EMPLEADOS)
menorSalario = min(INGRESOS_EMPLEADOS)
viejo = max(EDAD_EMPLEADOS)
jovencito = min(EDAD_EMPLEADOS)


#Printing all the results...
print('U.Pamplona INVIERTE en sus empleados: ' + presupuestoEmpleados(empleados))
porcentaje(empleados)
print('Los empleados en orden alfabetico: {}'.format(orderAlfabetico(empleados)))
print('Lista de salarios en orden ascendente')
print(ascendente)
print('Salario max {}. Salario min {}'.format(mayorSalario, menorSalario))
print('Edad max {}. Edad min {}'.format(viejo, jovencito))
