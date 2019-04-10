class Entidade:
    """
    Um objeto genérico para representar jogadores, inimigos, itens, etc.
    """

    def __init__(self, x, y, char, cor):
        self.x = x
        self.y = y
        self.char = char  # por hora o simbolo que represta a entidade depois podemos mudar
        self.cor = cor  # cor

    def mover(self, dx, dy):
        # Move a entidade com os parametros passados em dx e dy
        self.x += dx
        self.y += dy
