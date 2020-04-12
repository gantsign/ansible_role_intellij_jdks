import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file_path,expected_text', [
    ('jdk.table.xml', '/usr/lib/jvm/java-1.8.0-openjdk'),
    ('jdk.table.xml', '/usr/lib/jvm/java-1.7.0-openjdk'),
    ('project.default.xml', 'project-jdk-name="1.8"'),
])
def test_config_files(host, file_path, expected_text):
    config_dir_pattern = (
        '\\.config/JetBrains/(IdeaIC|IntelliJIdea)[0-9]+\\.[0-9]/options$')
    config_home = host.check_output('find %s | grep --color=never -E %s',
                                    '/home/test_usr',
                                    config_dir_pattern)
    assert host.file(config_home + '/' + file_path).contains(expected_text)
