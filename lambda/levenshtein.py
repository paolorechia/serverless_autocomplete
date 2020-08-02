import pytest
from collections import namedtuple


class DistanceMatrix:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.distance_matrix = self.create_distance_matrix(a, b)

    def __str__(self):
        header = "#"
        for c in self.a:
            header += " {}".format(c)

        i = 0
        result = header + "\n"
        for row in self.distance_matrix:
            result += self.b[i]
            i += 1
            for n in row:
                result += " {}".format(n)
            result += "\n"

        return result

    def create_distance_matrix(self, a, b):
        rows = []
        columns = []
        for _ in range(len(a)):
            rows.append(0)
        for _ in range(len(b)):
            columns.append(rows[:])
        return columns


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


def levenshtein(a, b):
    # Check for empty strings
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    return 0


print(DistanceMatrix("tree", "hop"))
