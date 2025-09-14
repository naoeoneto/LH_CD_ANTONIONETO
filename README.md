# Desafio Lighthouse - Indicium Tech

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/naoeoneto/LH_CD_ANTONIONETO/blob/main/notebooks/EDA_IMDB.ipynb)

Este repositório foi criado para o **Desafio Lighthouse**, da Indicium Tech.  
O objetivo é, a partir de uma base de dados de filmes do IMDb, realizar uma análise exploratória e desenvolver um modelo preditivo para estimar a nota do IMDb de um filme.

---

## ⚙️ Como rodar o projeto

Você pode rodar de duas formas:  

### ▶️ Abrir direto no Google Colab
Clique no badge acima ou [neste link](https://colab.research.google.com/drive/1pa4z_qTjtDvlhBCkKfrV07lHcX_AxQbV?usp=sharing) para abrir o notebook no Colab.  
Não é necessário instalar nada na sua máquina, apenas ter uma conta Google.  

### 💻 Rodar localmente

### 1. Criar e ativar ambiente virtual
```bash
python -m venv venv
```

### 2. Ative seu venv:

```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

### 3. Após ativado, instale o pacote listadas em requirements.txt:

```bash
pip install -r requirements.txt
```


### 4. Treinar e salvar o modelo
Execute o script abaixo para treinar e salvar o modelo.
O arquivo modelo.pkl será gerado dentro da pasta *model/*.
```bash
python model/save_model.py
```

### 5. Carregar e usar o modelo
Com o modelo já treinado, use o script abaixo para carregar o *.pkl* e realizar previsões:
```bash
python model/load_model.py
```

## Estrutura do projeto

*data/* → arquivos de dados originais (.csv).

*model/* → scripts de treino (save_model.py), predição (load_model.py) e modelo salvo (modelo.pkl).

*requirements.txt* → dependências do projeto.

*notebooks/* → notebooks de análise exploratória (EDA).

# Observação:
- Caso o arquivo com a base de dados seja mudado, seja o nome ou o local ou o arquivo completo, seu caminho deve ser ajustado dentro do arquivo *save_model.py*, na variável *file_path*, para que os resultados sejam visualiados corretamente.
- Certifique-se de que o Python 3.10+ esteja instalado para compatibilidade com as versões das bibliotecas.

# Desenvolvido por:

<table>
  <tbody style="display: flex;">
      <td align="center"><a href="https://github.com/naoeoneto"><img src="https://avatars.githubusercontent.com/u/106770927?v=4" width="100px;" alt="Antonio Neto"/><br /><sub><b>Antonio Neto</b></sub></a><br /><a href="https://github.com/naoeoneto/LH_CD_ANTONIONETO" title="Code">💻</a></td>
      <tr/>
    <tbody/>
<table/>