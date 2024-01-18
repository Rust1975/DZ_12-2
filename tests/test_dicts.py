from utils import dicts


def test_dicts():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "bazaar") == "git"
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", "mercurial") == "mercurial"
    assert dicts.get_val({}, "vcs", "mercurial") == "mercurial"
    assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"
