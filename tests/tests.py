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


def test_version():
    test_directory = 'version'
    run_test(test_directory)


def test_version_w_profile():
    test_directory = 'version-w-profile'
    run_test(test_directory)


def test_version_w_whitespace():
    test_directory = 'version-w-whitespace'
    run_test(test_directory)


def test_version_w_profile_w_whitespace():
    test_directory = 'version-w-profile-w-whitespace'
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


def test_commented_versions():
    test_directory = 'commented-versions'
    run_test(test_directory)


def test_commented_versions_and_version():
    test_directory = 'commented-versions-and-version-w-profile'
    run_test(test_directory)


def test_commented_versions_and_version_w_whitespace():
    test_directory = 'commented-versions-and-version-w-whitespace'
    run_test(test_directory)


def test_commented_versions_and_version_w_profile_w_whitespace():
    test_directory = 'commented-versions-and-version-w-profile-w-whitespace'
    run_test(test_directory)


def test_multiline_comment_after_version():
    test_directory = 'multiline-comment-after-version'
    run_test(test_directory)


def test_multiline_comment_after_version_w_profile():
    test_directory = 'multiline-comment-after-version-w-profile'
    run_test(test_directory)


def test_multiline_comment_after_version_w_whitespace():
    test_directory = 'multiline-comment-after-version-w-whitespace'
    run_test(test_directory)


def test_multiline_comment_after_version_w_profile_w_whitespace():
    test_directory = 'multiline-comment-after-version-w-profile-w-whitespace'
    run_test(test_directory)
