# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* Add `zsh-pyenv` to default set of plugins [!5](https://github.com/nekeal/ansible-role-zsh/pull/5)
* Add .zshenv to default files created from env_vars [!8](https://github.com/nekeal/ansible-role-zsh/pull/8)
* Add jinja blocks to templates [!8](https://github.com/nekeal/ansible-role-zsh/pull/8)
* Add new default plugins to zinit [!8](https://github.com/nekeal/ansible-role-zsh/pull/8)
* Add fzf to default zinit plugins template [!9](https://github.com/nekeal/ansible-role-zsh/pull/9)
* Add nvm to default zinit plugins template [!10](https://github.com/nekeal/ansible-role-zsh/pull/10)
* Add support for [tfenv](https://github.com/tfutils/tfenv) and [tgenv](https://github.com/cunymatthieu/tgenv/tree/master/bin) version managers [!11](https://github.com/nekeal/ansible-role-zsh/pull/11)

### Fixed

* Fixed tags for zinit tasks [!5](https://github.com/nekeal/ansible-role-zsh/pull/5)
* Fix problem with permissions for other users than `remote_user` [!7](https://github.com/nekeal/ansible-role-zsh/pull/5)
* Loading `zsh-pyenv` plugin is no longer verbose [!8](https://github.com/nekeal/ansible-role-zsh/pull/8)
* Fix example in readme (thanks to [eastokes](https://github.com/eastokes)) [!13](https://github.com/nekeal/ansible-role-zsh/pull/13)
* Fix aliases default template [!12](https://github.com/nekeal/ansible-role-zsh/pull/12)

## [1.0.0]

### Added
* Bootstrap project with molecule [!1](https://github.com/nekeal/ansible-role-zsh/pull/1)
* Installation of zsh from source [!2](https://github.com/nekeal/ansible-role-zsh/pull/2)
* Add configuring zsh config templates per user [!3](https://github.com/nekeal/ansible-role-zsh/pull/3)
* Add zinit installation with default set of plugins [zinit-plugins-defaults.zsh.j2](./templates/zinit-plugins-default.zsh.j2) [!4](https://github.com/nekeal/ansible-role-zsh/pull/4)

### Changed
* Some templates are enabled by default [!4](https://github.com/nekeal/ansible-role-zsh/pull/4)
