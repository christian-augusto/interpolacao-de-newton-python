from interpolacao_newton import InterpolacaoNewton


def testes():
    # Prova

    pontos = [
        {
            "x": 3,
            "y": 2
        },
        {
            "x": 4,
            "y": 1
        }
    ]
    interpolacao_newton_1 = InterpolacaoNewton(pontos)

    print(interpolacao_newton_1.calcular(3.7))  # R: 1.3

    """
    pontos = [
        {
            "x": 3,
            "y": 2
        },
        {
            "x": 4,
            "y": 1
        },
        {
            "x": 5,
            "y": 2
        }
    ]
    interpolacao_newton_1 = InterpolacaoNewton(pontos)

    print(interpolacao_newton_1.calcular(3.7)) # R: aprox 1.09
    """

    """
    pontos = [
        {
            "x": 2,
            "y": -18
        },
        {
            "x": 4,
            "y": 28
        },
        {
            "x": 6,
            "y": 106
        }
    ]
    interpolacao_newton_1 = InterpolacaoNewton(pontos)

    print(interpolacao_newton_1.calcular(3)) # R: 1
    """

    """
    pontos = [
        {
            "x": 2,
            "y": -18
        },
        {
            "x": 4,
            "y": 28
        },
        {
            "x": 6,
            "y": 106
        }
    ]
    interpolacao_newton_1 = InterpolacaoNewton(pontos)

    print(interpolacao_newton_1.calcular(5)) # R: 63
    """

    # Lista
    """
    pontos = [
        {
            "x": 3,
            "y": 92
        },
        {
            "x": 4,
            "y": 132
        }
    ]
    interpolacao_newton_1 = InterpolacaoNewton(pontos)

    print(interpolacao_newton_1.calcular(3.7)) # R: 120
    """

    """
    pontos = [
        {
            "x": 2,
            "y": 65
        },
        {
            "x": 3,
            "y": 92
        },
        {
            "x": 4,
            "y": 132
        }
    ]
    interpolacao_newton_1 = InterpolacaoNewton(pontos)

    print(interpolacao_newton_1.calcular(3.7)) # R: 118,635
    """

    # Outros
    """
    pontos = [
        {
            "x": -2,
            "y": 15
        },
        {
            "x": 2,
            "y": -1
        },
        {
            "x": 5,
            "y": 8
        }
    ]
    interpolacao_newton_1 = InterpolacaoNewton(pontos)

    print(interpolacao_newton_1.calcular(6))
    """

    """
    pontos = [
        {
            "x": 0,
            "y": 1
        },
        {
            "x": 0.1,
            "y": 1.1052
        },
        {
            "x": 0.3,
            "y": 1.3499
        },
        {
            "x": 0.4,
            "y": 1.4918
        },
        {
            "x": 0.6,
            "y": 1.8221
        }
    ]

    interpolacao_newton_1 = InterpolacaoNewton(pontos)

    print(interpolacao_newton_1.calcular(0.5)) R: aprox 1.64776
    """

    print(interpolacao_newton_1.deltas_por_niveis)
    print(interpolacao_newton_1.deltas)


def main():
    testes()


main()
