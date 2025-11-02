# core/game_logic.py
"""Módulo de Lógica de Jogo e Gerenciamento de Estado.

Este módulo encapsula toda a lógica de estado (usando st.session_state)
para os minigames da aplicação. Ele é reutilizável para qualquer
jogo que precise:
1.  Inicializar um estado.
2.  Sortear um novo desafio.
3.  Verificar uma resposta do usuário.
"""

import streamlit as st
import random
from typing import List, Dict, Any

def initialize_game_state(game_key: str, challenges: List[Dict[str, Any]]):
    """Inicializa o estado da sessão para um jogo específico.

    Verifica se as chaves necessárias para um jogo (desafio, status, dados)
    já existem no st.session_state. Se não, cria-as com valores padrão.

    Args:
        game_key: Uma string única que identifica o jogo (ex: "complete_word").
        challenges: A lista completa de desafios (dicionários) para este jogo,
                    geralmente vinda do data_manager.
    """
    state_keys = {
        "challenge": None,  # O desafio atual (ex: um dict de "casa")
        "status": "new",    # Status: "new", "playing", "correct", "wrong"
        "data": challenges  # A lista completa de todos os desafios
    }

    for key, default_value in state_keys.items():
        session_key = f"{game_key}_{key}"
        if session_key not in st.session_state:
            st.session_state[session_key] = default_value

def get_new_challenge(game_key: str):
    """Sorteia um novo desafio e atualiza o estado da sessão.

    Seleciona aleatoriamente um desafio da lista de dados do jogo
    e o define como o desafio atual. O status do jogo é
    resetado para "playing".

    Args:
        game_key: A chave do jogo para o qual sortear um desafio.
    """
    challenge_list = st.session_state[f"{game_key}_data"]

    # Tenta não repetir o desafio anterior
    current_challenge = st.session_state[f"{game_key}_challenge"]
    new_challenge = random.choice(challenge_list)

    # Se a lista tiver mais de um item e o sorteado for igual ao atual
    if len(challenge_list) > 1 and new_challenge == current_challenge:
        while new_challenge == current_challenge:
            new_challenge = random.choice(challenge_list)

    st.session_state[f"{game_key}_challenge"] = new_challenge
    st.session_state[f"{game_key}_status"] = "playing"


def check_user_answer(game_key: str, user_answer: str) -> bool:
    """Verifica a resposta do usuário contra a resposta correta.

    Compara a resposta fornecida pelo usuário (user_answer) com a
    resposta ("correct") armazenada no desafio atual no estado da sessão.
    Atualiza o status do jogo para "correct" ou "wrong".

    Args:
        game_key: A chave do jogo que está sendo verificado.
        user_answer: A string de resposta fornecida pelo usuário.

    Returns:
        True se a resposta estiver correta, False caso contrário.
    """
    correct_answer = st.session_state[f"{game_key}_challenge"]["correct"]

    # Comparação case-insensitive e sem espaços extras
    is_correct = user_answer.strip().lower() == correct_answer.strip().lower()

    if is_correct:
        st.session_state[f"{game_key}_status"] = "correct"
        return True
    else:
        st.session_state[f"{game_key}_status"] = "wrong"
        return False


def initialize_scramble_game(game_key: str, challenges: List[Dict[str, Any]]):
    """Inicializa o estado da sessão para o jogo de organizar frases.

    Reutiliza a inicialização padrão e adiciona chaves de estado
    específicas para este jogo (tentativa do usuário e palavras restantes).

    Args:
        game_key: A chave única do jogo (ex: "scramble_sentence").
        challenges: A lista de desafios do data_manager.
    """
    # 1. Roda a inicialização padrão
    initialize_game_state(game_key, challenges)

    # 2. Adiciona chaves de estado específicas deste jogo
    if f"{game_key}_user_attempt" not in st.session_state:
        st.session_state[f"{game_key}_user_attempt"] = []  # Palavras clicadas
    if f"{game_key}_remaining_words" not in st.session_state:
        st.session_state[f"{game_key}_remaining_words"] = [] # Palavras-botão

def setup_scramble_challenge(game_key: str):
    """Configura um novo desafio de organizar frases.

    Esta função pega um novo desafio, embaralha as palavras-botão
    e reseta o estado da tentativa do usuário.

    Args:
        game_key: A chave do jogo.
    """
    # 1. Pega um novo desafio usando a lógica padrão
    get_new_challenge(game_key)

    # 2. Configura as palavras
    challenge = st.session_state[f"{game_key}_challenge"]
    if challenge:
        # Copia a lista de palavras e a embaralha
        words_to_scramble = list(challenge["words"])
        random.shuffle(words_to_scramble)

        # 3. Reseta o estado do jogo para este novo desafio
        st.session_state[f"{game_key}_user_attempt"] = []
        st.session_state[f"{game_key}_remaining_words"] = words_to_scramble
        st.session_state[f"{game_key}_status"] = "playing"

def add_word_to_scramble_attempt(game_key: str, word: str):
    """Adiciona uma palavra clicada à tentativa do usuário.

    Move a palavra da lista 'remaining_words' para a lista 'user_attempt'.

    Args:
        game_key: A chave do jogo.
        word: A palavra que foi clicada.
    """
    if word in st.session_state[f"{game_key}_remaining_words"]:
        st.session_state[f"{game_key}_user_attempt"].append(word)
        st.session_state[f"{game_key}_remaining_words"].remove(word)
        st.session_state[f"{game_key}_status"] = "playing"

def clear_scramble_attempt(game_key: str):
    """Limpa a tentativa do usuário e restaura os botões.

    Chamado quando o usuário clica em 'Limpar'.
    """
    challenge = st.session_state[f"{game_key}_challenge"]
    if challenge:
        words_to_scramble = list(challenge["words"])
        random.shuffle(words_to_scramble)
        st.session_state[f"{game_key}_user_attempt"] = []
        st.session_state[f"{game_key}_remaining_words"] = words_to_scramble
        st.session_state[f"{game_key}_status"] = "playing"

def check_scramble_answer(game_key: str) -> bool:
    """Verifica a frase montada pelo usuário.

    Junta as palavras da 'user_attempt' e compara com a
    resposta correta. Atualiza o status do jogo.

    Args:
        game_key: A chave do jogo.

    Returns:
        True se a resposta estiver correta, False caso contrário.
    """
    attempt_list = st.session_state[f"{game_key}_user_attempt"]
    user_sentence = " ".join(attempt_list)

    challenge = st.session_state[f"{game_key}_challenge"]
    correct_sentence = challenge["correct"]

    # Comparação exata, case-sensitive
    is_correct = (user_sentence.strip() == correct_sentence.strip())

    if is_correct:
        st.session_state[f"{game_key}_status"] = "correct"
        return True
    else:
        st.session_state[f"{game_key}_status"] = "wrong"
        return False
