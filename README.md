# Data Science 📊

Repositório de estudos para **revisar estudos de Data Science com Python do básico ao avançado**, com exemplos práticos em Jupyter Notebook.

O estudo começa pelos fundamentos da linguagem Python e pelas bibliotecas de manipulação de dados (**NumPy** e **pandas**). Depois vêm a **estatística descritiva**, a **visualização** e a **análise exploratória (EDA)**. A trilha termina na **estatística inferencial** (testes de hipótese), em **séries temporais** e em **Machine Learning não supervisionado**.

---

## 📚 Sumário

- [Proposta do projeto](#-proposta-do-projeto)
- [Etapas de uma análise de dados](#-etapas-de-uma-análise-de-dados)
- [Trilha de estudos](#-trilha-de-estudos)
  - [Nível 1 — Básico](#nível-1--básico-fundamentos-e-manipulação-de-dados)
  - [Nível 2 — Intermediário](#nível-2--intermediário-estatística-descritiva-e-visualização)
  - [Nível 3 — Avançado](#nível-3--avançado-inferência-séries-temporais-e-machine-learning)
- [Estrutura do repositório](#-estrutura-do-repositório)
- [Como executar](#-como-executar)
- [Glossário rápido](#-glossário-rápido)
- [Referências](#-referências)

---

## 🎯 Proposta do projeto

Este repositório é um **caderno de revisão** de análise de dados. Cada notebook trata de um tema, com exemplos curtos e comentados, para ser fácil de consultar depois.

### O que significa "do básico ao avançado"?

O conteúdo segue uma ordem em que cada etapa usa o que foi aprendido na anterior:

1. **Básico: carregar e organizar dados.** Conhecer o Python usado em ciência de dados (bibliotecas, funções, estruturas de dados), trabalhar com arrays no **NumPy** e com tabelas (DataFrames) no **pandas**: ler arquivos CSV, selecionar colunas, filtrar linhas, tratar valores nulos e remover registros.
2. **Intermediário: descrever e visualizar dados.** Resumir os dados com **estatística descritiva** (média, mediana, moda, quartis, variância, desvio padrão), identificar os tipos de variáveis (qualitativas e quantitativas) e criar gráficos (histograma, boxplot, dispersão, escalas logarítmicas) para fazer a **análise exploratória** de uma base real.
3. **Avançado: tirar conclusões e encontrar padrões.** Usar **estatística inferencial** para testar hipóteses a partir de uma amostra, analisar **séries temporais** (tendência, sazonalidade, estacionariedade, médias móveis, suavização LOESS) e aplicar **Machine Learning não supervisionado** para agrupar dados (K-Means), reduzir dimensões (PCA) e detectar anomalias (Isolation Forest).

Há também um exemplo de **SQL dentro do Python** com o SQLite, ligando a análise de dados aos bancos de dados relacionais.

---

## 🔄 Etapas de uma análise de dados

Os notebooks seguem, na prática, o fluxo de trabalho de uma análise:

```
Coleta → Limpeza/Tratamento → Análise Exploratória → Visualização → Inferência/Modelagem → Conclusões
```

| Etapa | O que envolve | Ferramentas |
|-------|---------------|-------------|
| **Coleta** | Ler dados de arquivos, URLs, bancos de dados ou do Kaggle | `pandas`, `sqlite3`, `kagglehub` |
| **Limpeza/Tratamento** | Tratar nulos, duplicados, tipos de dados e filtros | `pandas` |
| **Análise Exploratória (EDA)** | Entender a distribuição e a relação entre variáveis | `pandas`, `numpy` |
| **Visualização** | Comunicar padrões com gráficos | `matplotlib`, `seaborn` |
| **Inferência/Modelagem** | Testar hipóteses, modelar séries e aplicar ML | `scipy`, `statsmodels`, `scikit-learn` |

> 💡 A **estatística descritiva** *resume* os dados que você tem (ex.: a média salarial da amostra). A **estatística inferencial** usa uma amostra para *tirar conclusões sobre a população* (ex.: "a altura média da população é diferente de 1,70 m?").
>
> 💡 No **aprendizado supervisionado** o modelo aprende com dados rotulados (já se sabe a resposta). No **aprendizado não supervisionado**, que é o caso deste repositório, o modelo encontra padrões e grupos sozinho, sem rótulos.

---

## 🧭 Trilha de estudos

### Nível 1 — Básico (fundamentos e manipulação de dados)

| Conceito | Descrição | Arquivo |
|----------|-----------|---------|
| Python para Data Science | Instalar e importar bibliotecas, funções built-in, criar funções e estruturas de dados | [python_ds_intro.ipynb](Notebooks/python_ds_intro.ipynb) |
| NumPy | Criar e manipular arrays, carregar dados com `np.loadtxt` | [numpy_curso1.ipynb](Notebooks/numpy_curso1.ipynb) |
| pandas | Importar dados, explorar a base, tratar nulos, remover registros e aplicar filtros | [pandas_alura_1.ipynb](Notebooks/pandas_alura_1.ipynb) |
| SQL com Python | Criar tabelas, inserir e consultar dados com `sqlite3` | [sqlite_python.ipynb](Notebooks/sqlite_python.ipynb) |

```python
import pandas as pd

df = pd.read_csv("Arquivos/dados.csv")
df.head()                      # primeiras linhas
df[df["Idade"] > 30]           # filtro de linhas
df["Renda"].mean()             # média de uma coluna
```

### Nível 2 — Intermediário (estatística descritiva e visualização)

| Conceito | Descrição | Arquivo |
|----------|-----------|---------|
| Estatística descritiva | Tipos de variáveis, distribuição de frequências, medidas de tendência central e de dispersão (base PNAD 2015) | [curso-estatistica-python.ipynb](Notebooks/curso-estatistica-python.ipynb) |
| Quartis | Calcular Q1, Q2 (mediana) e Q3 com `np.percentile` e `np.quantile` | [quartil-numpy.py](Notebooks/quartil-numpy.py) |
| Gráficos de dispersão | Scatter plot simples, por grupos, com tamanho/cor e linha de regressão | [scatter_plot.ipynb](Notebooks/scatter_plot.ipynb) |
| Escala logarítmica | Visualizar crescimento exponencial com eixo em log | [log_plot.ipynb](Notebooks/log_plot.ipynb) |
| Escala semi-log e log-log | Identificar leis de potência e relações exponenciais | [semi_logplot.ipynb](Notebooks/semi_logplot.ipynb) |
| Análise exploratória completa | EDA de custos de seguro saúde: distribuições, boxplots, outliers e correlações | [medical_cost_personal.ipynb](Notebooks/medical_cost_personal.ipynb) |

### Nível 3 — Avançado (inferência, séries temporais e machine learning)

| Conceito | Descrição | Arquivo |
|----------|-----------|---------|
| Teste de hipótese | Teste t para comparar a média de uma amostra com um valor de referência | [teste_hipotese.ipynb](Notebooks/teste_hipotese.ipynb) |
| Séries temporais | Tendência, sazonalidade, decomposição, teste de Dickey-Fuller (estacionariedade), ACF e PACF | [series-temporais.ipynb](Notebooks/series-temporais.ipynb) |
| Médias móveis | Suavizar oscilações com `rolling().mean()` | [medias_moveis.ipynb](Notebooks/medias_moveis.ipynb) |
| LOESS | Suavização por regressão local para destacar a tendência | [loess.ipynb](Notebooks/loess.ipynb) |
| ML não supervisionado | Agrupamento (K-Means), redução de dimensionalidade (PCA) e detecção de anomalias (Isolation Forest) | [ML_algoritmos_n_sup.ipynb](Notebooks/ML_algoritmos_n_sup.ipynb) |

**Média móvel, exemplo:**

```python
df["media_movel_3d"] = df["vendas"].rolling(window=3).mean()
```

**K-Means, exemplo:**

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(dados_padronizados)
```

### 🚧 Próximos tópicos (roadmap)

- [ ] Intervalos de confiança e outros testes (qui-quadrado, ANOVA)
- [ ] Regressão linear e logística
- [ ] Aprendizado supervisionado (árvores de decisão, Random Forest)
- [ ] Previsão de séries temporais (ARIMA, Prophet)
- [ ] Dashboards interativos (Plotly, Streamlit)

---

## 📁 Estrutura do repositório

```
An-lise-de-Dados-/
├── README.md
├── Arquivos/
│   └── dados.csv                       # Amostra da PNAD 2015 (UF, Sexo, Idade, Cor, Anos de Estudo, Renda, Altura)
└── Notebooks/
    ├── python_ds_intro.ipynb           # Python para Data Science
    ├── numpy_curso1.ipynb              # NumPy
    ├── pandas_alura_1.ipynb            # pandas: exploração, nulos, filtros
    ├── sqlite_python.ipynb             # SQL com sqlite3
    ├── curso-estatistica-python.ipynb  # Estatística descritiva
    ├── quartil-numpy.py                # Quartis com NumPy
    ├── scatter_plot.ipynb              # Gráficos de dispersão
    ├── log_plot.ipynb                  # Escala logarítmica
    ├── semi_logplot.ipynb              # Escalas semi-log e log-log
    ├── medical_cost_personal.ipynb     # EDA de custos médicos (Kaggle)
    ├── teste_hipotese.ipynb            # Teste de hipótese
    ├── series-temporais.ipynb          # Séries temporais
    ├── medias_moveis.ipynb             # Médias móveis
    ├── loess.ipynb                     # Suavização LOESS
    └── ML_algoritmos_n_sup.ipynb       # K-Means, PCA, Isolation Forest
```

---

## ▶️ Como executar

### Pré-requisitos

- [Python 3](https://www.python.org/)
- [Jupyter Notebook](https://jupyter.org/), [VS Code](https://code.visualstudio.com/) com a extensão Jupyter, ou [Google Colab](https://colab.research.google.com/)

### 1. Clonar o repositório

```sh
git clone https://github.com/gustavocoderjs/An-lise-de-Dados-.git
cd An-lise-de-Dados-
```

### 2. Instalar as dependências

```sh
pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn kagglehub jupyter
```

### 3. Abrir os notebooks

```sh
jupyter notebook Notebooks/
```

> ⚠️ Alguns notebooks baixam dados da internet (GitHub e Kaggle), então é preciso estar conectado. O [medical_cost_personal.ipynb](Notebooks/medical_cost_personal.ipynb) usa o `kagglehub`, que pode pedir login no Kaggle.

---

## 📖 Glossário rápido

| Termo | Significado |
|-------|-------------|
| **DataFrame** | Tabela do pandas, com linhas e colunas nomeadas |
| **EDA** | *Exploratory Data Analysis*: análise exploratória para entender os dados antes de modelar |
| **Quartis** | Valores que dividem os dados ordenados em 4 partes iguais (Q1, Q2 = mediana, Q3) |
| **Outlier** | Valor muito distante dos demais, geralmente visível no boxplot |
| **Correlação** | Mede o quanto duas variáveis variam juntas (de -1 a 1) |
| **Teste de hipótese** | Procedimento para decidir, com base em uma amostra, se uma afirmação sobre a população é plausível |
| **p-valor** | Probabilidade de obter o resultado observado se a hipótese nula for verdadeira |
| **Série temporal** | Dados registrados em sequência ao longo do tempo |
| **Estacionariedade** | Quando média e variância de uma série não mudam com o tempo |
| **Média móvel** | Média calculada sobre uma "janela" que desliza pelos dados |
| **Clusterização** | Agrupar dados semelhantes sem rótulos prévios (ex.: K-Means) |
| **PCA** | *Principal Component Analysis*: reduz o número de variáveis mantendo a maior parte da informação |

---

## 🔗 Referências

- [Documentação pandas](https://pandas.pydata.org/docs/)
- [Documentação NumPy](https://numpy.org/doc/)
- [Documentação Matplotlib](https://matplotlib.org/stable/)
- [Documentação Seaborn](https://seaborn.pydata.org/)
- [Documentação SciPy](https://docs.scipy.org/doc/scipy/)
- [Documentação statsmodels](https://www.statsmodels.org/)
- [Documentação scikit-learn](https://scikit-learn.org/stable/)

---

📌 *Repositório em constante evolução, acompanhando o avanço nos estudos de análise de dados.*
