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

    def fazer_mapa(self):
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
