from core.mensagens import Mensagem
import tcod as libtcod


class Combatente:
    """
    Classe guarda dados para a luta.
    Usado hp por ser uma nomenclatura já bastante usada.
    """
    def __init__(self, hp, defesa, forca):
        self.max_hp = hp
        self.hp = hp
        self.defesa = defesa
        self.forca = forca

    def receber_dano(self, dano):
        resultado = []
        self.hp -= dano

        if self.hp <= 0:
            resultado.append({'morto' : self.owner})
        return resultado

    def atacar(self, alvo):
        resultado = []
        dano = self.forca - alvo.combatente.defesa

        if dano > 0:
            resultado.append({'mensagem':
                                  Mensagem(f'{self.owner.nome.capitalize()} atacou {alvo.nome} e causou {str(dano)} de dano.', libtcod.white )} )
            resultado.extend(alvo.combatente.receber_dano(dano))

        else:
            resultado.append({'mensagem':
                                 Mensagem(f'{self.owner.nome.capitalize()} atacou {alvo.name} sem causar dano.', libtcod.white)})

        return resultado