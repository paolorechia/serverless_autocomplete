import pytest


class DistanceMatrix:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.distance_matrix = []

    def __str__(self):
        if not self.distance_matrix:
            return "a: {}\nb: {}\n [Empty Distance Matrix]".format(self.a, self.b)

        assert isinstance(self.distance_matrix, list)

        header = "#  "
        for c in self.a:
            header += " {}".format(c)

        i = 0
        result = header + "\n"

        # Build first row
        result += " "
        first_row = self.distance_matrix[0]
        for n in first_row:
            result += " {}".format(n)

        result += "\n"

        other_rows = self.distance_matrix[1:]
        for row in other_rows:
            result += self.b[i]
            i += 1
            for n in row:
                result += " {}".format(n)
            result += "\n"
        return result

    def create_distance_matrix(self):
        first_row = []
        row = []
        rows = []

        # First Row
        for i in range(len(self.a) + 1):
            first_row.append(i)

        # Zeros
        for _ in range(len(self.a)):
            row.append(0)

        rows.append(first_row[:])

        for i in range(len(self.b)):
            rows.append([i + 1] + row[:])
        
        self.distance_matrix = rows

    def edit_distance(self):
        # Check for empty strings
        print("TODO")
        if len(self.a) == 0:
            return len(self.b)
        if len(self.b) == 0:
            return len(self.a)

        # do more stuff here stuff
        return 0


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
    dm.create_distance_matrix()
    assert dm.distance_matrix == expected_matrix


def levenshtein(a, b):
    dm = DistanceMatrix(a, b)
    dm.create_distance_matrix()
    return dm.edit_distance()


dm = DistanceMatrix("tree", "hop")
dm.create_distance_matrix()
print(dm)
