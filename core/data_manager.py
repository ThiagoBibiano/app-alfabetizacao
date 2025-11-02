# core/data_manager.py
"""Módulo de gerenciamento de dados.

Centraliza todo o conteúdo (palavras, imagens, desafios) da aplicação
para facilitar a manutenção e expansão.
"""

# Dados para o Módulo 1: Conhecendo as Letras
# Estamos usando caminhos relativos para as imagens
LETTER_EXAMPLES = {
    "A": {"word": "Abelha", "emoji": "🐝", "image": "assets/images/abelha.png"},
    "B": {"word": "Bola", "emoji": "⚽", "image": "assets/images/bola.png"},
    "C": {"word": "Casa", "emoji": "🏠", "image": "assets/images/casa.png"},
    "D": {"word": "Dado", "emoji": "🎲", "image": "assets/images/dado.png"},
    "E": {"word": "Elefante", "emoji": "🐘", "image": "assets/images/elefante.png"},
    # Adicione mais letras conforme criar as imagens
}


# Dados para o Módulo 2: Formando Sílabas
SYLLABLE_CONSONANTS = (
    'B', 'C', 'D', 'F', 'G', 'J', 'L', 'M',
    'N', 'P', 'R', 'S', 'T', 'V', 'X', 'Z'
)

SYLLABLE_VOWELS = ('A', 'E', 'I', 'O', 'U')
