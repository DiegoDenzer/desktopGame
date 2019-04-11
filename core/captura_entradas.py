import tcod as libtcod


def captura_teclado(key):
    # Movimento teclado
    if key.vk == libtcod.KEY_UP:
        return {'mover': (0, -1)}   # Negativo eixo y pra cima
    elif key.vk == libtcod.KEY_DOWN:
        return {'mover': (0, 1)}  # positivo eixo y pra baixo
    elif key.vk == libtcod.KEY_LEFT:
        return {'mover': (-1, 0)}  # Negativo eixo x pra esquerda
    elif key.vk == libtcod.KEY_RIGHT:
        return {'mover': (1, 0)}  # positivo eixo x pra direita

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: altera para fullscreen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Sai do Jogo.
        return {'sair': True}

    # se nada ser teclado
    return {}