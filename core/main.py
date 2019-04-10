import tcod as libtcod

from core.entidade import Entidade

from core.captura_entradas import captura_teclado
from core.renderizacao import desenhar_tudo, limpar_tudo


def main():

    # Largura
    largura_tela = 50
    # Altura
    altura_tela = 50

    mapa_largura = 45
    mapa_altura = 45

    player = Entidade(int(largura_tela / 2), int(altura_tela / 2), '@', libtcod.white)
    npc = Entidade(int(largura_tela / 2 - 1), int(altura_tela / 2), 'N', libtcod.yellow)

    entidades = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(largura_tela, altura_tela, 'Dugeon Diego', False)

    console = libtcod.console_new(largura_tela, altura_tela)

    # cria variaveis para teclas e Mouse.
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # captura eventos
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # desenhar
        desenhar_tudo(console, entidades, largura_tela, altura_tela)

        libtcod.console_flush()
        # limpar
        limpar_tudo(console, entidades)

        # Recebe um dicionario
        acao = captura_teclado(key)

        mover = acao.get('mover')
        sair = acao.get('sair')
        tela_cheia = acao.get('fullscreen')

        if mover:
            dx, dy = mover
            player.mover(dx, dy)

        if sair:
            return True

        if tela_cheia:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())



if __name__ == '__main__':
    main()