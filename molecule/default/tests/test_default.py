"""Role testing files using testinfra."""
import pytest
import requests

debian_based_distros = ("ubuntu", "debian")


def test_zsh_is_installed(host):
    result = host.run("zsh --version")

    assert not result.rc
    assert "5.8" in result.stdout


def test_zsh_dependencies_are_installed(host):
    if host.system_info.distribution in debian_based_distros:
        assert host.package("ncurses-base").is_installed
    else:
        raise


def test_zsh_config_dir_is_created(host):
    assert host.file("/home/zsh-user/.zsh").is_directory


def test_zshrc_is_placed_in_home_directory(host):
    assert host.file("/home/zsh-user/.zshrc").is_file


def test_zshenv_is_placed_in_home_directory(host):
    assert host.file("/home/zsh-user/.zshenv").is_file
