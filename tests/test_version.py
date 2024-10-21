import importlib.metadata


def test_version():
    assert isinstance(importlib.metadata.version("play_football_match_highlights"), str)
