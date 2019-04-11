import tcod as libtcod

from core.entidade import Entidade

from core.captura_entradas import captura_teclado
from core.renderizacao import desenhar_tudo, limpar_tudo
from core.visao import inicializa_visao, recalcular_visao
from maps.mapa_jogo import MapaJogo


def main():

    # Largura
    largura_tela = 80
    # Altura
    altura_tela = 50

    mapa_largura = 80
    mapa_altura = 50

    tamanho_max_sala = 10
    tamanho_min_sala = 6
    max_salas = 30

    visao_algoritimo = 0
    visao_ilumina_parede = True
    area_visao = 3

    cores = {
        'parede_escura': libtcod.Color(0, 0, 100),
        'chao_escuro': libtcod.Color(180, 180, 180),
        'parede_iluminada': libtcod.Color(130, 110, 50),
        'chao_iluminado': libtcod.Color(200, 180, 50)
    }

    player = Entidade(int(largura_tela / 2), int(altura_tela / 2), '@', libtcod.white)
    npc = Entidade(int(largura_tela / 2 - 5), int(altura_tela / 2), 'N', libtcod.yellow)

    entidades = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(largura_tela, altura_tela, 'Dugeon Diego', False)

    console = libtcod.console_new(largura_tela, altura_tela)

    mapa_jogo = MapaJogo(mapa_largura, mapa_altura)
#    mapa_jogo.fazer_mapa_estatico()
    # Desenha a DG.
    mapa_jogo.fazer_mapa(max_salas, tamanho_min_sala, tamanho_max_sala, mapa_largura, mapa_altura, player)

    recalcula_visao = True

    visao = inicializa_visao(mapa_jogo)

    # cria variaveis para teclas e Mouse.
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # captura eventos
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        if recalcula_visao:
            recalcular_visao(visao, player.x, player.y, area_visao, visao_ilumina_parede, visao_algoritimo)

        # desenhar
        desenhar_tudo(console, entidades,mapa_jogo, largura_tela, altura_tela, cores, visao, recalcula_visao)

        recalcula_visao = False

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
            if not mapa_jogo.is_bloqueado(player.x + dx, player.y + dy):
                player.mover(dx, dy)
                recalcula_visao = True

        if sair:
            return True

        if tela_cheia:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()