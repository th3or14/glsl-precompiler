import filecmp
import subprocess


def run_precompiler(test_directory):
    args = ['python',
            '../precompiler.py',
            '-D',
            'A=1',
            '-D',
            'B=2',
            '-i',
            test_directory + '/in.glsl',
            '-o',
            test_directory + '/out.glsl']
    return subprocess.run(args)


def run_test(test_directory):
    run_precompiler(test_directory).returncode == 0
    assert filecmp.cmp(test_directory + '/out.glsl',
                       test_directory + '/expected-out.glsl')


def test_version_with_profile():
    test_directory = 'version-with-profile'
    run_test(test_directory)


def test_version_without_profile():
    test_directory = 'version-without-profile'
    run_test(test_directory)


def test_version_with_extra_whitespace():
    test_directory = 'version-with-extra-whitespace'
    run_test(test_directory)
