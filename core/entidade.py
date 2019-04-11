import math
import tcod as libtcod


class Entidade:
    """
    Um objeto genérico para representar jogadores, inimigos, itens, etc.
    """

    def __init__(self, x, y, char, cor, nome, bloqueia=False, combatente=None, ai=None):
        self.x = x
        self.y = y
        self.char = char  # por hora o simbolo que represta a entidade depois podemos mudar
        self.cor = cor  # cor
        self.nome = nome
        self.bloqueia = bloqueia
        self.combatente = combatente
        self.ai = ai

        if self.combatente:
            self.combatente.owner = self

        if self.ai:
            self.ai.owner = self

    def mover(self, dx, dy):
        # Move a entidade com os parametros passados em dx e dy
        self.x += dx
        self.y += dy

    # Mover em direcao ao jogador a entidade ai
    def mover_para(self, alvo_x, alvo_y, mapa, entidades):
        dx = alvo_x - self.x
        dy = alvo_y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distancia))
        dy = int(round(dy / distancia))

        if not (mapa._is_bloqueado(self.x + dx, self.y + dy) or
                obter_entidade_com_bloqueio_por_localizacao(entidades, self.x + dx, self.y + dy)):
            self.move(dx, dy)

    def distancia_para(self, outro):
        dx = outro.x - self.x
        dy = outro.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


    # PARTE DESSE ALGORITIMO NÂO É MEU .. =)  por isso o comentario em ingles do author: Roguebasin
    def move_astar(self, alvo, entidades, mapa):

        fov = libtcod.map_new(mapa.largura, mapa.altura)


        for y1 in range(mapa.altura):
            for x1 in range(mapa.largura):
                libtcod.map_set_properties(fov, x1, y1, not mapa.tiles[x1][y1].block_sight,
                                           not mapa.tiles[x1][y1].blocked)

        for entidade in entidades:
            if entidade.bloqueia and entidade != self and entidade != alvo:
                libtcod.map_set_properties(fov, entidade.x, entidade.y, True, False)

        # Allocate a A* path
        # The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited
        my_path = libtcod.path_new_using_map(fov, 1.41)
        # Compute the path between self's coordinates and the target's coordinates
        libtcod.path_compute(my_path, self.x, self.y, alvo.x, alvo.y)

        # Check if the path exists, and in this case, also the path is shorter than 25 tiles
        # The path size matters if you want the monster to use alternative longer paths (for example through other rooms) if for example the player is in a corridor
        # It makes sense to keep path size relatively low to keep the monsters from running around the map if there's an alternative path really far away
        if not libtcod.path_is_empty(my_path) and libtcod.path_size(my_path) < 25:
            # Find the next coordinates in the computed full path
            x, y = libtcod.path_walk(my_path, True)
            if x or y:
                # Set self's coordinates to the next path tile
                self.x = x
                self.y = y
        else:
            self.mover_para(alvo.x, alvo.y, mapa, entidades)

        # Delete
        libtcod.path_delete(my_path)



# Funcao que não pertence a uma objeto especifico por isso está fora da classe!
def obter_entidade_com_bloqueio_por_localizacao(entidades, local_x, local_y):
    for entidade in entidades:
        if entidade.bloqueia and entidade.x == local_x and entidade.y == local_y:
            return entidade
    return None
