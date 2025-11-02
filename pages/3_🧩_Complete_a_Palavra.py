# pages/3_🧩_Complete_a_Palavra.py
"""Página Módulo 3: Jogo de Completar a Palavra.

O usuário vê uma imagem e uma palavra incompleta (ex: CA___).
Ele deve clicar no botão da sílaba correta para completar a palavra.
"""

import streamlit as st
import os
from core.game_logic import initialize_game_state, get_new_challenge, check_user_answer
from core.audio_utils import generate_audio_mp3
from core.data_manager import COMPLETE_WORD_CHALLENGES

# Chave única para este jogo no session_state
GAME_KEY = "complete_word"

def main():
    """Função principal para renderizar a página do Módulo 3."""
    st.title("🧩 Complete a Palavra")

    # --- 1. Inicialização do Estado ---
    # Isso garante que nosso "cérebro" para este jogo exista
    initialize_game_state(GAME_KEY, COMPLETE_WORD_CHALLENGES)

    # --- 2. Lógica de Carregamento do Desafio ---
    # Se o jogo é novo ou se o usuário acabou de acertar, pegue um novo desafio
    if st.session_state[f"{GAME_KEY}_status"] in ["new", "correct"]:
        get_new_challenge(GAME_KEY)

    # Pega o desafio atual do estado para exibir
    challenge = st.session_state[f"{GAME_KEY}_challenge"]

    if not challenge:
        st.error("Erro: Não foi possível carregar um desafio.")
        return

    # --- 3. Renderização da UI (Visão) ---
    st.markdown(f"### O que você vê na imagem? Complete a palavra:")

    # Exibe a imagem
    if os.path.exists(challenge["image"]):
        st.image(challenge["image"], width=300)
    else:
        st.error(f"Imagem não encontrada em: {challenge['image']}")

    # Exibe o prompt (ex: "CA ___")
    st.header(challenge["prompt"])

    st.divider()
    st.write("Clique na sílaba correta:")

    # Cria colunas para os botões de opção
    options = challenge["options"]
    cols = st.columns(len(options))

    for i, option in enumerate(options):
        with cols[i]:
            # --- 4. Lógica de Verificação (Controle) ---
            if st.button(option, key=f"{GAME_KEY}_{option}", width=300):
                # O usuário clicou, vamos checar a resposta
                check_user_answer(GAME_KEY, option)
                # Força um rerun imediato para mostrar o feedback (Correto/Errado)
                st.rerun()

    # --- 5. Feedback (Reação ao Estado) ---
    game_status = st.session_state[f"{GAME_KEY}_status"]

    if game_status == "correct":
        full_word = challenge["full_word"]
        st.success(f"**ISSO AÍ!** Você formou a palavra **{full_word}**!")
        st.balloons()

        # Toca o som da palavra completa
        audio_bytes = generate_audio_mp3(full_word)
        if audio_bytes:
            st.audio(audio_bytes, autoplay=True)

        # Botão para ir para o próximo desafio
        if st.button("Próxima Palavra ➔", width=300, type="primary"):
            # O status já é "correct", então no próximo rerun ele vai
            # acionar a lógica no passo 2 e pegar um novo desafio.
            st.rerun()

    elif game_status == "wrong":
        st.error("Ops! Tente de novo. Você consegue!")
        # Reseta o status para "playing" para permitir nova tentativa
        st.session_state[f"{GAME_KEY}_status"] = "playing"


if __name__ == "__main__":
    main()
