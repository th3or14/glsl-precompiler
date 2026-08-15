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


def check_output(test_directory):
    assert filecmp.cmp(test_directory + '/out.glsl',
                       test_directory + '/expected-out.glsl')


def run_positive_test(test_directory):
    assert run_precompiler(test_directory).returncode == 0
    check_output(test_directory)


def run_negative_test(test_directory):
    assert run_precompiler(test_directory).returncode != 0
    check_output(test_directory)


def test_example_from_readme():
    test_directory = 'example-from-readme'
    run_positive_test(test_directory)


def test_nothing_before_and_after_version():
    test_directory = 'nothing-before-and-after-version'
    run_positive_test(test_directory)


def test_nothing_before_and_after_version_w_profile():
    test_directory = 'nothing-before-and-after-version-w-profile'
    run_positive_test(test_directory)


def test_nothing_before_and_after_version_w_whitespace():
    test_directory = 'nothing-before-and-after-version-w-whitespace'
    run_positive_test(test_directory)


def test_nothing_before_and_after_version_w_profile_w_whitespace():
    test_directory = 'nothing-before-and-after-version-w-profile-w-whitespace'
    run_positive_test(test_directory)


def test_nothing_before_version():
    test_directory = 'nothing-before-version'
    run_positive_test(test_directory)


def test_nothing_before_version_w_profile():
    test_directory = 'nothing-before-version-w-profile'
    run_positive_test(test_directory)


def test_nothing_before_version_w_whitespace():
    test_directory = 'nothing-before-version-w-whitespace'
    run_positive_test(test_directory)


def test_nothing_before_version_w_profile_w_whitespace():
    test_directory = 'nothing-before-version-w-profile-w-whitespace'
    run_positive_test(test_directory)


def test_nothing_after_version():
    test_directory = 'nothing-after-version'
    run_positive_test(test_directory)


def test_nothing_after_version_w_profile():
    test_directory = 'nothing-after-version-w-profile'
    run_positive_test(test_directory)


def test_nothing_after_version_w_whitespace():
    test_directory = 'nothing-after-version-w-whitespace'
    run_positive_test(test_directory)


def test_nothing_after_version_w_profile_w_whitespace():
    test_directory = 'nothing-after-version-w-profile-w-whitespace'
    run_positive_test(test_directory)


def test_multiple_versions():
    test_directory = 'multiple-versions'
    run_positive_test(test_directory)


def test_multiple_versions_w_profile():
    test_directory = 'multiple-versions-w-profile'
    run_positive_test(test_directory)


def test_multiple_versions_w_whitespace():
    test_directory = 'multiple-versions-w-whitespace'
    run_positive_test(test_directory)


def test_multiple_versions_w_profile_w_whitespace():
    test_directory = 'multiple-versions-w-profile-w-whitespace'
    run_positive_test(test_directory)


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
    check_output(test_directory)


def test_commented_versions_and_version():
    test_directory = 'commented-versions-and-version'
    run_positive_test(test_directory)


def test_commented_versions_and_version_w_profile():
    test_directory = 'commented-versions-and-version-w-profile'
    run_positive_test(test_directory)


def test_commented_versions_and_version_w_whitespace():
    test_directory = 'commented-versions-and-version-w-whitespace'
    run_positive_test(test_directory)


def test_commented_versions_and_version_w_profile_w_whitespace():
    test_directory = 'commented-versions-and-version-w-profile-w-whitespace'
    run_positive_test(test_directory)


def test_multiline_comment_after_version():
    test_directory = 'multiline-comment-after-version'
    run_positive_test(test_directory)


def test_multiline_comment_after_version_w_profile():
    test_directory = 'multiline-comment-after-version-w-profile'
    run_positive_test(test_directory)


def test_multiline_comment_after_version_w_whitespace():
    test_directory = 'multiline-comment-after-version-w-whitespace'
    run_positive_test(test_directory)


def test_multiline_comment_after_version_w_profile_w_whitespace():
    test_directory = 'multiline-comment-after-version-w-profile-w-whitespace'
    run_positive_test(test_directory)


def test_multiline_comment_before_version():
    test_directory = 'multiline-comment-before-version'
    run_positive_test(test_directory)


def test_multiline_comment_before_version_w_profile():
    test_directory = 'multiline-comment-before-version-w-profile'
    run_positive_test(test_directory)


def test_multiline_comment_before_version_w_whitespace():
    test_directory = 'multiline-comment-before-version-w-whitespace'
    run_positive_test(test_directory)


def test_multiline_comment_before_version_w_profile_w_whitespace():
    test_directory = 'multiline-comment-before-version-w-profile-w-whitespace'
    run_positive_test(test_directory)


def test_version_profile_is_nondefault_compatibility():
    test_directory = 'version-profile-is-nondefault-compatibility'
    run_positive_test(test_directory)


def test_version_profile_is_nondefault_es():
    test_directory = 'version-profile-is-nondefault-es'
    run_positive_test(test_directory)


def test_only_commented_versions():
    test_directory = 'only-commented-versions'
    run_negative_test(test_directory)


def test_only_commented_versions_w_profile():
    test_directory = 'only-commented-versions-w-profile'
    run_negative_test(test_directory)


def test_only_commented_versions_w_whitespace():
    test_directory = 'only-commented-versions-w-whitespace'
    run_negative_test(test_directory)


def test_only_commented_versions_w_profile_w_whitespace():
    test_directory = 'only-commented-versions-w-profile-w-whitespace'
    run_negative_test(test_directory)


def test_empty_input_file():
    test_directory = 'empty-input-file'
    run_negative_test(test_directory)


def test_main_after_version():
    test_directory = 'main-after-version'
    run_positive_test(test_directory)


def test_main_after_version_w_profile():
    test_directory = 'main-after-version-w-profile'
    run_positive_test(test_directory)


def test_main_after_version_w_whitespace():
    test_directory = 'main-after-version-w-whitespace'
    run_positive_test(test_directory)


def test_main_after_version_w_profile_w_whitespace():
    test_directory = 'main-after-version-w-profile-w-whitespace'
    run_positive_test(test_directory)


def test_nothing_before_and_after_main():
    test_directory = 'nothing-before-and-after-main'
    run_negative_test(test_directory)
