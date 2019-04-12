import tcod as libtcod

from core.mensagens import Mensagem
from core.renderizacao import OrdemDesenho
from core.util import EstadoJogo


def matar_jogador(player):
    player.char = '%'
    player.cor = libtcod.dark_red
    return Mensagem('Você morreu !', libtcod.red), EstadoJogo.JOGADOR_MORTO

def kill_monster(monstro):
    msg = '{0} esta morto!'.format(monstro.nome.capitalize())
    msg = Mensagem('{0} esta morto!'.format(monstro.nome.capitalize()), libtcod.orange)
    monstro.char = '%'
    monstro.color = libtcod.dark_red
    monstro.bloqueia = False
    monstro.combatente = None
    monstro.ai = None
    monstro.nome = 'Restos de ' + monstro.nome
    monstro.ordem_desenho = OrdemDesenho.CORPO
    return msg