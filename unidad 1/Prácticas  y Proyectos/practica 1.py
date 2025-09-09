 # practica diagnostico_superheroes.py

productos = ["Figura Iron Man", "Figura Spider-Man", "Figura Capitán América"]
precios = [350, 400, 500]

# Función para calcular el total 
def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

# Menú usuario
print("Bienvenido a la tienda de figuras de superhéroes")
nombre = input("Ingresa tu nombre: ")

cantidades = []
print("\nSelecciona tus figuras (ingresa la cantidad de cada una):\n")
for i in range(len(productos)):
    print(f"[{i}] {productos[i]} - ${precios[i]}")
    cantidad = int(input(f"Cantidad de {productos[i]}: "))
    cantidades.append(cantidad)

# Calcular total
total = calcular_total(cantidades, precios)

# Aplicar descuento (10% si el total es mayor a $1000)
descuento = 0
if total > 1000:
    descuento = total * 0.10

total_final = total - descuento

# Ticket
print("\n------ TICKET DE COMPRA ------")
print(f"Cliente: {nombre}\n")

print("Figuras compradas:")
for i in range(len(productos)):
    if cantidades[i] > 0:
        subtotal = cantidades[i] * precios[i]
        print(f"{cantidades[i]} x {productos[i]} - ${subtotal}")

print(f"\nSubtotal: ${total}")
print(f"Descuento: ${descuento}")
print(f"TOTAL A PAGAR: ${total_final}")
print("------------------------------")
