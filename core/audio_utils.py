# core/audio_utils.py
"""Módulo de utilidades para geração de áudio.

Este módulo centraliza a lógica de Text-to-Speech (TTS),
abstraindo a complexidade da biblioteca gTTS das páginas
da aplicação.
"""

import io
import streamlit as st
from gtts import gTTS
from typing import Optional


def generate_audio_mp3(text: str) -> Optional[bytes]:
    """Gera um áudio MP3 a partir de um texto e o retorna como bytes.

    Utiliza a biblioteca gTTS para converter o texto em fala (em português
    do Brasil) e salva o resultado em um buffer de bytes na memória,
    pronto para ser usado pelo `st.audio`.

    Args:
        text: O texto a ser convertido em fala.

    Returns:
        Um objeto de bytes contendo o áudio MP3, ou None se a geração falhar.
    """
    try:
        tts = gTTS(text=text, lang='pt-br', slow=False)
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)
        return buffer.getvalue()
    except Exception as e:
        st.error(f"Não foi possível gerar o áudio para '{text}'. Erro: {e}")
        return None
