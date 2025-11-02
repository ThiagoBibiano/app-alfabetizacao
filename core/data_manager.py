# core/data_manager.py
"""Módulo de gerenciamento de dados.

Centraliza todo o conteúdo (palavras, imagens, desafios) da aplicação
para facilitar a manutenção e expansão.
"""

# Dados para o Módulo 1: Conhecendo as Letras
# Estamos usando caminhos relativos para as imagens
LETTER_EXAMPLES = {
    "A": {"word": "Abelha", "emoji": "🐝", "image": "assets/images/abelha.jpg"},
    "B": {"word": "Bola", "emoji": "⚽", "image": "assets/images/bola.jpg"},
    "C": {"word": "Casa", "emoji": "🏠", "image": "assets/images/casa.jpg"},
    "D": {"word": "Dado", "emoji": "🎲", "image": "assets/images/dado.jpg"},
    "E": {"word": "Elefante", "emoji": "🐘", "image": "assets/images/elefante.jpg"},
    # Adicione mais letras conforme criar as imagens
}


# Dados para o Módulo 2: Formando Sílabas
SYLLABLE_CONSONANTS = (
    'B', 'C', 'D', 'F', 'G', 'J', 'L', 'M',
    'N', 'P', 'R', 'S', 'T', 'V', 'X', 'Z'
)

SYLLABLE_VOWELS = ('A', 'E', 'I', 'O', 'U')


COMPLETE_WORD_CHALLENGES = [
    {
        "id": "casa",
        "image": "assets/images/casa.jpg",
        "prompt": "CA ___",
        "options": ["SA", "LA", "MA"],
        "correct": "SA",
        "full_word": "CASA"
    },
    {
        "id": "bola",
        "image": "assets/images/bola.jpg",
        "prompt": "___ LA",
        "options": ["BO", "VE", "PA"],
        "correct": "BO",
        "full_word": "BOLA"
    },
    {
        "id": "gato",
        "image": "assets/images/gato.jpg",
        "prompt": "GA ___",
        "options": ["FO", "TO", "LO"],
        "correct": "TO",
        "full_word": "GATO"
    },
    # Adicione quantos desafios quiser...
]


# (O código anterior: LETTER_EXAMPLES, COMPLETE_WORD_CHALLENGES, etc. ficam acima)
# ...

# ---
# Dados para o Módulo 4: O que é isso? (Imagem -> Palavra)
# ---
IMAGE_TO_WORD_CHALLENGES = [
    {
        "id": "uva",
        "image": "assets/images/uva.jpg",
        "correct": "uva",  # A resposta correta
        "hint": "U-VA"   # Dica (opcional, para uma futura funcionalidade)
    },
    {
        "id": "dado",
        "image": "assets/images/dado.jpg",
        "correct": "dado",
        "hint": "DA-DO"
    },
    {
        "id": "elefante",
        "image": "assets/images/elefante.jpg",
        "correct": "elefante",
        "hint": "E-LE-FAN-TE"
    },
    # Adicione quantos desafios quiser...
]
