import sqlite3
import pandas as pd
import plotly.express as px  # Trocamos matplotlib por plotly

NOME_BANCO_DADOS = "gta_players.db" # Mesmo nome do outro script

def carregar_dados_do_banco():
    """Carrega os dados do banco SQLite para um DataFrame do Pandas."""
    try:
        conn = sqlite3.connect(NOME_BANCO_DADOS)
        df = pd.read_sql_query(
            "SELECT timestamp, contagem_jogadores FROM jogadores_gta", 
            conn,
            parse_dates=['timestamp'] # O pandas já converte para data
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
    """Cria e exibe o gráfico interativo com Plotly."""
    if df is None:
        return

    print("Gerando gráfico interativo com Plotly...")

    # --- Cria o Gráfico Interativo ---
    fig = px.line(
        df,
        x='timestamp', # A coluna de data que já temos
        y='contagem_jogadores',
        title='Jogadores Online de GTA V (Coleta em Tempo Real)',
        labels={'timestamp': 'Data', 'contagem_jogadores': 'Jogadores Online'},
        color_discrete_sequence=['#2CA02C'], # Sua linha verde
        markers=True # Adiciona os pontos de referência
    )

    # --- Aplica o Modo Escuro ---
    fig.update_layout(
        template='plotly_dark',
        xaxis_title="Data e Hora",
        yaxis_title="Número de Jogadores"
    )

    # === Adiciona os Botões de Filtro ===
    fig.update_xaxes(
        rangeselector=dict(
            buttons=list([
                dict(count=30, label="30 dias", step="day", stepmode="backward"),
                dict(count=3, label="3 meses", step="month", stepmode="backward"),
                dict(count=6, label="6 meses", step="month", stepmode="backward"),
                # --- LINHAS CORRIGIDAS ABAIXO ---
                dict(count=1, label="1 ano", step="year", stepmode="backward"),
                dict(count=3, label="3 anos", step="year", stepmode="backward"),
                dict(count=6, label="6 anos", step="year", stepmode="backward"),
                dict(label="Tudo", step="all") # Botão para ver tudo
            ]),
            bgcolor="#333", # Cor de fundo dos botões (para o modo escuro)
            activecolor="#555" # Cor do botão ativo
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date" # Diz ao eixo X que ele é do tipo "data"
    )

    # Abre o gráfico no seu navegador
    fig.show()
    print("Gráfico pronto. Verifique seu navegador!")

# --- Principal ---
if __name__ == "__main__":
    dados = carregar_dados_do_banco()
    plotar_grafico(dados)
