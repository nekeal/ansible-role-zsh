"""Role testing files using testinfra."""
import pytest
import requests

def test_zsh_is_installed(host):
    result = host.run("zsh --version")

    assert not result.rc
    assert "5.8" in result.stdout
