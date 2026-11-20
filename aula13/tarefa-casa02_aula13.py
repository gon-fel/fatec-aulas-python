import math
# Bloco 1: Entrada de dados
volume = float(input("Digite o volume do recipiente em m³: "))
altura = float(input("Digite a altura do recipiente em metros: "))

# 2. Bloco 2: Cálculos do raio e da área total
raio = math.sqrt(volume / (math.pi * altura))

# 3. Bloco 3: Cálculo da área total 
area_total = math.pow(raio, 2) * math.pi + 2 * math.pi * raio * altura

# 4. Bloco 4: Cálculo da quantidade de galões 
galoes = math.ceil(area_total / 18)

# 5. Bloco 5: Cálculo do custo total
preco_galao = 145.75

custo_total = round(galoes * preco_galao, 2)

# 6. Bloco 6: Saída de dados
print(f"\n --- RESUMO DO ORÇAMENTO ---")
print(f"Raio do recipiente: {raio:.2f} metros")
print(f"Área total: {area_total:.2f} m²")
print(f"Quantidade de galões necessários: {galoes}")
print(f"Custo total: R$ {custo_total:.2f}")