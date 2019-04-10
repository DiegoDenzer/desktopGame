import tcod as libtcod

def desenhar_tudo(console, entidades, largura, altura):
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

