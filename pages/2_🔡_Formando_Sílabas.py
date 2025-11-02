# pages/2_🔡_Formando_Sílabas.py
"""Página Módulo 2: Formando Sílabas.

Esta página é uma ferramenta interativa para a criança combinar
consoantes e vogais para formar e ouvir sílabas.
"""

import streamlit as st
from core.audio_utils import generate_audio_mp3
from core.data_manager import SYLLABLE_CONSONANTS, SYLLABLE_VOWELS

def main():
    """Função principal para renderizar a página do Módulo 2."""
    st.title("🔡 Vamos Formar Sílabas com Som!")
    st.write("Escolha uma consoante e uma vogal para ver a mágica acontecer.")

    col1, col2 = st.columns(2)

    # Coluna das Consoantes
    with col1:
        st.header("Consoantes")
        # Usamos st.radio para seleção única
        consoante = st.radio(
            "Escolha uma consoante:",
            SYLLABLE_CONSONANTS,
            label_visibility="collapsed"
        )

    # Coluna das Vogais
    with col2:
        st.header("Vogais")
        vogal = st.radio(
            "Escolha uma vogal:",
            SYLLABLE_VOWELS,
            label_visibility="collapsed"
        )

    st.divider()

    # --- Resultado e Geração de Áudio ---
    silaba_formada = consoante + vogal

    # Mostra a sílaba bem grande
    st.markdown(
        f"<h1 style='text-align: center; color: #FF4B4B;'>"
        f"{silaba_formada}"
        f"</h1>",
        unsafe_allow_html=True
    )

    # Gera e exibe o player de áudio para a sílaba
    # O áudio é gerado a cada seleção de botão
    audio_bytes = generate_audio_mp3(silaba_formada)
    if audio_bytes:
        st.audio(audio_bytes, format='audio/mp3')

    # Botão de reforço positivo
    if st.button("Adorei formar esta sílaba! 🎉", width=300):
        st.balloons()
        st.success(f"EBA! Parabéns por formar a sílaba '{silaba_formada}'!")

if __name__ == "__main__":
    main()
