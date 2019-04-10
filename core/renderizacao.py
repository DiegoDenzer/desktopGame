import tcod as libtcod


def desenhar_tudo(console, entidades, mapa, largura, altura, cores):

    # Desenhar mapa
    for y in range(mapa.altura):
        for x in range(mapa.largura):
            wall = mapa.tiles[x][y].bloqueio_visao
            if wall:
                libtcod.console_set_char_background(console, x, y, cores.get('parede'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(console, x, y, cores.get('chao'), libtcod.BKGND_SET)

    # Draw all entities in the list
    for entidade in entidades:
        desenhar(console, entidade)

    libtcod.console_blit(console, 0, 0, largura, altura, 0, 0, 0)


def limpar_tudo(console, entidades):
    for entidade in entidades:
        limpar(console, entidade)


def desenhar(console, entidade):
    libtcod.console_set_default_foreground(console, entidade.cor)
    libtcod.console_put_char(console, entidade.x, entidade.y, entidade.char, libtcod.BKGND_NONE)


def limpar(console, entidade):
    # apaga o caracter responsavel pelo objeto
    libtcod.console_put_char(console, entidade.x, entidade.y, ' ', libtcod.BKGND_NONE)

