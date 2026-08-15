import filecmp
import subprocess
import unittest


class TestPrecompiler(unittest.TestCase):

    def run_precompiler(self, test_directory):
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

    def check_output(self, test_directory):
        self.assertTrue(filecmp.cmp(test_directory + '/out.glsl',
                                    test_directory + '/expected-out.glsl'))

    def run_positive_test(self, test_directory):
        self.assertEqual(self.run_precompiler(test_directory).returncode, 0)
        self.check_output(test_directory)

    def run_negative_test(self, test_directory):
        self.assertNotEqual(self.run_precompiler(test_directory).returncode, 0)
        self.check_output(test_directory)

    def test_example_from_readme(self):
        test_directory = 'example-from-readme'
        self.run_positive_test(test_directory)

    def test_nothing_before_and_after_version(self):
        test_directory = 'nothing-before-and-after-version'
        self.run_positive_test(test_directory)

    def test_nothing_before_and_after_version_w_profile(self):
        test_directory = 'nothing-before-and-after-version-w-profile'
        self.run_positive_test(test_directory)

    def test_nothing_before_and_after_version_w_whitespace(self):
        test_directory = 'nothing-before-and-after-version-w-whitespace'
        self.run_positive_test(test_directory)

    def test_nothing_before_and_after_version_w_profile_w_whitespace(self):
        test_directory = 'nothing-before-and-after-version-w-profile-w-whitespace'
        self.run_positive_test(test_directory)

    def test_nothing_before_version(self):
        test_directory = 'nothing-before-version'
        self.run_positive_test(test_directory)

    def test_nothing_before_version_w_profile(self):
        test_directory = 'nothing-before-version-w-profile'
        self.run_positive_test(test_directory)

    def test_nothing_before_version_w_whitespace(self):
        test_directory = 'nothing-before-version-w-whitespace'
        self.run_positive_test(test_directory)

    def test_nothing_before_version_w_profile_w_whitespace(self):
        test_directory = 'nothing-before-version-w-profile-w-whitespace'
        self.run_positive_test(test_directory)

    def test_nothing_after_version(self):
        test_directory = 'nothing-after-version'
        self.run_positive_test(test_directory)

    def test_nothing_after_version_w_profile(self):
        test_directory = 'nothing-after-version-w-profile'
        self.run_positive_test(test_directory)

    def test_nothing_after_version_w_whitespace(self):
        test_directory = 'nothing-after-version-w-whitespace'
        self.run_positive_test(test_directory)

    def test_nothing_after_version_w_profile_w_whitespace(self):
        test_directory = 'nothing-after-version-w-profile-w-whitespace'
        self.run_positive_test(test_directory)

    def test_multiple_versions(self):
        test_directory = 'multiple-versions'
        self.run_positive_test(test_directory)

    def test_multiple_versions_w_profile(self):
        test_directory = 'multiple-versions-w-profile'
        self.run_positive_test(test_directory)

    def test_multiple_versions_w_whitespace(self):
        test_directory = 'multiple-versions-w-whitespace'
        self.run_positive_test(test_directory)

    def test_multiple_versions_w_profile_w_whitespace(self):
        test_directory = 'multiple-versions-w-profile-w-whitespace'
        self.run_positive_test(test_directory)

    def test_input_file_is_output_file(self):
        test_directory = 'input-file-is-output-file'
        args = ['cp',
                test_directory + '/in.glsl',
                test_directory + '/out.glsl']
        self.assertEqual(subprocess.run(args).returncode, 0)
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
        self.assertEqual(subprocess.run(args).returncode, 0)
        self.check_output(test_directory)

    def test_commented_versions_and_version(self):
        test_directory = 'commented-versions-and-version'
        self.run_positive_test(test_directory)

    def test_commented_versions_and_version_w_profile(self):
        test_directory = 'commented-versions-and-version-w-profile'
        self.run_positive_test(test_directory)

    def test_commented_versions_and_version_w_whitespace(self):
        test_directory = 'commented-versions-and-version-w-whitespace'
        self.run_positive_test(test_directory)

    def test_commented_versions_and_version_w_profile_w_whitespace(self):
        test_directory = 'commented-versions-and-version-w-profile-w-whitespace'
        self.run_positive_test(test_directory)

    def test_multiline_comment_after_version(self):
        test_directory = 'multiline-comment-after-version'
        self.run_positive_test(test_directory)

    def test_multiline_comment_after_version_w_profile(self):
        test_directory = 'multiline-comment-after-version-w-profile'
        self.run_positive_test(test_directory)

    def test_multiline_comment_after_version_w_whitespace(self):
        test_directory = 'multiline-comment-after-version-w-whitespace'
        self.run_positive_test(test_directory)

    def test_multiline_comment_after_version_w_profile_w_whitespace(self):
        test_directory = 'multiline-comment-after-version-w-profile-w-whitespace'
        self.run_positive_test(test_directory)

    def test_multiline_comment_before_version(self):
        test_directory = 'multiline-comment-before-version'
        self.run_positive_test(test_directory)

    def test_multiline_comment_before_version_w_profile(self):
        test_directory = 'multiline-comment-before-version-w-profile'
        self.run_positive_test(test_directory)

    def test_multiline_comment_before_version_w_whitespace(self):
        test_directory = 'multiline-comment-before-version-w-whitespace'
        self.run_positive_test(test_directory)

    def test_multiline_comment_before_version_w_profile_w_whitespace(self):
        test_directory = 'multiline-comment-before-version-w-profile-w-whitespace'
        self.run_positive_test(test_directory)

    def test_version_profile_is_nondefault_compatibility(self):
        test_directory = 'version-profile-is-nondefault-compatibility'
        self.run_positive_test(test_directory)

    def test_version_profile_is_nondefault_es(self):
        test_directory = 'version-profile-is-nondefault-es'
        self.run_positive_test(test_directory)

    def test_only_commented_versions(self):
        test_directory = 'only-commented-versions'
        self.run_negative_test(test_directory)

    def test_only_commented_versions_w_profile(self):
        test_directory = 'only-commented-versions-w-profile'
        self.run_negative_test(test_directory)

    def test_only_commented_versions_w_whitespace(self):
        test_directory = 'only-commented-versions-w-whitespace'
        self.run_negative_test(test_directory)

    def test_only_commented_versions_w_profile_w_whitespace(self):
        test_directory = 'only-commented-versions-w-profile-w-whitespace'
        self.run_negative_test(test_directory)

    def test_empty_input_file(self):
        test_directory = 'empty-input-file'
        self.run_negative_test(test_directory)

    def test_main_after_version(self):
        test_directory = 'main-after-version'
        self.run_positive_test(test_directory)

    def test_main_after_version_w_profile(self):
        test_directory = 'main-after-version-w-profile'
        self.run_positive_test(test_directory)

    def test_main_after_version_w_whitespace(self):
        test_directory = 'main-after-version-w-whitespace'
        self.run_positive_test(test_directory)

    def test_main_after_version_w_profile_w_whitespace(self):
        test_directory = 'main-after-version-w-profile-w-whitespace'
        self.run_positive_test(test_directory)

    def test_nothing_before_and_after_main(self):
        test_directory = 'nothing-before-and-after-main'
        self.run_negative_test(test_directory)
