
class DistanceMatrix:
    def __init__(self, a, b):
        self._a = a
        self._b = b
        self._distance_matrix = []
        self._edit_distance = 0

    def __str__(self):
        if not self._distance_matrix:
            return "a: {}\nb: {}\n [Empty Distance Matrix]".format(self._a, self._b)

        assert isinstance(self._distance_matrix, list)

        header = "#  "
        for c in self._a:
            header += " {}".format(c)

        i = 0
        result = header + "\n"

        # Build first row
        result += " "
        first_row = self._distance_matrix[0]
        for n in first_row:
            result += " {}".format(n)

        result += "\n"

        other_rows = self._distance_matrix[1:]
        for row in other_rows:
            result += self._b[i]
            i += 1
            for n in row:
                result += " {}".format(n)
            result += "\n"
        return result

    def _create_distance_matrix(self):
        first_row = []
        row = []
        rows = []

        # First Row
        for i in range(len(self._a) + 1):
            first_row.append(i)

        # Zeros
        for _ in range(len(self._a)):
            row.append(0)

        rows.append(first_row[:])

        for i in range(len(self._b)):
            rows.append([i + 1] + row[:])

        # Update values with Levenshtein distance
        # Algorithm: Wagner–Fischer_algorithm
        # Source: https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm

        self._distance_matrix = rows

        for i in range(len(self._b)):
            for j in range(len(self._a)):
                if (self._b[i] == self._a[j]):
                    cost = 0
                else:
                    cost = 1

                self._distance_matrix[i+1][j+1] = \
                    min(
                        self._distance_matrix[i][j+1] + 1,       # deletion
                        self._distance_matrix[i+1][j] + 1,        # insertion
                        self._distance_matrix[i][j] + cost       # substition
                        )
        

    def edit_distance(self):
        if len(self._a) == 0:
            return len(self._b)
        if len(self._b) == 0:
            return len(self._a)

        self._create_distance_matrix()
        self._edit_distance = self._distance_matrix[-1][-1]

        return self._distance_matrix[-1][-1]


def levenshtein(a, b):
    dm = DistanceMatrix(a, b)
    return dm.edit_distance()


def autocomplete(word_list, input_, limit=5):
    comparisons = []
    for word in word_list:
        comparisons.append((word, levenshtein(word, input_)))

    comparisons.sort(key = lambda x : x[1])
    return comparisons[:limit]

def extract_suggestions(suggestions):
    return [ w[0] for w in suggestions ]

