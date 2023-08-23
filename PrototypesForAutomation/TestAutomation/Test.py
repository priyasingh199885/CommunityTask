import unittest

import unittest


class TestYourScript(unittest.TestCase):
    def setUp(self):
        self.github_object = Invitation

    def test_github_access(self):
        # replace 'your_repo_address' with the correct info
        result = self.github_object.access_github('your_repo_address')
        self.assertEqual(result.status_code, 200)

    def test_read_md_files(self):
        # Replace 'read_md_files()' with the correct function name.
        result = self.github_object.read_md_files()
        self.assertIsNotNone(result)

    def test_check_invitations(self):
        dummy_yaml_info = {'invitation-sent': False}
        # Replace 'check_invitation()' with the correct function name.
        result = self.github_object.check_invitation(dummy_yaml_info)
        self.assertTrue(result)

    def test_email_draft_creation(self):
        dummy_yaml_info = {'invitation-sent': False}
        # Replace 'create_email_draft()' with the correct function name.
        result = self.github_object.create_email_draft(dummy_yaml_info)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
