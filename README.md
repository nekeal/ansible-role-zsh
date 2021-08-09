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

Dependencies
------------

None

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
