# pages/5_✍️_Organize_a_Frase.py
"""Página Módulo 5: Jogo de Organizar a Frase.

O usuário vê uma imagem e "peças" (botões) de uma frase.
Ele deve clicar nos botões na ordem correta para formar a frase.
"""

import streamlit as st
import os
from core.game_logic import (
    initialize_scramble_game,
    setup_scramble_challenge,
    add_word_to_scramble_attempt,
    clear_scramble_attempt,
    check_scramble_answer
)
from core.audio_utils import generate_audio_mp3
from core.data_manager import SENTENCE_SCRAMBLE_CHALLENGES

# Chave única para este jogo no session_state
GAME_KEY = "scramble_sentence"


def main():
    """Função principal para renderizar a página do Módulo 5."""
    st.title("✍️ Organize a Frase")

    # --- 1. Inicialização do Estado ---
    initialize_scramble_game(GAME_KEY, SENTENCE_SCRAMBLE_CHALLENGES)

    # --- 2. Lógica de Carregamento do Desafio ---
    if st.session_state[f"{GAME_KEY}_status"] in ["new", "correct"]:
        setup_scramble_challenge(GAME_KEY)

    challenge = st.session_state[f"{GAME_KEY}_challenge"]

    if not challenge:
        st.error("Erro: Não foi possível carregar um desafio.")
        return

    # --- 3. Renderização da UI (Visão) ---
    st.markdown("### Olhe a imagem e clique nas palavras na ordem certa:")

    if os.path.exists(challenge["image"]):
        st.image(challenge["image"], use_container_width=True)
    else:
        st.error(f"Imagem não encontrada em: {challenge['image']}")

    st.divider()

    # Caixa de "Resposta do Usuário"
    user_attempt_list = st.session_state[f"{GAME_KEY}_user_attempt"]
    if not user_attempt_list:
        st.info("Clique nos botões abaixo para montar sua frase aqui...")
    else:
        # Mostra a frase sendo montada
        st.subheader(" ".join(user_attempt_list))

    st.divider()

    # Botões de Palavras (Palavras Restantes)
    remaining_words = st.session_state[f"{GAME_KEY}_remaining_words"]
    if remaining_words:
        # Exibe os botões em colunas
        cols = st.columns(len(remaining_words))
        for i, word in enumerate(remaining_words):
            with cols[i]:
                if st.button(word, key=f"word_{word}_{i}", use_container_width=True):
                    add_word_to_scramble_attempt(GAME_KEY, word)
                    st.rerun()

    # --- 4. Botões de Ação (Controle) ---
    game_status = st.session_state[f"{GAME_KEY}_status"]

    # Só mostra "Verificar" se o usuário usou todas as palavras
    if not remaining_words and game_status == "playing":
        if st.button("Verificar Frase ✅", use_container_width=True, type="primary"):
            check_scramble_answer(GAME_KEY)
            st.rerun()

    # Botão para Limpar a tentativa
    if user_attempt_list and game_status == "playing":
        if st.button("Limpar ❌", use_container_width=True):
            clear_scramble_attempt(GAME_KEY)
            st.rerun()

    # --- 5. Feedback (Reação ao Estado) ---
    if game_status == "correct":
        correct_sentence = challenge["correct"]
        st.success(f"**EXCELENTE!** A frase está correta: **{correct_sentence}**")
        st.balloons()

        audio_bytes = generate_audio_mp3(correct_sentence)
        if audio_bytes:
            st.audio(audio_bytes, autoplay=True)

        if st.button("Próxima Frase ➔", use_container_width=True, type="primary"):
            st.rerun()

    elif game_status == "wrong":
        st.error("Ops! Essa não é a ordem correta. Tente de novo!")
        # Permite ao usuário tentar de novo
        if st.button("Tentar Novamente 🔄", use_container_width=True):
            clear_scramble_attempt(GAME_KEY)
            st.rerun()


if __name__ == "__main__":
    main()
