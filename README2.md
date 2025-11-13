## Este README explica como configurar e executar os scripts de coleta e visualização de dados de jogadores da Steam.
---
## 📋 Pré-requisitos

Antes de começar, garanta que você tem:

1.  **Python 3.10+** instalado no seu computador.
2.  Uma **Chave da API da Steam**. (Você pode obter a sua em: `steamcommunity.com/dev/apikey`)

---

## ⚙️ 1. Instalação e Configuração

Siga estes passos na primeira vez que for rodar o projeto.

### Passo 1: Instalar as Dependências

Abra um terminal (Prompt de Comando ou o terminal do VS Code) na pasta deste projeto e instale as bibliotecas necessárias:

```bash
# Se você tiver o arquivo requirements.txt
pip install -r requirements.txt

# Ou, instale manualmente:
pip install pandas matplotlib requests
```
(Se o comando pip não for reconhecido, tente usar py -m pip install ...)

### Passo 2: Configurar a Chave da API

Este é o passo mais importante.

Abra o arquivo `coletor.py`.

Encontre a variável `SUA_CHAVE_API` no topo do arquivo.

Cole a sua chave da API da Steam dentro das aspas:
```
# Mude disto:
SUA_CHAVE_API = "COLOQUE_SUA_CHAVE_API_AQUI"

# Para isto (exemplo):
SUA_CHAVE_API = "A1B2C3D4E5F6A7B8C9D0..."
```

## 🚀 2. Como Executar o Projeto
Este projeto precisa de dois terminais rodando ao mesmo tempo: um para coletar os dados e outro para ver o gráfico.

**Terminal 1: O Coletor (Deixe rodando)**
Este script é o "robô" que salva os dados. Você precisa deixá-lo rodando em segundo plano.

No seu terminal, na pasta do projeto, execute:

```Bash
python coletor.py
(ou py coletor.py)
```
Você verá uma mensagem como `Iniciando coletor...` e depois `[data/hora] Salvo: XXXXX jogadores.`

Não feche este terminal! Apenas minimize-o.

**Terminal 2: O Gráfico (Rode quando quiser)**
Este script lê o banco de dados que o Coletor está criando e desenha o gráfico.

Espere alguns minutos (pelo menos 10-20 minutos) para que o `coletor.py` tenha tempo de salvar alguns dados.

Abra um NOVO terminal (pode ser no VS Code, clicando no `+`).

Neste novo terminal, execute:

```Bash
python grafico.py
(ou py grafico.py)
```
Uma janela com o gráfico de linha deve aparecer na sua tela!

## ⚠️ Solução de Problemas Comuns

Erro:`ModuleNotFoundError: No module named 'pandas'`

Solução: Você não instalou as dependências. Rode o comando `pip install pandas matplotlib requests` no terminal que você está usando.

Erro: `'python' não é reconhecido...`

Solução: O Python não foi adicionado ao PATH. Tente usar `py` em vez de python nos comandos (ex: `py coletor.py`).

Erro: O Gráfico Aparece Vazio:

Solução: Você não esperou o `coletor.py` salvar os dados. Deixe o coletor rodando por mais tempo e tente rodar o `grafico.py` novamente.
