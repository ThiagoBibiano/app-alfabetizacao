# pages/6_🗣️_Ditado_de_Frases.py
"""Página Módulo 6: Jogo de Ditado de Frases.

O usuário ouve uma frase e deve escrevê-la corretamente
em um campo de texto.
"""

import streamlit as st
import os
from core.game_logic import initialize_game_state, get_new_challenge, check_user_answer
from core.audio_utils import generate_audio_mp3
from core.data_manager import DICTATION_CHALLENGES

# Chave única para este jogo no session_state
GAME_KEY = "dictation"


def main():
    """Função principal para renderizar a página do Módulo 6."""
    st.title("🗣️ Ditado de Frases")

    # --- 1. Inicialização do Estado ---
    # Usando a lógica de jogo PADRÃO (a mesma dos módulos 3 e 4)
    initialize_game_state(GAME_KEY, DICTATION_CHALLENGES)

    # --- 2. Lógica de Carregamento do Desafio ---
    if st.session_state[f"{GAME_KEY}_status"] in ["new", "correct"]:
        get_new_challenge(GAME_KEY)

    challenge = st.session_state[f"{GAME_KEY}_challenge"]

    if not challenge:
        st.error("Erro: Não foi possível carregar um desafio.")
        return

    # --- 3. Renderização da UI (Visão) ---
    st.markdown("### Ouça a frase e escreva o que você ouviu:")

    if os.path.exists(challenge["image"]):
        st.image(challenge["image"], width=300)
    else:
        st.warning(f"Imagem de dica não encontrada em: {challenge['image']}")

    # Botão para tocar o áudio
    sentence_to_say = challenge["sentence"]
    if st.button("Ouvir a frase 🔊", width=300):
        audio_bytes = generate_audio_mp3(sentence_to_say)
        if audio_bytes:
            st.audio(audio_bytes, autoplay=True)

    # --- 4. Lógica de Verificação (Controle) ---
    with st.form(key=f"{GAME_KEY}_form"):
        user_answer = st.text_input(
            "Escreva a frase aqui:",
            disabled=(st.session_state[f"{GAME_KEY}_status"] == "correct")
        )

        submit_button = st.form_submit_button(
            "Verificar Ditado ✅",
            width=300,
            disabled=(st.session_state[f"{GAME_KEY}_status"] == "correct")
        )

        if submit_button:
            # Reutilizando a função de checagem padrão
            check_user_answer(GAME_KEY, user_answer)

    # --- 5. Feedback (Reação ao Estado) ---
    game_status = st.session_state[f"{GAME_KEY}_status"]

    if game_status == "correct":
        correct_sentence = challenge["correct"]
        st.success(f"**MUITO BEM!** Você escreveu: **{correct_sentence}**")
        st.balloons()

        if st.button("Próximo Ditado ➔", width=300, type="primary"):
            st.rerun()

    elif game_status == "wrong":
        st.error("Quase! Ouça de novo e tente corrigir.")
        # Reseta o status para permitir nova tentativa
        st.session_state[f"{GAME_KEY}_status"] = "playing"


if __name__ == "__main__":
    main()
