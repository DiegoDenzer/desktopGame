from enum import Enum

import tcod as libtcod


class OrdemDesenho (Enum):
    CORPO = 1
    ITEM = 2
    ATOR = 3


def desenhar_barra(panel, x, y, total_largura, nome, valor, maximo, cor, cor_fundo):
    largura_barra = int(float(valor) / maximo * total_largura)

    libtcod.console_set_default_background(panel, cor_fundo)
    libtcod.console_rect(panel, x, y, total_largura, 1, False, libtcod.BKGND_SCREEN)

    libtcod.console_set_default_background(panel, cor_fundo)
    if largura_barra > 0:
        libtcod.console_rect(panel, x, y, largura_barra, 1, False, libtcod.BKGND_SCREEN)

    libtcod.console_set_default_foreground(panel, libtcod.white)
    libtcod.console_print_ex(panel, int(x + total_largura / 2), y, libtcod.BKGND_NONE, libtcod.CENTER,
                             '{0}: {1}/{2}'.format(nome, valor, maximo))


def desenhar_tudo(console, entidades, mapa, largura, altura, cores, visao, recalcula_visao, player, panel,
                  largura_barra,  largura_tela, altura_painel, panel_y, msg_log, mouse):

    if recalcula_visao:
        # Desenhar mapa
        for y in range(mapa.altura):
            for x in range(mapa.largura):
                visivil = libtcod.map_is_in_fov(visao, x, y)
                parede = mapa.tiles[x][y].bloqueio_visao

                if visivil:
                    if parede:
                        libtcod.console_set_char_background(console, x, y, cores.get('parede_iluminada'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(console, x, y, cores.get('chao_iluminado'), libtcod.BKGND_SET)

                    mapa.tiles[x][y].explorado = True

                elif mapa.tiles[x][y].explorado:

                    if parede:
                        libtcod.console_set_char_background(console, x, y, cores.get('parede_escura'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(console, x, y, cores.get('chao_escuro'), libtcod.BKGND_SET)

    # desanha as entidades

    entidades_ordem = sorted(entidades, key=lambda x: x.ordem_desenho.value)


    for entidade in entidades_ordem:
        desenhar(console, entidade)

    libtcod.console_blit(console, 0, 0, largura, altura, 0, 0, 0)

    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_clear(panel)

    y = 1
    for msg in msg_log.mensagens:
        libtcod.console_set_default_foreground(panel, msg.cor)
        libtcod.console_print_ex(panel, msg_log.x, y, libtcod.BKGND_NONE, libtcod.LEFT, msg.texto)
        y += 1

    desenhar_barra(panel, 1, 1, largura_barra, 'HP', player.combatente.hp, player.combatente.max_hp,
               libtcod.light_red, libtcod.darker_red)

    libtcod.console_set_default_foreground(panel, libtcod.light_gray)
    libtcod.console_print_ex(panel, 1, 0, libtcod.BKGND_NONE, libtcod.LEFT,
                             mostrar_nomes_mouse(mouse, entidades, visao))


    libtcod.console_blit(panel, 0, 0, largura_tela, altura_painel, 0, 0, panel_y)


def mostrar_nomes_mouse(mouse, entidades, mapa):
    (x, y) = (mouse.cx, mouse.cy)

    nomes = [entidade.nome for entidade in entidades
             if entidade.x == x and entidade.y == y and libtcod.map_is_in_fov(mapa, entidade.x, entidade.y)]
    nomes = ', '.join(nomes)

    return nomes.capitalize()


def limpar_tudo(console, entidades):
    for entidade in entidades:
        limpar(console, entidade)


def desenhar(console, entidade):
    libtcod.console_set_default_foreground(console, entidade.cor)
    libtcod.console_put_char(console, entidade.x, entidade.y, entidade.char, libtcod.BKGND_NONE)


def limpar(console, entidade):
    # apaga o caracter responsavel pelo objeto
    libtcod.console_put_char(console, entidade.x, entidade.y, ' ', libtcod.BKGND_NONE)

