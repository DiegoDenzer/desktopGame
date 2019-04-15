import tcod as libtcod

from core.componentes.combatente import Combatente
from core.entidade import Entidade, obter_entidade_com_bloqueio_por_localizacao

from core.captura_entradas import captura_teclado
from core.mensagens import MensagemLog
from core.morte import matar_jogador, kill_monster
from core.renderizacao import desenhar_tudo, limpar_tudo, OrdemDesenho
from core.util import EstadoJogo
from core.visao import inicializa_visao, recalcular_visao
from maps.mapa_jogo import MapaJogo

def main():
    # Tela
    # Largura
    largura_tela = 80
    # Altura
    altura_tela = 50

    # Mapa
    mapa_largura = 80
    mapa_altura = 43

    # Sala
    tamanho_max_sala = 10
    tamanho_min_sala = 6
    max_salas = 30

    # Algoritimo para visao (Famoso Fog)
    visao_algoritimo = 0
    visao_ilumina_parede = True
    area_visao = 3

    # interface
    barra_largura = 20
    painel_altura = 7
    painel_y = altura_tela - painel_altura

    msg_x = barra_largura + 2
    msg_alt = largura_tela - barra_largura - 2
    msg_lar = painel_altura + 6

    # Monstros
    monstros_por_sala = 3

    # Cores
    cores = {
        'parede_escura': libtcod.Color(0, 0, 100),
        'chao_escuro': libtcod.Color(180, 180, 180),
        'parede_iluminada': libtcod.Color(130, 110, 50),
        'chao_iluminado': libtcod.Color(200, 180, 50)
    }
    # Jogador
    combatente = Combatente(hp=30, defesa=2, forca=5)
    player = Entidade(0, 0, '@', libtcod.white, 'Diego', bloqueia=True, combatente=combatente,ordem_desenho=OrdemDesenho.ATOR)
   # npc = Entidade(int(largura_tela / 2 - 5), int(altura_tela / 2), 'N', libtcod.yellow, 'SHOP', bloqueia=False)

    # Objetos do Mapa (NPC , Jogador, Monstros, Itens e etc ... )
    entidades = [player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(largura_tela, altura_tela, 'Dugeon Diego', False)

    console = libtcod.console_new(largura_tela, altura_tela)

    painel = libtcod.console_new(largura_tela, painel_altura)


    mapa_jogo = MapaJogo(mapa_largura, mapa_altura)
#    mapa_jogo.fazer_mapa_estatico()
    # Desenha a DG.
    mapa_jogo.fazer_mapa(max_salas, tamanho_min_sala, tamanho_max_sala, mapa_largura, mapa_altura, player,entidades, monstros_por_sala)

    recalcula_visao = True

    visao = inicializa_visao(mapa_jogo)

    msg_log = MensagemLog(msg_x, msg_lar, msg_alt)

    # cria variaveis para teclas e Mouse.
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    estado_jogo = EstadoJogo.TURNO_JOGADOR

    # Com tudo pronto aqui começa o laço principal
    while not libtcod.console_is_window_closed():
        # captura eventos
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

        if recalcula_visao:
            recalcular_visao(visao, player.x, player.y, area_visao, visao_ilumina_parede, visao_algoritimo)

        # desenhar
        desenhar_tudo(console, entidades,mapa_jogo, largura_tela, altura_tela, cores, visao, recalcula_visao, player,
                      painel, barra_largura, largura_tela, painel_altura, painel_y, msg_log, mouse)

        recalcula_visao = False

        libtcod.console_flush()
        # limpar
        limpar_tudo(console, entidades)

        # Recebe um dicionario
        acao = captura_teclado(key)

        mover = acao.get('mover')
        sair = acao.get('sair')
        tela_cheia = acao.get('fullscreen')

        jogador_resultado = []

        if mover and estado_jogo == EstadoJogo.TURNO_JOGADOR:
            dx, dy = mover
            destino_x = player.x + dx
            destino_y = player.y + dy
            if not mapa_jogo.is_bloqueado(destino_x, destino_y):
                alvo = obter_entidade_com_bloqueio_por_localizacao(entidades, destino_x, destino_y)
                if alvo:
                    j_ataque_resultado = player.combatente.atacar(alvo)
                    jogador_resultado.extend(j_ataque_resultado)
                else:
                    player.mover(dx, dy)
                    recalcula_visao = True

                estado_jogo = EstadoJogo.TURNO_INIMIGO

        if sair:
            return True

        if tela_cheia:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        for resultado in jogador_resultado:
            msg = resultado.get('mensagem')
            morto = resultado.get('morto')

            if msg:
                msg_log.add_msg(msg)

            if morto:
                if morto == player:
                    msg, estado_jogo = matar_jogador(morto)
                else:
                    msg = kill_monster(morto)

                msg_log.add_msg(msg)


        if estado_jogo == EstadoJogo.TURNO_INIMIGO:
            for entidade in entidades:
                if entidade.ai:
                    entidade.ai.acao_ai(player, visao,mapa_jogo,entidades)
                    enimigo_resultado = entidade.ai.acao_ai(player, visao,mapa_jogo,entidades)

                    for resultado in enimigo_resultado:
                        msg = resultado.get('mensagem')
                        morto = resultado.get('morto')

                        if msg:
                            msg_log.add_msg(msg)
                        if morto:
                            if morto == player:
                                message, estado_jogo = matar_jogador(morto)
                            else:
                                message = kill_monster(morto)
                            msg_log.add_msg(message)
                            if estado_jogo == EstadoJogo.JOGADOR_MORTO:
                                break
                    if estado_jogo == EstadoJogo.JOGADOR_MORTO:
                        break

            else:
                estado_jogo = EstadoJogo.TURNO_JOGADOR

if __name__ == '__main__':
    main()