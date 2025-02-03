# LH_CD_ANTONIONETO
O presente arquivo foi criado para o desafio Lighthouse, da Indicium Tech. Seu objetivo é, a partir de uma base de dados, fazer uma análise de previsão de informação solicitada.

**Para rodar esse projeto em seu computador, é necessário seguir os seguintes passos:**

1. Crie um ambiente virtual

```
python -m venv venv
```

2. Ative seu venv:

```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Após ativado, instale o pacote listadas em requirements.txt:

```shell
pip install -r requirements.txt
```

4. Para rodar a análise exploratória de dados no Python, basta rodar 


4. Execute o script *save_model.py* para treinar e salvar o modelo. Isso gerará o arquivo modelo.pkl na pasta *model*.

```shell
python model/save_model.py
```

5. Após o arquivo *modelo.pkl* ter sido gerado (caso não tenha sido gerado anteriormente), você pode usar o script *load_model.py* para carregar o modelo e fazer previsões.
```shell
python model/load_model.py
```

# Observação:
Caso o arquivo com a base de dados seja mudado, seja o nome ou o local ou o arquivo completo, seu caminho deve ser ajustado dentro do arquivo *save_model.py*, na variável *file_path*, para que os resultados sejam visualiados corretamente.

# Desenvolvido por:

<table>
  <tbody style="display: flex;">
      <td align="center"><a href="https://github.com/naoeoneto"><img src="https://avatars.githubusercontent.com/u/106770927?v=4" width="100px;" alt="Antonio Neto"/><br /><sub><b>Antonio Neto</b></sub></a><br /><a href="https://github.com/naoeoneto/LH_CD_ANTONIONETO" title="Code">💻</a></td>
      <tr/>
    <tbody/>
<table/>