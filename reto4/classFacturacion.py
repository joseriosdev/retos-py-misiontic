import dataBase as DataBase

class Facturacion:

    def consultar(lista):
        print('Codigo----Descripcion----%IVA----Valor Unitario $')
        for i in lista:
            print('{} | {} | {} | {}'.format(i.codigo, i.descripcion, i.iva, i.valor))
    ##END OF CONSULTAR

    def generarFactura(lista):
        nombre = input('Nombre del cliente por favor: ')
        cxID = input('Cédula de ciudadanía por favor: ')
        factura = '001'

        subtotal = 0
        iva19 = 0
        iva10 = 0

        for i in lista:
            cant = int(input('Cuantos items vas a llevar de {}? '.format(i.cantidad)))
            i.cantidad = cant
            totalProducto = i.cantidad*i.valor
            subtotal = subtotal+totalProducto
            if i.iva == 19:
                iva19 = iva19 + (i.iva*i.valor /100)
            elif i.iva == 10:
                iva10 = iva10 + (i.iva*i.valor /100)
##END OF CLASS 'FACTURACION'

productosSeleccionados = [
    DataBase.dataBase[0],
    DataBase.dataBase[1],
    DataBase.dataBase[2],
    DataBase.dataBase[5]
]
