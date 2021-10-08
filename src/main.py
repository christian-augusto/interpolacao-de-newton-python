from interpolacao_newton import InterpolacaoNewton


def main():
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

    InterpolacaoNewton(pontos).calc()


main()
