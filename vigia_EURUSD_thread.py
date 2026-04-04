# vigia_EURUSD_thread.py

import  MetaTrader5 as mt5
import  os
import  time
import  threading
from    queue import Queue
from    dotenv import load_dotenv


######################################################################################
# Carregando os dados de acesso e realizando o login

load_dotenv()
login_mt5       = int(os.getenv("MT5_LOGIN"))
senha_mt5       = os.getenv("MT5_PASSWORD")
servidor_mt5    = os.getenv("MT5_SERVER")

if not mt5.initialize(login=login_mt5, password=senha_mt5, server=servidor_mt5):
    print(f"X Erro ao iniciar o mt5: cod. {mt5.last_error()}")
    quit()

######################################################################################

def vigia(nome_ativo, caixa):
    ultimo_bid = 0
    print(f"Vigia iniciado para o ativo: {nome_ativo}")

    while True:
        tick = mt5.symbol_info_tick(nome_ativo)

        if tick is not None:
            # Só avisa se o preço mudar
            if tick.bid != ultimo_bid:
                # Joga o novo preço na caixa/fila (queue)
                caixa.put(tick.bid) 
                ultimo_bid = tick.bid

        time.sleep(0.01) # Descanso minúsculo para não travar o pc










