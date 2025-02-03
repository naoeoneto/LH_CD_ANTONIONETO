# LH_CD_ANTONIONETO
O presente arquivo foi criado para o desafio Lighthouse, da Indicium Tech. Seu objetivo é, a partir de uma base de dados, fazer uma análise de previsão de informação solicitada.

---

## **Como rodar este projeto no seu computador?**  

Siga os passos abaixo para configurar o ambiente e executar os scripts corretamente.

### **1. Crie um ambiente virtual**  

```
python -m venv venv
```

### **2. Ative seu venv:**

```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

### **3. Após ativado, instale o pacote de bibliotecas listadas em requirements.txt:**

```shell
pip install -r requirements.txt
```

### **4. Executar a análise exploratória**
Caso queira rodar a análise exploratória de dados no Python diretamente, execute o seguinte comando:

```shell
python analytics/nome_do_arquivo.py
```

### **5. Executar a Análise Interativa no Jupyter Notebook**
Se preferir rodar o notebook interativamente, execute o seguinte comando para abrir o Jupyter Notebook:

```shell
jupyter notebook

```

Depois, navegue até a pasta *analytics/* e abra o arquivo *LH_CD_ANTONIONETO.ipynb.*
No Jupyter Notebook, clique em "Kernel" → "Restart & Run All" para rodar todas as células automaticamente e gerar os gráficos novamente.

Alternativamente, o notebook também pode ser aberto e executado no Google Colab.

### **6. Treinar e salvar o modelo**
Execute o script abaixo para treinar e salvar o modelo. Isso gerará o arquivo *modelo.pkl* dentro da pasta *model/*.

```shell
python model/save_model.py
```

### **7. Carregar o modelo e fazer previsões**
Caso o arquivo *modelo.pkl* já tenha sido gerado, você pode utilizar o script abaixo para carregá-lo e fazer previsões.

```shell
python model/load_model.py
```

# Observação importante:
Caso o arquivo com a base de dados seja alterado (seja o nome, local ou estrutura), o caminho do arquivo deve ser atualizado dentro do script *save_model.py*.
Isso deve ser feito na variável *file_path* para garantir que o modelo seja treinado corretamente e os resultados possam ser visualizados sem erros.

# Desenvolvido por:

<table>
  <tbody style="display: flex;">
      <td align="center"><a href="https://github.com/naoeoneto"><img src="https://avatars.githubusercontent.com/u/106770927?v=4" width="100px;" alt="Antonio Neto"/><br /><sub><b>Antonio Neto</b></sub></a><br /><a href="https://github.com/naoeoneto/LH_CD_ANTONIONETO" title="Code">💻</a></td>
      <tr/>
    <tbody/>
<table/>