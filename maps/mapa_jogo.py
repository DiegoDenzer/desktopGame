from random import randint

from maps.retangulo import Retangulo
from maps.tile import Tile


class MapaJogo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.altura)] for x in range(self.largura)]
        return tiles

    def fazer_mapa(self, max_salas, tamanho_min, tamanho_max, largura_mapa, altura_mapa, jogador):

        salas = []
        numero_salas = 0

        for r in range(max_salas):
            # random width and height
            w = randint(tamanho_min, tamanho_max)
            h = randint(tamanho_min, tamanho_max)
            # posição aleatória sem sair dos limites do mapa
            x = randint(0, largura_mapa - w - 1)
            y = randint(0, altura_mapa - h - 1)

            # cria as dimenções da sala
            nova_sala = Retangulo(x, y, w, h)

            # verificar se a sala se sobre pos
            for outra_sala in salas:
                if nova_sala.intercesao(outra_sala):
                    break
            else:
                self.criar_sala(nova_sala)

                # centralizar
                (new_x, new_y) = nova_sala.centralizar()

                if numero_salas == 0:
                    # se a sala for a primeira e onde o jodor comeca
                    jogador.x = new_x
                    jogador.y = new_y
                else:
                    # Demais salas
                    # centralizando
                    (prev_x, prev_y) = salas[numero_salas - 1].centralizar()

                    # um rand aqui para deixar mais interresante
                    if randint(0, 1) == 1:
                        # primeiro horiziontal e depois vertical
                        self.criar_h_tunel(prev_x, new_x, prev_y)
                        self.criar_v_tunel(prev_y, new_y, new_x)
                    else:
                        # aqui é aos contrario né  =)
                        self.criar_v_tunel(prev_y, new_y, prev_x)
                        self.criar_h_tunel(prev_x, new_x, new_y)

                # Fazendo append na lista
                salas.append(nova_sala)
                numero_salas += 1

    def fazer_mapa_estatico(self):
        # Para fins de demonstração
        sala1 = Retangulo(20, 15, 10, 15)
        sala2 = Retangulo(35, 15, 10, 15)
        self.criar_sala(sala1)
        self.criar_sala(sala2)
        self.criar_h_tunel(25, 40, 23)

    def criar_sala(self, sala):
        # Intera o retângulo e torna eles transitáveis
        for x in range(sala.x1 + 1, sala.x2):
            for y in range(sala.y1 + 1, sala.y2):
                self.tiles[x][y].bloqueado = False
                self.tiles[x][y].bloqueio_visao = False

    def criar_h_tunel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].bloqueado = False
            self.tiles[x][y].bloqueio_visao = False

    def criar_v_tunel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].bloqueado = False
            self.tiles[x][y].bloqueio_visao = False

    def is_bloqueado(self, x, y):
        if self.tiles[x][y].bloqueado:
            return True
        return False
