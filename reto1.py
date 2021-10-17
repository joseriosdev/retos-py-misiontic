resultadosProductoNuevo = {
    'lunes':{'unidadesVendidas': 20, 'precioUnidad': 3500},
    'martes':{'unidadesVendidas': 23, 'precioUnidad': 3400},
    'miercoles':{'unidadesVendidas': 15, 'precioUnidad': 3800},
    'jueves':{'unidadesVendidas': 32, 'precioUnidad': 3200},
    'viernes':{'unidadesVendidas': 31, 'precioUnidad': 3100},
    'sabado':{'unidadesVendidas': 8, 'precioUnidad': 4000}
}


def unidadesVendidasPorSemana(objProducto):
    resultado = 0
    for dia in objProducto:
        resultado = resultado + objProducto[dia]['unidadesVendidas']

    return resultado

def ventaBruta(objProducto):
    resultado = 0
    for dia in objProducto:
        resultado = resultado + (objProducto[dia]['precioUnidad']*objProducto[dia]['unidadesVendidas'])

    return resultado


# Suma de productos vendidos en la semana
weeklySales = unidadesVendidasPorSemana(resultadosProductoNuevo)
print('Productos vendidos en la semana: ' + str(weeklySales))
# Ventas Bruta -> dinero que ingresa
allSales = ventaBruta(resultadosProductoNuevo)
print('Venta total: ' + str(allSales))
# Ganancias reales (10%)
profit = allSales*0.1
print('Ganancias: ' + str(profit))
