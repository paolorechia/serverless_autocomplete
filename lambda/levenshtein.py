import pytest


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
    print(comparisons)
    return comparisons[:limit]


@pytest.mark.parametrize(
    "a,b,expected_distance",
    [
        ("tree", "tree", 0),
        ("tree", "tre", 1),
        ("snd", "sand", 1),
        ("xand", "sand", 1),
        ("topaz", "topazo", 1),
        ("txpaz", "topaz", 1),
        ("automaton", "automaton", 0),
        ("auto", "automaton", 5),
        ("automobile", "automaton", 5),
        ("auto", "autobahn", 4),
        ("auto", "au", 2),
        ("at", "au", 1),
        ("on", "on", 0),
        ("on", "on", 0),
        ("marble", "martin", 3),
        ("", "martin", 6),
        ("mint", "", 4),
    ],
)
def test_levenshtein(a, b, expected_distance):
    assert levenshtein(a, b) == expected_distance


@pytest.mark.parametrize(
    "a, b, expected_matrix",
    [
        (
            "kitten",
            "sitting",
            [
                [0, 1, 2, 3, 4, 5, 6],
                [1, 1, 2, 3, 4, 5, 6],
                [2, 2, 1, 2, 3, 4, 5],
                [3, 3, 2, 1, 2, 3, 4],
                [4, 4, 3, 2, 1, 2, 3],
                [5, 5, 4, 3, 2, 2, 3],
                [6, 6, 5, 4, 3, 3, 2],
                [7, 7, 6, 5, 4, 4, 3],
            ],
        ),
        (
            "Saturday",
            "Sunday",
            [
                [0, 1, 2, 3, 4, 5, 6, 7, 8],
                [1, 0, 1, 2, 3, 4, 5, 6, 7],
                [2, 1, 1, 2, 2, 3, 4, 5, 6],
                [3, 2, 2, 2, 3, 3, 4, 5, 6],
                [4, 3, 3, 3, 3, 4, 3, 4, 5],
                [5, 4, 3, 4, 4, 4, 4, 3, 4],
                [6, 5, 4, 4, 5, 5, 5, 4, 3],
            ],
        ),
    ],
)
def test_edit_distance(a, b, expected_matrix):
    dm = DistanceMatrix(a, b)
    dm.edit_distance()
    assert dm._distance_matrix == expected_matrix


test_word_list = [
    "assert",
    "ball",
    "car",
    "cart",
    "dart"
    "tree",
]

@pytest.mark.parametrize(
    "query,limit,expected",
    [
        (
            "ca", 2, 
            [("car", 1),
            ("cart", 2)]
        ),
        (
            "bal", 1,
            [("ball", 1)]
        )
    ]
)
def test_autocomplete(query, limit, expected):
    suggestions = autocomplete(test_word_list, query, limit=limit)
    assert suggestions == expected