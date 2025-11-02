# pages/1_🅰️_Conhecendo_as_Letras.py
"""Página Módulo 1: Conhecendo as Letras.

Esta página permite ao usuário explorar as letras do alfabeto,
associando cada letra a uma palavra, imagem e som.
"""

import streamlit as st
import os
from core.audio_utils import generate_audio_mp3
from core.data_manager import LETTER_EXAMPLES

def main():
    """Função principal para renderizar a página do Módulo 1."""
    st.title("🅰️ Conhecendo as Letras e os Sons")
    st.write("Escolha uma letra para ver e ouvir o que ela representa!")

    # Seleciona a letra
    letras = list(LETTER_EXAMPLES.keys())
    letra_escolhida = st.selectbox("Selecione uma letra:", letras)

    if letra_escolhida:
        # Pega os dados do nosso "banco de dados" central
        data = LETTER_EXAMPLES[letra_escolhida]
        palavra = data["word"]
        emoji = data["emoji"]
        caminho_imagem = data["image"]

        # Mostra a letra e a palavra grande
        st.markdown(
            f"<h1 style='text-align: center; color: #FF4B4B;'>"
            f"{letra_escolhida}"
            f"</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h2 style='text-align: center;'>"
            f"é de... {palavra} {emoji}"
            f"</h2>",
            unsafe_allow_html=True
        )

        # Mostra a imagem (com verificação se o arquivo existe)
        if os.path.exists(caminho_imagem):
            st.image(caminho_imagem, use_column_width=True)
        else:
            st.warning(
                f"Imagem {caminho_imagem} não encontrada. "
                "Você já a adicionou na pasta 'assets/images'?"
            )

        st.divider()
        col1, col2 = st.columns(2)

        # Botão para ouvir o som da LETRA
        with col1:
            if st.button(f"Ouvir o som da letra '{letra_escolhida}'",
                         use_container_width=True):
                audio_bytes = generate_audio_mp3(letra_escolhida)
                if audio_bytes:
                    st.audio(audio_bytes, format='audio/mp3')

        # Botão para ouvir o som da PALAVRA
        with col2:
            if st.button(f"Ouvir a palavra '{palavra}'",
                         use_container_width=True):
                audio_bytes = generate_audio_mp3(palavra)
                if audio_bytes:
                    st.audio(audio_bytes, format='audio/mp3')

if __name__ == "__main__":
    main()
