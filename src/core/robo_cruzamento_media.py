# robo_cruzamento_medias.py
import  MetaTrader5 as mt5
import  pandas      as pd
import  os                              #ponte de comunicação direta com o Sistema Operacional (Windows, Linux ou Mac)
import  time
import  threading

from    queue       import Queue
from    dotenv      import load_dotenv
from    src.services.vigia_EURUSD_thread import vigia


######################################################################################
# Carrega o arquivo .env
load_dotenv()

# Pegar os dados do .env e converter para o tipo ceto
login_mt5       = int(os.getenv("MT5_LOGIN"))
senha_mt5       = os.getenv("MT5_PASSWORD")
servidor_mt5    = os.getenv("MT5_SERVER")


######################################################################################
# Ligando o motor: O python se conecta ao MetaTrader 5

if not mt5.initialize(login = login_mt5, password = senha_mt5, server = servidor_mt5):
    print(f"X   Falha ao conectar com o MetaTrader 5: {mt5.last_error()}")    
    mt5.shutdown()  # 5. Desligando o motor
    quit()          # Encerrar
else:
    print("\n$  Conectado com sucesso usando os dados do .env!")

######################################################################################
# Criando a fila para os novos preços
fila_de_precos  = Queue()   # Buffer de segurança para garantir que nenhum tick de preço seja perdido.

######################################################################################
# Escolhendo o "produto": Vamos olhar para o Euro x Dólar (EURUSD)
ativo = "EURUSD" 


######################################################################################
# DISPARA O VIGIA (Que está no outro arquivo)
# O target agora aponta para a função importada
t = threading.Thread(target = vigia, args = (ativo, fila_de_precos), daemon = True)
t.start()   # inicia a linha de produção (threading)

print(f"\n$ Robô ligado! Aguardando o valor do {ativo}...")

# LOOP DO ESTRATEGISTA (Processamento do robo -) (Onde a mágica acontece)
try:
    while True:
        # O .get() trava aqui até o vigia colocar um preço na fila
        preco_atual = fila_de_precos.get()

        hora = time.strftime('%H:%M:%S')
        print(f"[{hora}] ESTRATEGISTA: Recebi o preço do ativo: {preco_atual}")

        # No futuro, as médias móveis entram aqui!

except KeyboardInterrupt:
    print("\nEncerrando processos...")

    # 5. Desligando o motor
    mt5.shutdown()
