import pytest
from utils import dicts


@pytest.fixture
def dict_fixture():
    data = {"vcs": "mercurial"}
    return data


@pytest.fixture
def dict_fixture_empty():
    data = {}
    return data


def test_dicts(dict_fixture, dict_fixture_empty):
    assert dicts.get_val(dict_fixture, "vcs") == dict_fixture["vcs"]
    assert dicts.get_val(dict_fixture, "vcs", "git") == dict_fixture["vcs"]
    assert dicts.get_val(dict_fixture_empty, "vcs", "git") == "git"
    assert dicts.get_val(dict_fixture_empty, "vcs", "bazaar") == "bazaar"
