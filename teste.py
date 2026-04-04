# teste.py

import MetaTrader5 as mt5
import pandas as pd
import os
from dotenv import load_dotenv

######################################################################################
# 1. INICIALIZAÇÃO E SEGURANÇA
######################################################################################

# Carrega as variáveis de ambiente do arquivo .env (protege suas senhas)
load_dotenv()

# Captura as credenciais e converte o login para inteiro (exigência do MT5)
login_mt5 = int(os.getenv("MT5_LOGIN"))
senha_mt5 = os.getenv("MT5_PASSWORD")
servidor_mt5 = os.getenv("MT5_SERVER")

# Tenta estabelecer a ponte entre o Python e o terminal MetaTrader 5 aberto
if not mt5.initialize(login = login_mt5, password = senha_mt5, server = servidor_mt5):
    # Se falhar, exibe o código do erro oficial da MetaQuotes
    print(f"X Falha ao conectar com o MetaTrader 5 'teste.py': {mt5.last_error()}")
    quit() # Encerra o script imediatamente
          

######################################################################################
# 2. CAPTURA DE DADOS HISTÓRICOS (BACKTESTING)
######################################################################################

symbol    = "EURUSD"           # Ativo que queremos analisar
timeframe = mt5.TIMEFRAME_H1   # Tempo gráfico: H1 significa que cada "vela" (candle) vale 1 hora
start_pos = 0                  # 0 indica que queremos começar a contar a partir de AGORA (a vela atual)
count     = 500                # Quantidade de velas para trás que o Python vai buscar (neste caso, 500 horas)

# Função que busca os dados no servidor da corretora e traz como um "array" de dados brutos
rates = mt5.copy_rates_from_pos(symbol, timeframe, start_pos, count)

# Validação: verifica se os dados realmente chegaram (evita erros se o ativo estiver escrito errado)
if rates is None or len(rates) == 0:
    print("X Erro: Não foi possível baixar os dados. Verifique o nome do ativo.")
    mt5.shutdown() # Desliga a conexão com o MT5 antes de sair
    quit()


######################################################################################
# 3. TRATAMENTO E ORGANIZAÇÃO DOS DADOS (PANDAS)
######################################################################################

# Converte o "pacote de dados brutos" (rates) em uma tabela estruturada (DataFrame)
# A tabela terá colunas como: time, open, high, low, close, tick_volume, etc.
df = pd.DataFrame(rates)

# O MT5 envia a hora em "Unix Timestamp" (segundos desde 1970). 
# Aqui convertemos esses segundos em uma data/hora legível (Human Readable).
df['time'] = pd.to_datetime(df['time'], unit='s')


######################################################################################
# 4. SIMULAÇÃO DO ROBÔ (A "VIAGEM NO TEMPO")
######################################################################################

# Percorremos a tabela linha por linha, do passado para o presente
# len(df) nos diz quantas linhas (velas) temos no total (serão 500)
for i in range(len(df)):
    
    # .iloc[i] acessa a linha específica da posição 'i'
    # 'close' é o preço de fechamento daquela hora específica
    preco_fechamento = df['close'].iloc[i]
    horario          = df['time'].iloc[i]

    # ESPAÇO PARA LÓGICA:
    # É aqui que você insere as regras matemáticas. 
    # Exemplo: "Se o preço de fechamento for maior que o anterior, imagine uma compra."

    # Exibe no terminal o resultado da simulação para cada hora processada
    print(f"Testando vela de {horario}: Preço foi de {preco_fechamento}")