Ansible Role: IntelliJ JDKs
===========================

[![Tests](https://github.com/gantsign/ansible_role_intellij_jdks/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_intellij_jdks/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.intellij__jdks-blue.svg)](https://galaxy.ansible.com/gantsign/intellij_jdks)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_intellij_jdks/master/LICENSE)

Role to configure JDKs in the IntelliJ IDEA IDE
[https://www.jetbrains.com/idea](https://www.jetbrains.com/idea).

Requirements
------------

* Ansible >= 2.8

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Xenial (16.04)
            * Bionic (18.04)
            * Focal (20.04)

    * RedHat Family

        * CentOS

            * 7

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Directory containing IntelliJ IDEA user specific configuration (relative to user home)
# Note: the `ansible_local.intellij.general.user_config_dir` fact is provided by the gantsign.intellij role
intellij_jdks_intellij_user_config_dir: '{{ ansible_local.intellij.general.user_config_dir }}'
```

This role must be configured per user. Users are configured as follows:

```yaml
users:
  - username: # Unix user name
    intellij_jdks:
      - name: # The name use want to use for this JDK
        home: # The path to the JDK home.
    # The name of the JDK you want to be the default for new projects.
    # Required if you specify `intellij_jdks`.
    # Must match the name given to one of the `intellij_jdks`.
    intellij_jdks_default:
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.intellij_jdks
      users:
        - username: vagrant
          intellij_jdks:
            - name: '1.8'
              home: '/usr/lib/jvm/java-8-openjdk-amd64'
            - name: '1.7'
              home: '/usr/lib/jvm/java-7-openjdk-amd64'
            - name: '1.6'
              home: '/usr/lib/jvm/java-6-openjdk-amd64'
          intellij_jdks_default: '1.8'
```

Related Roles
-------------

You may find the following related roles useful:

* [gantsign.intellij](https://galaxy.ansible.com/gantsign/intellij) for
  installing and configuring the IntelliJ IDEA IDE.

* [gantsign.intellij-plugins](https://galaxy.ansible.com/gantsign/intellij-plugins)
  for conditionally installing IntelliJ IDEA IDE plugins.

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
