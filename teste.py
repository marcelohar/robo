# import os
# from dotenv import load_dotenv
# import MetaTrader5 as mt5

# load_dotenv()

# print("--- Verificação de Ambiente ---")
# print(f"Senha do .env carregada? {'Sim' if os.getenv('MT5_PASSWORD') else 'Não'}")
# print(f"Pasta venv ativa? {'Sim' if 'venv' in os.environ.get('VIRTUAL_ENV', '') else 'Não'}")

# if not mt5.initialize():
#     print("Falha ao iniciar MT5")
# else:
#     print("Conectado ao MetaTrader 5 com sucesso!")
#     mt5.shutdown()