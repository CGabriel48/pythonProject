def calcular_descuento(monto_total, porcentaje_descuento=25):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def mostrar_resultados(monto_total, descuento):
    monto_final = monto_total - descuento
    print(f"Monto total de la compra: ${monto_total}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"Monto final a pagar después del descuento: ${monto_final}")


monto_compra_1 = 200
descuento_1 = calcular_descuento(monto_compra_1)
print("\nResultados de compra:")
mostrar_resultados(monto_compra_1, descuento_1)
monto_compra_2 = 300
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
print("\nResultados de compra:")
mostrar_resultados(monto_compra_2, descuento_2)

