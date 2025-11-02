# 0_🏠_Bem_Vinda.py
"""Página principal da aplicação de alfabetização.

Esta é a página de "Home" que serve como ponto de entrada
e boas-vindas para o usuário.
"""

import streamlit as st

# Configuração da página (deve ser o primeiro comando Streamlit)
st.set_page_config(
    page_title="App de Alfabetização",
    page_icon="📚",
    layout="centered"
)

st.title("🌟 Bem-vinda ao App de Aprendizagem! 🌟")

# Personalização simples
# nome = st.text_input("Qual o seu nome, minha estrela?", "Exploradora")
nome = "Paulinha"

st.header(f"Olá, {nome}! Vamos aprender juntos?")

# Você pode trocar esta imagem por uma sua em assets/images/
st.image("assets/images/paulinha.jpg", width=300)

st.info(
    "Use o menu à esquerda (clique na setinha `>` no canto superior esquerdo) "
    "para escolher uma atividade legal!"
)

if st.button("Começar a Aventura! 🎉"):
    st.balloons()
