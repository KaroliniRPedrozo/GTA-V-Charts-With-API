# 📊 Monitor de Jogadores GTA V (Steam)

Um projeto em Python que utiliza a API da Steam para coletar, armazenar e visualizar o número de jogadores online de Grand Theft Auto V ao longo do tempo.

Este projeto foi desenvolvido como um exercício prático de coleta de dados (API), armazenamento (SQLite) e visualização de dados (Matplotlib).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.14+**
* **Requests:** Para fazer chamadas à API da Steam.
* **Pandas:** Para carregar os dados do banco para a visualização.
* **Matplotlib:** Para plotar o gráfico de linha.
* **SQLite3:** Para armazenar os dados históricos coletados.

---

## 🚀 Como Funciona

O projeto é dividido em dois scripts principais:

1. **`coletor.py`**:
    * Este é o "robô" coletor.
    * Ele se conecta à API da Steam em intervalos regulares (a cada 10 minutos, por padrão).
    * Ele busca o número atual de jogadores online do GTA V (App ID: 271590).
    * Ele salva cada registro (data/hora e contagem de jogadores) em um banco de dados local `gta_players.db`.

2. **`grafico.py`**:
    * Este é o "visualizador".
    * Ele lê todos os dados armazenados no `gta_players.db`.
    * Ele usa o Pandas e o Matplotlib para gerar e exibir um gráfico de linha que mostra a flutuação de jogadores ao longo do tempo.

---

## 📈 Como Usar

Siga estes passos para rodar o projeto em sua máquina local.

### 1. Pré-requisitos

* Você precisa ter o [Python 3.10+](https://www.python.org/) instalado.
* Você precisa de uma **Chave da API da Steam** (gratuita): [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey)

### 2. Instalação

1. Clone este repositório (ou baixe o ZIP e extraia):

    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    ```

2. Navegue até a pasta do projeto:

    ```bash
    cd SEU-REPOSITORIO
    ```

3. Instale as bibliotecas necessárias:

    ```bash
    pip install -r requirements.txt
    ```

### 3. Configuração

1. Abra o arquivo `coletor.py` em um editor de texto.
2. Encontre a variável `SUA_CHAVE_API` no topo do arquivo.
3. Substitua o valor `"COLOQUE_SUA_CHAVE_API_AQUI"` pela sua chave da API da Steam.

### 4. Execução

Você precisará de dois terminais abertos na pasta do projeto.

**Terminal 1 (Para coletar os dados):**

Deixe este terminal rodando em segundo plano para construir seu banco de dados.

```bash
python coletor.py
```

**Terminal 2 (Para ver o gráfico):**

Depois de deixar o coletor rodar por um tempo (pelo menos 30-60 minutos), rode o script do gráfico:

```bash
python grafico.py
```

---

### 3. ⚠️ Dicas Essenciais para o GitHub

Antes de enviar seus arquivos (`git push`), faça estas três coisas:

#### 1. CRIE o `requirements.txt`

```bash
pip freeze > requirements.txt
```
(Se o pip não for reconhecido, use py -m pip freeze > requirements.txt) Isso criará o arquivo requirements.txt que o README menciona.
