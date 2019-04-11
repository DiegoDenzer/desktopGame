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
        self.hp -= dano

    def atacar(self, alvo):
        dano = self.forca - alvo.combatente.defesa

        if dano > 0:
            alvo.combatente.receber_dano(dano)
            print(f'{self.owner.nome.capitalize()} atacou {alvo.nome} e causou {str(dano)} de dano.')
        else:
            print(f'{self.owner.nome.capitalize()} atacou {alvo.name} sem causar dano.')