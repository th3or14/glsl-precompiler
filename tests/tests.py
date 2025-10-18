import filecmp
import subprocess


def run_test(test_directory):
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
    assert subprocess.run(args).returncode == 0
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


def test_nothing_before_version():
    test_directory = 'nothing-before-version'
    run_test(test_directory)


def test_input_file_is_output_file():
    test_directory = 'input-file-is-output-file'
    args = ['cp',
            test_directory + '/in.glsl',
            test_directory + '/out.glsl']
    assert subprocess.run(args).returncode == 0
    args = ['python',
            '../precompiler.py',
            '-D',
            'A=1',
            '-D',
            'B=2',
            '-i',
            test_directory + '/out.glsl',
            '-o',
            test_directory + '/out.glsl']
    assert subprocess.run(args).returncode == 0
    assert filecmp.cmp(test_directory + '/out.glsl',
                       test_directory + '/expected-out.glsl')


def test_version_with_extra_comments():
    test_directory = 'version-with-extra-comments'
    run_test(test_directory)
