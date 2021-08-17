Ansible Role: Zsh
---
 [![CI](https://github.com/nekeal/ansible-role-zsh/actions/workflows/ci.yml/badge.svg)](https://github.com/nekeal/ansible-role-zsh/actions/workflows/ci.yml)
=========

Ansible role which configures zsh, zinit and some shell tools.

Requirements
------------

Officially supported OSes:

* Debian 11
* Debian 10
* Debian 9
* Ubuntu 18
* Ubuntu 20

Role Variables
--------------

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `zsh_version` | 5.8 | Version of zsh to be installed |
| `zsh_reinstall_from_source` | false | Defines whether to force re-installation zsh even if version matches current installation |
| `zsh_install_bin_prefix` | /bin | Where to keep zsh binary |
| `zsh_user_config_dir` | ~/.zsh | Where to keep and load zsh configuration files |
| `zsh_install_zinit` | true | Whether to install [zinit](https://github.com/zdharma/zinit) plugin manager |
| `zsh_zshrc_template` | zshrc-default.zsh.j2 | Default template used for .zshrc file |
| `zsh_aliases_template` | aliases-default.zsh.j2 | Default template used for file containing aliases definitions |
| `zsh_zinit_plugins_template` | zinit-plugins-default.zsh.j2 | Default template containing plugins for zinit. It contains subset of usefull plugins by default as well as some configurations from [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh/) |
| `users` | [] | Contains list of users for which to configure zsh |

* Users config example:

      users:
        - username: admin
          shell: /bin/zsh
          aliases:
            aliases:
              l: ls -lart
          zshrc:
            template: zshrc-default.zsh.j2
          zsh_config_templates:
            src: extra-config-template.zsh.j2
            dest: ~/.zsh/config.zsh

Default zshrc template sources some common files found in `~` and  `~/.zsh` folder as well as every extra template. It has also default
support for [zinit](https://github.com/zdharma/zinit), [fzf](https://github.com/junegunn/fzf) and [powerlevel10k](https://github.com/romkatv/powerlevel10k)

Dependencies
------------

Roles:
* `nekeal.users` - uses the same list `users` as this role.
`shell` key should be set to `/bin/zsh`

Example:

    users:
      - username: admin
        shell: /bin/zsh

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: nekeal.zsh }

License
-------

MIT

Author Information
------------------

Nekeal
