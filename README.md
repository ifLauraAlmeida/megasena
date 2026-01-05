# 🎲 MegaSena Data Science Project

Projeto desenvolvido com o objetivo de **praticar e consolidar habilidades em Data Science**, utilizando dados históricos da Mega-Sena para análise, manipulação e comparação de apostas fictícias.

> ⚠️ Este projeto **não incentiva jogos de azar**.  
> Ele tem finalidade **educacional**, focada em **engenharia e análise de dados**.

<p align="center">
  <img src="banner.jpg" width="600">
</p>
<p align="center">
  [Tem mega da virada ou não?!]
</p>
---

## 🧠 Objetivos do Projeto

- Praticar **Python aplicado a dados**.
- Trabalhar com:
  - `pandas`;
  - `requests`;
  - coleta de dados via **API pública**.
- Organizar um projeto seguindo **boas práticas de mercado**.
- Separar claramente:
  - coleta;
  - processamento;
  - análise;
  - interação com usuário;
- Simular análises reais de **cruzamento de dados**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**;
- **pandas** — manipulação e análise de dados;
- **requests** — consumo de API;
- **tqdm** — barra de progresso;
- **Git/GitHub** — versionamento.

---

## 📦 Estrutura do Projeto

├── data
│ ├── raw
│ └── processed
│ └── megasena.csv
│
├── notebooks
│
├── src
│ ├── coleta
│ │ └── obter_dados.py
│ │
│ ├── processamento
│ │ └── limpar_dados.py
│ │
│ ├── analise
│ │ ├── comparar_aposta.py
│ │ ├── regras.py
│ │ └── executar_apostas.py
│ │
│ └── utils
│ └── salvar_csv.py
│
├── main.py
└── README.md


---

## 🔄 Pipeline de Dados

### 1️⃣ Coleta
- Os dados são coletados concurso por concurso através de uma **API pública da Mega-Sena**;
- Cada concurso é transformado em um DataFrame.

### 2️⃣ Processamento
- Limpeza e padronização dos dados;
- Estruturação em formato tabular adequado para análise.

### 3️⃣ Armazenamento
- Todos os concursos são unificados em um único DataFrame;
- Salvos em `data/processed/megasena.csv`.

### 4️⃣ Análise Interativa
- O usuário insere apostas fictícias (6 dezenas)
- O sistema compara a aposta com **todos os concursos históricos**
- Exibe:
  - quantidade de acertos;
  - concurso;
  - ano do sorteio.
- O usuário pode apostar **quantas vezes quiser**.

---

## ▶️ Como Executar o Projeto

### 1️⃣ Instale as dependências

-bash
pip install pandas requests tqdm

### 2️⃣ Gere o dataset

python main.py

Isso irá criar o arquivo:

data/processed/megasena.csv

### 3️⃣ Execute a análise interativa

python -m src.analise.executar_apostas

## 💡 Aprendizados

    Organização de projetos em Data Science;

    Separação de responsabilidades (ETL vs Análise);

    Manipulação eficiente de DataFrames;

    Uso de funções puras para regras de negócio;

    Construção de pipelines reutilizáveis.

## 🚀 Próximos Passos (Ideias)

    Otimizar performance eliminando iterrows;

    Criar análises estatísticas (frequência de dezenas);

    Visualizações com matplotlib ou seaborn;

    Criar uma API para consulta de apostas;

    Criar testes automatizados.

## 👩‍💻 Autoria

Por ifLauraAlmeida.
Projeto desenvolvido para fins educacionais e prática em Ciência de Dados e Engenharia de Dados.