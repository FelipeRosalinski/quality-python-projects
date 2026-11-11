import pandas as pd
from pathlib import Path

pasta_atual = Path(__file__).parent.absolute()
pasta_organizados = pasta_atual / "Planilhas_Separadas"
pasta_organizados.mkdir(exist_ok=True)
pasta_consolidadas = pasta_atual / "Planilhas_Consolidadas"
pasta_consolidadas.mkdir(exist_ok=True)
    
dados_pr = {
    "Cliente": ["Cliente A", "Cliente B"],
    "Vendas": [1500, 2200]
}

dados_sc = {
    "Cliente": ["Cliente C", "Cliente D"],
    "Vendas": [1800, 3100]
}

dados_rs = {
    "Cliente": ["Cliente E", "Cliente F"],
    "Vendas": [2500, 1900]
}

df1 = pd.DataFrame(dados_pr)
df2 = pd.DataFrame(dados_sc)
df3 = pd.DataFrame(dados_rs)

with pd.ExcelWriter("vendas_por_estado.xlsx") as writer:
    df1.to_excel(writer, sheet_name="PR", index=False)
    df2.to_excel(writer, sheet_name="SC", index=False)
    df3.to_excel(writer, sheet_name="RS", index=False)

tabelas = pd.read_excel("vendas_por_estado.xlsx", sheet_name=None)

for estado, tabela in tabelas.items():
    tabela.to_excel(pasta_organizados / f"vendas_{estado}.xlsx", index=False)

def consolidar_planilhas(caminho_separadas):
    with pd.ExcelWriter(pasta_consolidadas / "vendas_consolidadas.xlsx") as writer:
        for planilhas in caminho_separadas.glob("vendas_*.xlsx"):
            df = pd.read_excel(planilhas)
            estado = planilhas.stem.split("_")[-1]
            df.to_excel(writer, sheet_name=estado, index=False)

consolidar_planilhas(pasta_organizados)

print("Consolidação de planilhas concluída com sucesso!")
