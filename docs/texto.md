
Pressione Ctrl + Shift + V. --> O VS Code vai abrir uma aba ao lado mostrando o "resultado final" bonitão.

***
### ⚡ Performance: Python vs. MQL5

- **MQL5 (Nativo):** Execução em C++. Menor latência possível. Ideal para High Frequency Trading (HFT).
- **Python (Wrapper):** Existe um pequeno "atraso" (IPC - Inter-Process Communication) porque o Python precisa enviar o comando para o MT5 via biblioteca.
- **Veredito:** Para estratégias de médio/curto prazo (não HFT), a riqueza de bibliotecas do Python compensa a pequena perda de velocidade.

***
 # ANTES DE UMA PAUSA (FINALIZAR O DIA)

Para garantir que, quando você voltar, não perca tempo tentando lembrar "onde eu parei?".

Aqui está o seu Protocolo de Pausa Segura:  

1 Deixe um "Lembrete de Contexto"  
* Como você é o "professor" do seu próprio projeto, crie um arquivo simples chamado NOTAS.md ou apenas um comentário no topo do leitor_mercado.py:

  Python  
    - PAREI AQUI:  
     - Ambiente venv configurado e blindado.  
     - Conexão com .env e MT5 validada.  
     - Próximo passo: Criar o loop de monitoramento (while True).

2 Salve tudo (O óbvio)  
Certifique-se de que todos os arquivos no VS Code estão salvos (Ctrl + S). Se a bolinha branca no topo da aba sumiu, está salvo.  

3 O Ritual do Git (O envio real)  

👤 Identidade do Git

Sempre que configurar uma máquina nova, defina quem você é para o histórico do código:

- **Nome:** `git config --global user.name "Seu Nome"`. O nome que aparecerá ao lado dos seus "commits" (quem fez a alteração).  

- **E-mail:** `git config --global user.email "seu@email.com"`. O e-mail que liga suas alterações à sua conta do GitHub.

- **Verificar:** `git config --list` (Mostra se as configurações entraram).

Agora que os arquivos refletem exatamente o seu progresso, você faz os comandos:  

`git add .`  

`git commit -m "sua mensagem"`  

`git push`  


4 Feche o Ambiente de Forma Limpa. No terminal do VS Code, digite:  

`deactivate`

- Isso "sai" da venv e volta para o Python global do Windows. É uma boa prática para não deixar processos pendentes.  

5 O que fazer com o MetaTrader 5?  
Pode fechar o programa do MetaTrader 5 normalmente. Quando você voltar e rodar o script Python, o próprio código vai "chamar" o MT5 para abrir de novo, já que você configurou o login, password e server.

6 Quando você voltar, basta abrir o VS Code na pasta C:\robo e abrir o terminal e Digitar = `.\venv\Scripts\activate.`  

   E pronto, você estará exatamente onde parou.  


***
# ORGANIZAR O PROJETO

Para melhor organização do projeto, reorganizamos a instalação dos pacotes, passando de uma instalação global para uma instalação local. Isso garante que, futuramente, versões atualizadas de outros programas não interfiram nesta aplicação. Para isso, precisamos criar um ambiente virtual, que é a pasta venv, ou seja, um ecossistema autossuficiente.

1 - A venv (Virtual Environment) cria uma pasta dentro do seu projeto que contém uma cópia limpa do Python.  
Siga os esses passos para ter certeza que estará criando a pasta venv:  

   - No terminal e dentro da pasta do projeto digite:  
    * PS C:\robo> `python -m venv venv`  
    * PS C:\robo> `.\venv\Scripts\activate`  
    * (venv) PS C:\robo>   

        A indicação de `(venv)` significa que conseguimos configurar corretamente. A partir de agora, podemos fazer as instalações dos nosso pacote para este projeto. 

  ### 🛠️ Resumo Técnico: Ambiente Virtual (venv)

  O comando `python -m venv venv` é o pilar da **Arquitetura de Isolamento** em projetos Python.

  ### 🔍 Anatomia do Comando
  
  | Termo | Função Técnica | Descrição |
  | :--- | :--- | :--- |
  | **`python`** | Executável | Chama o interpretador instalado no Sistema Operacional. |
  | **`-m`** | Flag *Module* | Instrução para o Python executar um **módulo interno** como um script. |
  | **`venv` (1º)** | Módulo | A ferramenta oficial (Standard Library) que cria ambientes isolados. |
  | **`venv` (2º)** | Destino | O nome da **pasta local** que será criada (Convenção de mercado). |
   

  ### 💡 Conceitos de Engenharia de Software
  1. **Isolamento de Dependências:** Garante que as bibliotecas do robô (ex: `MetaTrader5`) não entrem em conflito com outros projetos no mesmo PC.
  2. **Imutabilidade Global:** O Python do Windows permanece "limpo". Se o ambiente do robô quebrar, basta apagar a pasta `venv` e recriar.
  3. **Portabilidade (Lista de Compras):** Não versionamos a pasta `venv` no Git. Usamos o arquivo `requirements.txt` para reconstruir o ambiente em qualquer máquina.

  ### 🚀 Ciclo de Vida (Cheat Sheet)
  - **Criar o ambiente:** `python -m venv venv`
  - **Ativar (Entrar no Laboratório):** `.\venv\Scripts\activate`
  - **Desativar (Sair do Laboratório):** `deactivate`
  - **Gerar Lista de Dependências:** `pip freeze > requirements.txt` 

***
# ARQUIVO 'REQUIREMENTS' - BAIXAR PACOTES AUTOMATICAMENTES

Despois de preparar nossa pasta 'venv' de configuração para cada projeto, vamos prepara um arquivo 'requirements' para baixar automaticamente todas as bibliotecas que o nosso projeto vai precisar para rodar.  
 - Digite no terminal: `pip freeze > requirements.txt`  

  Fazer isso sempre que baixar um novo pacote

***
# 📝 Guia de Instalação e Sincronização (Ambiente Novo)

Este guia serve para configurar o projeto `rb-cruza-medias` em qualquer computador novo (trabalho ou casa).

### 1. Ferramentas de Base
- **Git**: Instalar para clonar o projeto.
- **Python**: Instalar marcando a opção **"Add Python to PATH"**.

### 2. Clonar o Repositório
No terminal do VS Code, dentro da pasta onde os robôs ficarão:  

```
git clone https://github.com/SEU_USUARIO/rb-cruza-medias.git .

* Git Clone: Copia tudo da nuvem para o PC local.
```

### 3. Liberar o Sistema (Windows)
Permitir que o Windows execute o script da venv (executar apenas uma vez na máquina):

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

* Set-ExecutionPolicy: Muda a regra de segurança do Windows para aceitar scripts Python.
```


### 4. Criar o Ambiente Isolado (venv)
Criar a "caixa" onde as bibliotecas do robô serão instaladas:

```
python -m venv venv

* 🔧 Resumo Técnico
    - **Comando:** `python -m venv venv`
    - **python:** Chama o executor.
    - **-m:** Avisa que vou usar uma ferramenta interna (módulo).
    - **venv:** Ferramenta que cria o ambiente isolado.
    - **venv (final):** Nome da pasta que será criada no projeto.

    **Objetivo:** Criar uma "bolha" para o robô não entrar em conflito com outros programas do PC.  

```
### 5. Ativar o Ambiente
Entrar na bolha para começar a trabalhar (deve aparecer (venv) no terminal):
```
.\venv\Scripts\activate

* Activate: Liga o interruptor do ambiente virtual.
```

### 6. Instalar Dependências
Baixar as bibliotecas listadas no seu arquivo de requisitos:

```
pip install -r requirements.txt

* O comando `pip install -r requirements.txt` reconstrói o ambiente em qualquer máquina.

- `-r` (Requirements): Flag que indica que o próximo item é um arquivo de texto com a lista de pacotes e versões.

- `requirements.txt`: O arquivo "receita" que o Git salvou.
```

### **Dica de Engenheiro:**
Lembre-se que o arquivo `.env` (com suas senhas) não vem no `git clone`. Você precisa criá-lo manualmente agora para o robô conseguir conectar.

### **Fluxo de Engenharia:**
1. Você recebe o código do Git (sem a pasta `venv`).
2. Cria uma `venv` nova.
3. Roda o `pip install -r` para baixar tudo de uma vez.

Pronto! Em segundos, o Python baixa tudo de novo, mas agora configurado perfeitamente para esse novo computador.  

Moral da história: O código é o que você escreve. As bibliotecas são o que você requisita. O Git guarda apenas o que é seu código.



   
***
# ARQUIVO .gitignore  

3 - Não podemos esquecer do nosso arquvio .gitignore, para que não seja enviado para o github senhas e arquivos sigilosos

Bastar ter um arquivo com esse nome '.gitignore' na raiz do projeto, com as informações do que não dever ser enviado para o git remoto que o próprio git identifica que não é para usar o que está dentro dele.




***
# Robô de Monitoramento Multithread

### 1 -  Visão Geral  
O sistema foi redesenhado para separar a captação de dados da tomada de decisão. Em vez de um único fluxo linear, agora temos dois fluxos paralelos que se comunicam através de uma fila segura.

### 2 -  Componentes do Sistema  
O Vigia (Thread Produtora)

Função: Monitorar o ativo (ex: EURUSD) no MetaTrader 5 na maior velocidade permitida pelo hardware.

- Comportamento:
1. Roda em uma Thread separada (segundo plano).
2. Utiliza um loop de alta frequência (time.sleep(0.01)).
3. Filtragem de Ruído: Só envia dados para a fila se o preço atual (bid) for diferente do último preço registrado. Isso evita processamento desnecessário de dados repetidos.
4. Publicação: Coloca o novo preço na Queue (Fila).

#### A Fila (Queue - O Canal de Comunicação)

Função: Servir de ponte segura entre as Threads.

#### Por que usar queue.Queue?  
- No Python, as filas são thread-safe. Isso significa que o "Vigia", pode escrever e o "Estrategista", pode ler ao mesmo tempo sem que um atropele o dado do outro ou cause um crash no sistema (Race Condition).

- O Estrategista (Thread Principal / Consumidor)
Função: Processar os dados e aplicar a lógica de trading.

### Comportamento:

Utiliza o método `.get()`, que é um bloqueador eficiente. O processador não fica "gastando ciclo" enquanto a fila está vazia; ele entra em estado de espera e acorda instantaneamente quando um dado entra na fila.

* É aqui que, no futuro, colocaremos as condições: `if preco > media_movel: comprar()`.

### Benefícios da Arquitetura

1. Escalabilidade:  
 Podemos criar vários "Vigias" (um para cada par de moedas como GBPUSD, USDJPY) todos alimentando a mesma fila para um único "Estrategista".

2. Performance:  
 O programa não "engasga". Se o processamento de uma estratégia demorar 0.5s, o Vigia continua capturando os preços que mudaram nesse meio tempo e os coloca na fila para serem lidos logo em seguida.

3. Estabilidade:  
 O uso de `daemon=True` garante que, se você interromper o programa principal (Ctrl+C), todas as threads de apoio sejam encerradas automaticamente pelo sistema operacional.

### Glossário para o Engenheiro:
- `Thread`: Unidade básica de execução que compartilha o mesmo espaço de memória do processo pai.

- `Race Condition`: Problema que ocorre quando duas threads tentam modificar o mesmo dado ao mesmo tempo (evitado aqui pelo uso da Queue).

- `Daemon Thread`: Uma thread que roda em segundo plano e não impede o programa de encerrar.


***
# ESTRATÉGIA DE TESTE (MERCADO FECHADO)
### 🧪 Estratégias de Teste (Mercado Fechado)

1. **Mock (Simulação de Fluxo):** Criar uma função que substitui o MT5 e envia preços aleatórios para a `Queue`. Ideal para testar a **arquitetura** do código.
2. **Backtest (Dados Históricos):** Usar `mt5.copy_rates_from_pos` para baixar preços passados. Ideal para validar a **estratégia** matemática (médias, RSI, etc).
3. **Vantagem:** Permite desenvolver o robô 24/7, independente do horário da corretora.
