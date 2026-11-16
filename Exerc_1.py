lotes = [
    {"lote": 1001, "produto": "Caçarola 24", "inspecionadas": 1200, "rejeitadas": 18},
    {"lote": 1002, "produto": "Frigideira 28", "inspecionadas": 850, "rejeitadas": 25},
    {"lote": 1003, "produto": "Panela 20", "inspecionadas": 1500, "rejeitadas": 12},
    {"lote": 1004, "produto": "Caçarola 20", "inspecionadas": 900, "rejeitadas": 27}
]

def avaliar_lotes(lotes):
    lotes_aprovados = 0
    lotes_reprovados = 0
    for lote in lotes:
        if lote["inspecionadas"] > 0:
            taxa_rejeicao = calcular_rejeicao(lote["inspecionadas"], lote["rejeitadas"])
            if taxa_rejeicao > 2:
                print(f"Lote {lote['lote']} - Produto: {lote['produto']} - Taxa de rejeição: {taxa_rejeicao:.2f}% - REPROVADO")
                lotes_reprovados += 1
            else:
                print(f"Lote {lote['lote']} - Produto: {lote['produto']} - Taxa de rejeição: {taxa_rejeicao:.2f}% - APROVADO")
                lotes_aprovados += 1
        else:
            print("Erro: Número de unidades inspecionadas deve ser maior que zero.")

    print(f"\nTotal de lotes aprovados: {lotes_aprovados}")
    print(f"Total de lotes reprovados: {lotes_reprovados}")

def calcular_rejeicao(inspecionadas, rejeitadas):
    if inspecionadas > 0:
        return (rejeitadas / inspecionadas) * 100
    else:
        return None 

avaliar_lotes(lotes)
