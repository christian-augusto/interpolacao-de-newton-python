class InterpolacaoNewton:
    def __init__(self, pontos):
        if len(pontos) <= 1:
            raise Exception(
                'Precisam existir ao menos 2 pontos para o cálculo')

        self.pontos = pontos

    def calcular_deltas(self):
        """
            Calcula os deltas por nível, começando por:
                (y(i + 1) - yi) / (x(i + 1) - xi)

            Seguindo com:
                (delta(i + 1) - delta(i)) / (x(nivel + i) - x(0 + i))
        """

        self.deltas_por_niveis = []

        for nivel in range(1, len(self.pontos)):
            valores = []

            tamanho_calc = None
            indices_deltas = None

            if nivel == 1:
                tamanho_calc = len(self.pontos) - 1
            else:
                indices_deltas = nivel - 2
                tamanho_calc = len(self.deltas_por_niveis[indices_deltas]) - 1

            for j in range(0, tamanho_calc):
                delta_1 = None
                delta_2 = None

                if nivel == 1:
                    delta_1 = self.pontos[j + 1]["y"]
                    delta_2 = self.pontos[j]["y"]
                else:
                    delta_1 = self.deltas_por_niveis[indices_deltas][j + 1]
                    delta_2 = self.deltas_por_niveis[indices_deltas][j]

                x_1 = self.pontos[nivel + j]["x"]
                x_2 = self.pontos[0 + j]["x"]

                valores.append((delta_1 - delta_2) / (x_1 - x_2))

            nivel += 1

            self.deltas_por_niveis.append(valores)

    def deltas_finais(self):
        """
            Escolhe o primeiro y e os primeiros deltas de cada nível para
            montar o array de deltas que será usado na multiplicação
        """

        self.deltas = []

        self.deltas.append(self.pontos[0]["y"])

        for deltas_por_nivel in self.deltas_por_niveis:
            self.deltas.append(deltas_por_nivel[0])

    def calcular_y(self, x):
        """
            Realiza as multiplicações do método de newton:

            delta(0) + (delta(i)*(x - x(0))* ... (x - xi))
        """

        y = self.deltas[0]

        for i in range(1, len(self.deltas)):
            value = self.deltas[i]

            for j in range(0, i):
                value *= (x - self.pontos[j]["x"])

            y += value

        return y

    def calcular(self, x):
        self.calcular_deltas()
        self.deltas_finais()

        return self.calcular_y(x)
