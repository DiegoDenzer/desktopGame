import tcod as libtcod

class MonstroBasico:
    # alvo no caso e o jogador
    def acao_ai (self, alvo, visao, mapa, entidades):
        resultado = []
        monstro = self.owner

        if libtcod.map_is_in_fov(visao, monstro.x, monstro.y):
            if monstro.distancia_para(alvo) >= 2:
                monstro.move_astar(alvo,entidades,mapa)

            elif alvo.combatente.hp > 0:
                resultado_ataque = monstro.combatente.atacar(alvo)
                resultado.extend(resultado_ataque)

        return resultado