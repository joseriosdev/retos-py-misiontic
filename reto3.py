codigoCliente = [
       'Daniel', # arr[0] simpre es el nombre
       1, # arr[1] : 1 para afiliado, 2 para particular
       9, # arr[2]+arr[3]
       3, # arr[3]+arr[2] ESTA ES LA EDAD // 23 años
       1, # arr[4] tipo de servicio consumido 1,2,3
       3,
       2 # si la suma de los dos últimos digitos es par, 10% impar 20%
]

NOMBRE = codigoCliente[0] #const

#definiendo si es cliente o particular
if codigoCliente[1]==1 or codigoCliente[1]==2:
       if codigoCliente[1]==1:
              tipoCliente = 'Afiliado'
              AFILIADO = True
       else:
              tipoCliente = 'Particular'
              AFILIADO = False
else:
       tipoCliente = 'Registro no valido. Solo 1 o 2 por favor.'

EDAD = str(codigoCliente[2]) + str(codigoCliente[3]) #const

#Conociendo el servicio que utilizó
if codigoCliente[4]==1 or codigoCliente[4]==2 or codigoCliente[4]==3:
       if codigoCliente[4]==1:
              servicio = 'Deportes'
              cobro = 500000
       elif codigoCliente[4]==2:
              servicio = 'Artes y Música'
              cobro = 870000
       else:
              servicio = 'Gastronomía'
              cobro = 1230000
else:
       servicio = 'Registro no valido. Solo 1, 2 o 3 por favor.'

#DESCUENTO_BASICO
descuentoBasico = 10 if (codigoCliente[5]+codigoCliente[6])%2 == 0 else 20
#Aplicando descuentos %

descuentoAdicional = 0

#descuento por particular en rango de edad
if int(EDAD) > 30 and AFILIADO == False:
       descuentoAdicional = descuentoAdicional+10
else:
       print('El cliente {} no aplica a descuentos adicionales'.format(NOMBRE))

#descuento por edad
if int(EDAD) < 15:
       descuentoAdicional = descuentoAdicional+5
elif int(EDAD) > 50:
       descuentoAdicional = descuentoAdicional+25
else:
       print('El cliente {} no tiene descuento adicional porqué no es menor a 15 años o mayor de 50 años.'.format(NOMBRE))
       descuentoAdicional = descuentoAdicional+0

#TOTAL A PAGAR
descuentoTotal = descuentoAdicional + descuentoBasico
cobro = cobro-(cobro*descuentoTotal /100)

print('Nombre del Cliente: {}'.format(NOMBRE))
print('Tipo de Cliente: {}'.format(tipoCliente))
print('Edad del Cliente: {} años'.format(EDAD))
print('Servicio utilizado: {}'.format(servicio))
print('El % de descuento que tiene {} es: {}%'.format(NOMBRE, descuentoTotal))


print('Total a pagar: ${}'.format(cobro))

















