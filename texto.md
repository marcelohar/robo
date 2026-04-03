
Pressione Ctrl + Shift + V. --> O VS Code vai abrir uma aba ao lado mostrando o "resultado final" bonitão.


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

   * Fazer isso sempre que baixar um novo pacote


   
***
# ARQUIVO .gitignore  

3 - Não podemos esquecer do nosso arquvio .gitignore, para que não seja enviado para o github senhas e arquivos sigilosos

Bastar ter um arquivo com esse nome '.gitignore' na raiz do projeto, com as informações do que não dever ser enviado para o git remoto que o próprio git identifica que não é para usar o que está dentro dele.

***
# JUNTANDO TUDO

Depois de tudo configurado, vamos guardar no repositorio git remoto, somente os codigo e se precisar dos arquivo de configuracao e pacotes baixados basta:  

"Recupera" tudo em outro PC. O fluxo de um engenheiro sênior é este:  

- Você faz o git clone do seu projeto em um PC novo.  

- Você verá que a pasta venv não está lá (graças ao .gitignore).  

- Você cria uma venv nova e limpa: No terminal: `python -m venv venv.`  

- Você diz ao Python: "Leia a lista de compras e instale tudo":  

  `pip install -r requirements.txt`  

O comando `pip install -r requirements.txt` reconstrói o ambiente em qualquer máquina.

- **`-r` (Requirements):** Flag que indica que o próximo item é um arquivo de texto com a lista de pacotes e versões.
- **`requirements.txt`:** O arquivo "receita" que o Git salvou.



**Fluxo de Engenharia:**
1. Você recebe o código do Git (sem a pasta `venv`).
2. Cria uma `venv` nova.
3. Roda o `pip install -r` para baixar tudo de uma vez.

Pronto! Em segundos, o Python baixa tudo de novo, mas agora configurado perfeitamente para esse novo computador.  

Moral da história: O código é o que você escreve. As bibliotecas são o que você requisita. O Git guarda apenas o que é seu código.


***
# ESTRUTURA ATUAL

A estrutura até agora:  
C:/robo/   
├── venv/               (Pasta de bibliotecas - IGNORADA pelo Git)  
├── .env                (Suas senhas - IGNORADO pelo Git)  
├── .gitignore          (Regras de proteção - NA RAIZ)  
├── requirements.txt    (Lista de dependências - NO GIT)  
├── leitor_mercado.py   (Seu código principal)  
└── temporarioTeste.py  (Seu código de testes)  
 



