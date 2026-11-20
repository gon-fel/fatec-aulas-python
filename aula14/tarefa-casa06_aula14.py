import math

print("\n--- ORÇAMENTO DE PISOS ---")

comodo = ""
total_caixas = 0
area_total = 0

while comodo != "N":
    comodo = input("\nDeseja cadastrar um cômodo? [S]im [N]ão: ").upper()

    if comodo == "S":
        comprimento = float(input("Informe o comprimento do comôdo em metros: "))
        largura = float(input("Informe a largura do cômodo em metros: "))

        area = comprimento * largura
        area_total += area
        caixas_comodo = math.ceil(area / 2.5)
        total_caixas += caixas_comodo

print(f"\n ---Orçamento dos Pisos---")
print(f"A area total é de: {area_total:.2f}m².")
print(f"Para revestir a obra serão necessários: {total_caixas} de pisos.")
print(f"Sendo divididas em 3 entregas.")

for entrega in range (1, 4):
    entrega_caixas = math.ceil(total_caixas / 3)
   

    print(f"Entrega {entrega}: {entrega_caixas} caixas de pisos.")
