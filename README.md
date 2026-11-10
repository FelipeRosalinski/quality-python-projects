
# Quality Python Projects

Projetos de automação e processamento de dados desenvolvidos em Python, com foco na otimização de processos, organização de informações e melhoria da eficiência operacional.

## 📌 Sobre o projeto

Este repositório reúne projetos práticos desenvolvidos durante meus estudos em Python, integrando conhecimentos de **Qualidade Industrial, Análise de Dados e Automação de Processos**.

O objetivo é desenvolver soluções que reduzam atividades manuais, aumentem a confiabilidade das informações e contribuam para a padronização de processos.

## 🛠️ Tecnologias utilizadas

- **Python** — Linguagem principal de programação.
- **Pandas** — Manipulação e processamento de dados.
- **Pathlib** — Gerenciamento de caminhos, arquivos e diretórios.
- **OpenPyXL** — Leitura e gravação de arquivos Excel `.xlsx`.
- **Git e GitHub** — Controle de versão e gerenciamento do código-fonte.

## 📂 Projeto 1 — Automação de Planilhas Excel

**Arquivo:** `consolidar_planilhas.py`

### 🎯 Objetivo

Automatizar a separação e consolidação de informações armazenadas em planilhas Excel, reduzindo a necessidade de manipulação manual dos arquivos.

### ⚙️ Funcionalidades

- Criação de planilhas Excel a partir de dados estruturados.
- Organização de informações em diferentes abas.
- Separação automática das abas em arquivos individuais.
- Criação de diretórios para armazenamento dos arquivos.
- Leitura automática das planilhas separadas.
- Consolidação das informações em um único arquivo Excel.
- Identificação dinâmica das abas a partir dos nomes dos arquivos.

### ▶️ Como executar

**1. Clone o repositório:**

```bash
git clone https://github.com/FelipeRosalinski/quality-python-projects.git
```

**2. Acesse a pasta do projeto:**

```bash
cd quality-python-projects
```

**3. Instale as dependências:**

```bash
pip install pandas openpyxl
```

**4. Execute o programa:**

```bash
python consolidar_planilhas.py
```

**5. Confira os arquivos gerados:**

O programa deverá criar as pastas:

```text
quality-python-projects/
├── consolidar_planilhas.py
├── README.md
├── .gitignore
├── vendas_por_estado.xlsx
├── Planilhas_Separadas/
│   ├── vendas_PR.xlsx
│   ├── vendas_SC.xlsx
│   └── vendas_RS.xlsx
└── Planilhas_Consolidadas/
    └── vendas_consolidadas.xlsx
```

> **Nota:** O projeto utiliza dados fictícios para fins educacionais.

## 📊 Aplicações práticas

As técnicas utilizadas neste projeto podem ser adaptadas para:

- Consolidação de relatórios de inspeção.
- Organização de indicadores de qualidade.
- Processamento de dados de fornecedores.
- Automatização de relatórios operacionais.
- Padronização de arquivos e informações.

## 🚀 Desenvolvimento profissional

Este repositório faz parte do meu processo de desenvolvimento técnico em **Tecnologia da Informação**, com foco em:

- Python
- QA Automation
- Testes de Software
- Análise de Dados
- Automação de Processos

Novos projetos serão incorporados conforme a evolução dos estudos.

## 👨‍💻 Autor

**Felipe Rosalinski**

Profissional com experiência em Gestão da Qualidade Industrial, em desenvolvimento de competências em programação, automação e Engenharia de Qualidade de Software.

[LinkedIn](https://www.linkedin.com/in/felipe-rosalinski/) | [GitHub](https://github.com/FelipeRosalinski)