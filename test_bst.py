from random import randint

import pytest

from main import binary_search_tree


@pytest.fixture
def creat_list():
    out = []
    for _ in range(10):
        out.append(randint(0, 100))
    return out


@pytest.fixture
def tree():
    tree = binary_search_tree()

    return tree


def test_insert(tree, creat_list):
    list_tree = list(tree)
    for i in creat_list:
        tree.insert(i)

    assert all(elem in creat_list for elem in list_tree)
    assert len(list_tree) == len(creat_list)
