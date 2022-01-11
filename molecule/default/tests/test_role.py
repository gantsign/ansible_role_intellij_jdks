import pytest


@pytest.mark.parametrize('file_path,expected_text', [
    ('jdk.table.xml', '/usr/lib/jvm/java-1.8.0-openjdk'),
    ('jdk.table.xml', '/usr/lib/jvm/java-11-openjdk-amd64'),
    ('project.default.xml', 'project-jdk-name="1.8"'),
])
def test_config_files(host, file_path, expected_text):
    config_dir_pattern = (
        '\\.config/JetBrains/(IdeaIC|IntelliJIdea)[0-9]+\\.[0-9]/options$')
    config_home = host.check_output('find %s | grep --color=never -E %s',
                                    '/home/test_usr',
                                    config_dir_pattern)
    assert host.file(config_home + '/' + file_path).contains(expected_text)
