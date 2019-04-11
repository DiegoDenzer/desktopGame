import tcod as libtcod


def captura_teclado(key):
    # Movimento teclado
    key_char = chr(key.c)

    if key.vk == libtcod.KEY_UP or key_char == 'k':
        return {'mover': (0, -1)}   # Negativo eixo y pra cima
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
        return {'mover': (0, 1)}  # positivo eixo y pra baixo
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
        return {'mover': (-1, 0)}  # Negativo eixo x pra esquerda
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
        return {'mover': (1, 0)}  # positivo eixo x pra direita
    elif key_char == 'y':
        return {'move': (-1, -1)}
    elif key_char == 'u':
        return {'move': (1, -1)}
    elif key_char == 'b':
        return {'move': (-1, 1)}
    elif key_char == 'n':
        return {'move': (1, 1)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: altera para fullscreen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Sai do Jogo.
        return {'sair': True}

    # se nada ser teclado
    return {}