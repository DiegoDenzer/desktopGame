import tcod as libtcod

class MonstroBasico:
    # alvo no caso e o jogador
    def acao_ai (self, alvo, visao, mapa, entidades):

        monstro = self.owner

        if libtcod.map_is_in_fov(visao, monstro.x, monstro.y):
            if monstro.distancia_para(alvo) >= 2:
                monstro.move_astar(alvo,entidades,mapa)
                monstro.mover_para(alvo.x, alvo.y, mapa, entidades)

            elif alvo.combatente.hp > 0:
                monstro.combatente.atacar(alvo)
