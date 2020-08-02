import pytest

from levenshtein import DistanceMatrix, levenshtein, autocomplete, extract_suggestions


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
    "dart" "tree",
]


@pytest.mark.parametrize(
    "query,limit,expected",
    [("ca", 2, [("car", 1), ("cart", 2)]), ("bal", 1, [("ball", 1)])],
)
def test_autocomplete(query, limit, expected):
    suggestions = autocomplete(test_word_list, query, limit=limit)
    assert suggestions == expected


def test_extract_suggestions():
    assert extract_suggestions([("car", 1), ("cart", 2)]) == ["car", "cart"]
