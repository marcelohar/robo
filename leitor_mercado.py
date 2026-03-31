import  MetaTrader5 as mt5
import  pandas as pd
import  os                           #ponte de comunicação direta com o Sistema Operacional (Windows, Linux ou Mac)
from    dotenv import load_dotenv


# Carrega o arquivo .env
load_dotenv()

# Pegar os dados do .env e converter para o tipo ceto

login_mt5 =     int(os.getenv("MT5_LOGIN"))
senha_mt5 =     os.getenv("MT5_PASSWORD")
servidor_mt5 =  os.getenv("MT5_SERVER")


# 1. Ligando o motor: O python se conecta ao MetaTrader 5
if not mt5.initialize(login = login_mt5, password = senha_mt5, server = servidor_mt5):
    print(f"X Falha ao conectar com o MetaTrader 5: {mt5.last_error()}")

    
    mt5.shutdown()  # 5. Desligando o motor
    quit()          # Encerrar
else:
    print("$ Conectado com sucesso usando os dados do .env!")

# 2. Escolhendo o "produto": Vamos olhar para o Euro x Dólar (EURUSD)
ativo = "EURUSD" 

# 3. Pedindo a cotação: "Ei MT5, me dê a informação exata de agora desse ativo!"
info_ativo = mt5.symbol_info(ativo)

# 4. Verificando se deu certo e mostrando o resultado
if info_ativo is not None:
    # O f avisa: "Ei, Python, fique atento! Tudo o que estiver entre { } aqui dentro não é texto, é o nome de uma variável. Pegue o valor dela e coloque no lugar."
    # Se você quiser imprimir um número com apenas 2 casas decimais (muito comum em preços de Forex), você pode fazer assim dentro da f-string: print(f"O preço atual é {preco:.2f}")
    print(f"--- DADOS DO {ativo} ---")
    print(f"Preço de Compra (Ask): {info_ativo.ask}")
    print(f"Preço de Venda (Bid): {info_ativo.bid}")
else:
    print(f"X Não consegui achar o ativo {ativo}. Verifique se o MetaTrader está aberto e logado na conta demo!")


# 5. Desligando o motor
mt5.shutdown() 