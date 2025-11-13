import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates # Para formatar as datas no eixo

NOME_BANCO_DADOS = "gta_players.db" # Mesmo nome do outro script

def carregar_dados_do_banco():
    """Carrega os dados do banco SQLite para um DataFrame do Pandas."""
    try:
        conn = sqlite3.connect(NOME_BANCO_DADOS)
        
        # O 'parse_dates' já converte a coluna de texto para datas
        df = pd.read_sql_query(
            "SELECT timestamp, contagem_jogadores FROM jogadores_gta", 
            conn,
            parse_dates=['timestamp']
        )
        conn.close()
        
        if df.empty:
            print("O banco de dados está vazio. Deixe o 'coletor.py' rodar por um tempo.")
            return None
        return df
    except Exception as e:
        print(f"Erro ao ler o banco de dados: {e}")
        print("Certifique-se que o 'coletor.py' já rodou pelo menos uma vez.")
        return None

def plotar_grafico(df):
    """Cria e exibe o gráfico de linha."""
    if df is None:
        return

    df = df.set_index('timestamp') # Coloca as datas como o eixo principal

    plt.figure(figsize=(15, 7)) # Define um bom tamanho
    plt.plot(df.index, df['contagem_jogadores'], label='Jogadores Online', marker='o', markersize=2)
    
    # --- Formatação ---
    plt.title('Jogadores Online de GTA V (Coleta em Tempo Real)')
    plt.xlabel('Data e Hora')
    plt.ylabel('Número de Jogadores')
    plt.legend()
    plt.grid(True)
    
    # Formata o eixo X para exibir as datas de forma legível
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gcf().autofmt_xdate() # Inclina as datas

    plt.tight_layout()
    plt.show() # Abre a janela do gráfico

# --- Principal ---
if __name__ == "__main__":
    dados = carregar_dados_do_banco()
    plotar_grafico(dados)