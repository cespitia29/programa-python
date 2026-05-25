# =====================================================================
# Problema 3: Sistema de Auditoría de Inventario y Reabastecimiento
# Curso: Fundamentos de Programación
# =====================================================================

# MÓDULO (FUNCIÓN): Determina la cantidad exacta a pedir para un artículo
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Aplica la lógica de negocio para calcular el reabastecimiento.
    Si el stock actual es menor al mínimo, retorna la diferencia.
    De lo contrario, retorna cero.
    """
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        cantidad_a_pedir = 0
        
    return cantidad_a_pedir


# ESTRUCTURA DE DATOS: Matriz con 5 artículos de inventario
# Formato: [Código, Nombre, Stock Actual, Stock Mínimo Requerido]
inventario_matriz = [
    ["ART01", "Teclado Mecanico", 12, 20],
    ["ART02", "Mouse Optico",      35, 30],
    ["ART03", "Monitor 24 Pulg",    4, 10],
    ["ART04", "Auriculares Gamer", 15, 15],
    ["ART05", "Cable HDMI 2m",      8, 25]
]


# PROCESAMIENTO Y SALIDA: Reporte de auditoría y pedidos
print("-" * 50)
print("        REPORTE DE AUDITORÍA DE INVENTARIO")
print("-" * 50)
print(f"{'ARTÍCULO':<25} | {'CANTIDAD A PEDIR':<15}")
print("-" * 50)

# Recorremos la matriz fila por fila
for articulo in inventario_matriz:
    # Extraemos los datos basándonos en sus posiciones en la fila
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    # Llamamos al módulo para procesar la lógica de negocio
    pedido_exacto = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    
    # Imprimimos la lista de pedidos solicitada
    print(f"{nombre:<25} | {pedido_exacto:<15}")

print("-" * 50)