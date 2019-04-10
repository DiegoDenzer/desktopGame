class Tile:
    """
    Não pensei em um nome melhor em portugues por isso TILE ( Telha )
    Um bloco em um mapa. Ele pode ou não ser bloqueado e pode ou não bloquear a visão.
    """
    def __init__(self, bloqueado, bloqueio_visao=None):

        self.bloqueado = bloqueado

        # Por padrão, se um bloco for bloqueado, ele também bloqueia a visão
        if bloqueio_visao is None:
            bloqueio_visao = bloqueado

        self.bloqueio_visao = bloqueio_visao
