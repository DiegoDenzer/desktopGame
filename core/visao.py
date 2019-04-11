import tcod as libtcod


def inicializa_visao(mapa):
    visao = libtcod.map_new(mapa.largura, mapa.altura)

    for y in range(mapa.altura):
        for x in range(mapa.largura):
            libtcod.map_set_properties(visao, x, y, not mapa.tiles[x][y].bloqueio_visao,
                                       not mapa.tiles[x][y].bloqueado)

    return visao


def recalcular_visao(visao, x, y, area, iluminar_parede=True, algoritimo=0):
    libtcod.map_compute_fov(visao, x, y, area, iluminar_parede, algoritimo)