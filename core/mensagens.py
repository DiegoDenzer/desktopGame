import tcod as libtcod
import textwrap


class Mensagem:
    def __init__(self, texto, cor=libtcod.white):
        self.texto = texto
        self.cor = cor


class MensagemLog:
    def __init__(self, x , largura, altura):
        self.mensagens = []
        self.x = x
        self.largura = largura
        self.altura = altura

    def add_msg(self, msg):
        # Split the message if necessary, among multiple lines
        nova_linha = textwrap.wrap(msg.texto, self.largura)

        for linha in nova_linha:

            if len(self.mensagens) == self.altura:
                del self.mensagens[0]

            self.mensagens.append(Mensagem(linha, msg.cor))
