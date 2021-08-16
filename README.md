zinit
=========

**Note:**
This repo is currently in `work in progress` status.

Ansible role which configures zsh, zinit and some shell tools

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
| `users` | [] | Contains list of users for which to configure zsh |

* Users config example:

      users:
        - username: admin
          shell: /bin/zsh
          zsh_config_templates:
            - src: zshrc-default.zsh.j2
              dest: ~/.zshrc
              config:
                lang: en_US.UTF-8
            - src: aliases-default.zsh.j2
              dest: ~/.zsh/aliases.zsh
              config:
                l: ls -lart

Default zshrc template sources every file found in ~/.zsh folder. It has also default
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
         - { role: nekeal.zinit }

License
-------

MIT

Author Information
------------------

Nekeal
