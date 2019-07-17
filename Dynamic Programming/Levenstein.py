class Levenstein:

    @staticmethod
    def distance(string1, string2):
        aux = [[0 for col in range(len(string2) + 1)] for row in range(len(string1) + 1)]
        for i in range(1, len(string1) + 1):
            aux[i][0] = i
        for j in range(1, len(string2) + 1):
            aux[0][j] = j
        for j in range(1, len(string2) + 1):
            for i in range(1, len(string1) + 1):
                if string1[i-1] == string2[j-1]:
                    aux[i][j] = aux[i-1][j-1]
                else:
                    aux[i][j] = Levenstein._min(aux[i-1][j] + 1, aux[i][j-1] + 1, aux[i-1][j-1] + 1)
        return aux[len(string1)][len(string2)]

    @staticmethod
    def _min(x, y, z):
        min = x
        if y < min:
            min = y
        if z < min:
            min = z
        return min