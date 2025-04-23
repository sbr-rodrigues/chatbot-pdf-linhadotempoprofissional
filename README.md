# Chatbot Inteligente para Análise de currículo

## Visão Geral - Projeto DIO - Chatbot Profissional 

Este projeto implementa um chatbot interativo capaz de responder a perguntas com base no conteúdo de arquivos PDF relevantes 
da minha trajetória profissional, integrada em um chatbot inovador. Ele oferece uma linha do tempo interativa com todas as minhas experiências, destacando as etapas mais importantes dos meus processos e conquistas ao longo da carreira. O objetivo é proporcionar uma visão clara e organizada das minhas competências e crescimento profissional A dificuldade em correlacionar informações dos currículos entre diversos vagas motivou a criação deste sistema de busca inteligente.

## Funcionalidades

* Carregamento de múltiplos arquivos PDF.
* Indexação do conteúdo dos PDFs através de embeddings.
* Busca vetorial para encontrar informações relevantes.
* Geração de respostas contextuais utilizando um modelo de linguagem da OpenAI.
* Interface de chat interativa no terminal.

## Tecnologias Utilizadas

* Python
* `pypdf`
* `langchain`
* `chromadb`
* `openai`

## Passo a Passo da Implementação

1.  **Preparação do Ambiente:** Criação do repositório no GitHub, configuração do ambiente virtual e instalação das dependências.
    ![Print da estrutura do repositório](screenshots/repo_structure.png)
    ![Print do ambiente virtual e dependências](screenshots/venv_dependencies.png)

2.  **Carregamento e Processamento dos PDFs:** Implementação do script `process_pdfs.py` para carregar, dividir e criar embeddings dos PDFs.
    ![Print da execução do process_pdfs.py](screenshots/process_pdfs_execution.png)

3.  **Criação do Chatbot Interativo:** Desenvolvimento do script `chatbot.py` para interagir com o usuário, buscar informações no banco de dados vetorial e gerar respostas.
    ![Print do chatbot em funcionamento](screenshots/chatbot_interaction.png)

## Insights e Aprendizados

Durante o desenvolvimento deste projeto, aprendi sobre a importância do processamento de texto para IA generativa, a utilidade dos embeddings para realizar buscas semânticas e o poder dos frameworks como o Langchain para simplificar a construção de aplicações de LLMs.

Um desafio interessante foi ajustar o tamanho dos chunks de texto para equilibrar a relevância da busca e o contexto para o modelo de linguagem. Experimentar com diferentes tamanhos de chunk e estratégias de divisão foi fundamental.

## Possibilidades de Melhoria

* Adicionar suporte a outros formatos de arquivo (e.g., DOCX, TXT).
* Implementar uma interface gráfica de usuário (GUI) ou uma interface web para o chat.
* Integrar um sistema de citações para referenciar as fontes das respostas.
* Otimizar a busca vetorial para maior precisão e velocidade.
* Explorar diferentes modelos de linguagem e embeddings para comparar resultados.

## Como Executar

1.  Clone este repositório: `git clone https://docs.github.com/articles/referencing-and-citing-content`
2.  Navegue até o diretório do projeto: `cd seu-repositorio`
3.  Crie um arquivo `.env` com sua chave da OpenAI:
    ```
    OPENAI_API_KEY=sua_chave_api_aqui
    ```
4.  Crie a pasta `inputs` e adicione seus arquivos PDF.
5.  Execute o script de processamento: `python process_pdfs.py`
6.  Execute o chatbot: `python chatbot.py`

## Contribuição

Sinta-se à vontade para contribuir com este projeto através de pull requests!

