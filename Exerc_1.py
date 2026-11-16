from pathlib import Path

pasta_atual = Path(__file__).parent
pasta_relatorios = pasta_atual / "Relatorios_Qualidade"
pasta_relatorios.mkdir(exist_ok=True)
caminho_arquivo = pasta_relatorios / "historico_inspecoes.txt"

lotes = [
    {"lote": 1001, "produto": "Caçarola 24", "inspecionadas": 1200, "rejeitadas": 18},
    {"lote": 1002, "produto": "Frigideira 28", "inspecionadas": 850, "rejeitadas": 25},
    {"lote": 1003, "produto": "Panela 20", "inspecionadas": 1500, "rejeitadas": 12},
    {"lote": 1004, "produto": "Caçarola 20", "inspecionadas": 900, "rejeitadas": 27}
]

def avaliar_lotes(lotes, arquivo):
    lotes_aprovados = 0
    lotes_reprovados = 0
    for lote in lotes:
        if lote["inspecionadas"] > 0:
            taxa_rejeicao = calcular_rejeicao(lote["inspecionadas"], lote["rejeitadas"])
            if taxa_rejeicao > 2:
                arquivo.write(f"Lote {lote['lote']} - Produto: {lote['produto']} - Taxa de rejeição: {taxa_rejeicao:.2f}% - REPROVADO\n")
                lotes_reprovados += 1
            else:
                arquivo.write(f"Lote {lote['lote']} - Produto: {lote['produto']} - Taxa de rejeição: {taxa_rejeicao:.2f}% - APROVADO\n")
                lotes_aprovados += 1
        else:
            arquivo.write("Erro: Número de unidades inspecionadas deve ser maior que zero.\n")

    arquivo.write(f"\nTotal de lotes aprovados: {lotes_aprovados}\n")
    arquivo.write(f"Total de lotes reprovados: {lotes_reprovados}\n")

def calcular_rejeicao(inspecionadas, rejeitadas):
    if inspecionadas > 0:
        return (rejeitadas / inspecionadas) * 100
    else:
        return None 

with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write("RELATÓRIO DE INSPEÇÕES DE QUALIDADE\n")
    arquivo.write("=" * 40 + "\n")
    avaliar_lotes(lotes, arquivo)

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
print(conteudo)