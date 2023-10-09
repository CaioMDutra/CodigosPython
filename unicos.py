estados = [
    ["SP", "MG", "GO"],
    ["ES", "PA", "MG"],
    ["RJ", "BA", "SC"],
    ["SC", "RS", "PA"],
    ["RS", "MG", "SP"]
]

unicos = set()

for uf in estados:
    for estado in uf:
        unicos.add(estado)

valores_unicos = unicos

print(valores_unicos)