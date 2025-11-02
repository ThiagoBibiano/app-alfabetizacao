# 📚 App de Alfabetização com Streamlit

Este é um aplicativo web interativo, construído com Streamlit e Python, projetado para auxiliar minha filha no processo de alfabetização. A aplicação segue uma jornada de aprendizagem progressiva, começando pelo reconhecimento de letras e sons, passando pela formação de sílabas, até a construção e escrita de frases completas.

## 🚀 Jornada de Aprendizagem (Módulos)

O app é dividido em 6 módulos principais, cada um focado em uma etapa do aprendizado:

1.  **🅰️ Conhecendo as Letras:** Associa letras aos seus sons (fonemas) e a uma palavra/imagem de exemplo.
2.  **🔡 Formando Sílabas:** Ferramenta interativa para combinar consoantes e vogais, ouvindo o som da sílaba formada.
3.  **🧩 Complete a Palavra:** Jogo onde a criança vê uma imagem (ex: CASA) e a palavra incompleta (CA ___) e deve escolher a sílaba correta.
4.  **🖼️ O que é isso?:** Jogo de escrita. A criança vê uma imagem e deve escrever o nome do objeto em um campo de texto.
5.  **✍️ Organize a Frase:** Jogo de lógica onde a criança recebe "peças" de uma frase fora de ordem e deve clicar nelas na sequência correta.
6.  **🗣️ Ditado de Frases:** A criança ouve uma frase falada pelo app e deve escrevê-la corretamente.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Streamlit:** Para a criação rápida da interface web interativa.
* **gTTS (Google Text-to-Speech):** Para a geração dinâmica dos áudios de letras, sílabas, palavras e frases em português do Brasil.

---

## ⚙️ Como Instalar e Rodar o Projeto

Siga os passos abaixo para executar o projeto em sua máquina local.

### 1. Pré-requisitos

* Ter o [Python 3.13+](https://www.python.org/downloads/) instalado.
* Ter o [Git](https://git-scm.com/downloads) instalado (para clonar o repositório).

### 2. Clonar o Repositório

Abra seu terminal e clone este repositório:

```bash
git clone [https://github.com/ThiagoBibiano/app-alfabetizacao.git]
cd app-alfabetizacao
````

### 3\. Criar um Ambiente Virtual (Recomendado)

É uma boa prática isolar as dependências do projeto:

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

### 4\. Instalar as Dependências

Com o ambiente ativado, instale todas as bibliotecas necessárias que estão listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5\. Rodar a Aplicação

Finalmente, execute o arquivo principal do Streamlit:

```bash
streamlit run 0_🏠_Bem_Vinda.py
```

O Streamlit irá abrir automaticamente uma aba no seu navegador. A aplicação estará pronta para usar\!
