#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ != '__main__':

    __dicErros__ = {
        0: "[Erro]: O arquivo contendo o código fonte não foi passado!",
        1: "[Erro]: O arquivo passado possui extensão incompatível.",
        2: "[Erro]: Erro lexico na linha ",
        3: "[Erro]: Erro sintatico. Parenteses sem fechar. ",
        4: "[Erro]: Erro sintatico. Simbolo nao reconhecido. ",
        5: "[Erro]: Erro sintatico. Operador faltando. ",
        6: "[Erro]: Erro sintatico. Expressao invalida. ",
        7: "[Erro]: Erro sintatico. ';' esperado ",
        8: "[Erro]: Erro sintatico. '=' esperado ",
        9: "[Erro]: Erro sintatico. Declaracao invalida.",
        10: "[Erro]: Erro sintatico. '{' esperado.",
        11: "[Erro]: Erro sintatico. '}' esperado."
    }

    __listaErros__ = []

    def getErro(chave, linha, coluna):
        """A função retorna a string do erro correspondente contido no
        dicionário de erros."""

        if(linha is None and coluna is None):
            return __dicErros__[chave]
        return __dicErros__[chave] + ' l: ' + str(linha) + " c: " + str(coluna)

    def getListaErros():
        """A função retorna a lista de erros encontrados no código
        fonte."""

        return __listaErros__

    def setListaErros(erro):
        """A função acrescenta ao final da lista de erros uma nova string
        de um erro encontrado."""
        return __listaErros__.append(erro)
