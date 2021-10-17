class Producto:
    def __init__(self, codigo, descrip, cant, iva, valor, valorCompleto):
        self.codigo = codigo
        self.descripcion = descrip
        self.cantidad = cant
        self.iva = iva
        self.valor = valor
        self.valorCompleto = valorCompleto


dataBase = [
    Producto(77073, 'Pañal Patico x 30und Etapa 1', 1, 19, 19000),
    Producto(77072, 'Azúcar x Kg', 1, 10, 3000),
    Producto(77123, 'Leche x litro', 1, 0, 2500),
    Producto(77085, 'Cerveza aguila sixpack', 1, 19, 11000),
    Producto(77088, 'Alpin', 1, 19, 2000),
    Producto(77185, 'Caldo de costilla', 1, 10, 6000),
    Producto(77195, 'Jabon', 1, 19, 68000),
    Producto(77285, 'Cepillo de dientes', 1, 19, 10000),
    Producto(77385, 'Rascador de gatitos', 1, 19, 5000),
    Producto(77455, 'Cereal de la abuela', 1, 0, 1000)
]

