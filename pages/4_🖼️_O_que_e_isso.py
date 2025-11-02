# pages/4_🖼️_O_que_e_isso.py
"""Página Módulo 4: Jogo de Escrita (O que é isso?).

O usuário vê uma imagem e deve escrever o nome do objeto
em um campo de texto (st.text_input).
"""

import streamlit as st
import os
from core.game_logic import initialize_game_state, get_new_challenge, check_user_answer
from core.audio_utils import generate_audio_mp3
from core.data_manager import IMAGE_TO_WORD_CHALLENGES

# Chave única para este jogo no session_state
GAME_KEY = "image_to_word"


def main():
    """Função principal para renderizar a página do Módulo 4."""
    st.title("🖼️ O que é isso?")

    # --- 1. Inicialização do Estado ---
    initialize_game_state(GAME_KEY, IMAGE_TO_WORD_CHALLENGES)

    # --- 2. Lógica de Carregamento do Desafio ---
    if st.session_state[f"{GAME_KEY}_status"] in ["new", "correct"]:
        get_new_challenge(GAME_KEY)

    challenge = st.session_state[f"{GAME_KEY}_challenge"]

    if not challenge:
        st.error("Erro: Não foi possível carregar um desafio.")
        return

    # --- 3. Renderização da UI (Visão) ---
    st.markdown("### Olhe a imagem e escreva o nome dela abaixo:")

    # Exibe a imagem (usando a correção 'use_container_width')
    if os.path.exists(challenge["image"]):
        st.image(challenge["image"], width=300)
    else:
        st.error(f"Imagem não encontrada em: {challenge['image']}")

    # --- 4. Lógica de Verificação (Controle) ---
    # Usamos st.form para agrupar o text_input e o botão
    # Isso evita que a página recarregue a cada letra digitada
    with st.form(key=f"{GAME_KEY}_form"):
        user_answer = st.text_input(
            "Escreva sua resposta aqui:",
            placeholder="Digite a palavra...",
            # Desabilita o campo se o usuário já acertou
            disabled=(st.session_state[f"{GAME_KEY}_status"] == "correct")
        )

        submit_button = st.form_submit_button(
            "Verificar Resposta ✅",
            width=300,
            # Desabilita o botão se já acertou
            disabled=(st.session_state[f"{GAME_KEY}_status"] == "correct")
        )

        if submit_button:
            # O formulário foi enviado, vamos checar a resposta
            check_user_answer(GAME_KEY, user_answer)
            # st.rerun() não é estritamente necessário aqui
            # porque o st.form já causa um rerun, mas podemos
            # garantir o fluxo se precisarmos. Vamos testar sem.

    # --- 5. Feedback (Reação ao Estado) ---
    game_status = st.session_state[f"{GAME_KEY}_status"]

    if game_status == "correct":
        correct_word = challenge["correct"]
        st.success(f"**PERFEITO!** Você escreveu **{correct_word}** corretamente!")
        st.balloons()

        # Toca o som da palavra correta
        audio_bytes = generate_audio_mp3(correct_word)
        if audio_bytes:
            st.audio(audio_bytes, autoplay=True)

        # Botão para ir para o próximo desafio
        if st.button("Próxima Imagem ➔", width=300, type="primary"):
            # O status já é "correct", então no próximo rerun ele vai
            # acionar a lógica no passo 2 e pegar um novo desafio.
            st.rerun()

    elif game_status == "wrong":
        st.error("Ops, não foi bem isso. Tente de novo! Você consegue!")
        # Reseta o status para "playing" para permitir nova tentativa
        st.session_state[f"{GAME_KEY}_status"] = "playing"


if __name__ == "__main__":
    main()
