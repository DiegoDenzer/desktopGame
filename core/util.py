from enum import Enum


class EstadoJogo(Enum):
    TURNO_JOGADOR = 1
    TURNO_INIMIGO = 2
    JOGADOR_MORTO = 3
