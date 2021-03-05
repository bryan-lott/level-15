from src import data
import uuid


def test_sort_by_word_count():
    ns = uuid.uuid4()
    unsorted = [
        (uuid.uuid3(ns, "1"), 3),
        (uuid.uuid3(ns, "2"), 1),
        (uuid.uuid3(ns, "3"), 5),
    ]

    expected = [
        (uuid.uuid3(ns, "3"), 5),
        (uuid.uuid3(ns, "1"), 3),
        (uuid.uuid3(ns, "2"), 1),
    ]

    result = data.sort_by_word_count(unsorted)

    assert expected == result