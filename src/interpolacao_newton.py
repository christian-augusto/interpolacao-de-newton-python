class InterpolacaoNewton:
    def __init__(self, pontos):
        if len(pontos) <= 1:
            raise Exception(
                'Precisam existir ao menos 2 pontos para o cálculo')

        self.pontos = pontos

    def calc_deltas(self):
        self.deltas_por_niveis = []

        for nivel in range(1, len(self.pontos)):
            values = []

            indices_deltas = nivel - 2

            calc_len = None

            if nivel == 1:
                calc_len = len(self.pontos) - 1
            else:
                calc_len = len(self.deltas_por_niveis[indices_deltas]) - 1

            for j in range(0, calc_len):
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

                values.append((delta_1 - delta_2) / (x_1 - x_2))

            nivel += 1

            self.deltas_por_niveis.append(values)

    def final_deltas(self):
        self.deltas = []

        self.deltas.append(self.pontos[0]["y"])

        for deltas_por_nivel in self.deltas_por_niveis:
            self.deltas.append(deltas_por_nivel[0])

    def calc_y(self, x):
        y = self.deltas[0]

        for i in range(1, len(self.deltas)):
            value = self.deltas[i]

            for j in range(0, i):
                value *= (x - self.pontos[j]["x"])

            y += value

        return y

    def calc(self, x):
        self.calc_deltas()
        self.final_deltas()

        return self.calc_y(x)
