import unittest
import re
import Archive.RememberSpeakerDraft

#email=Archive.RememberSpeakerDraft.to
def valid_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


class TestEmailFormat(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(valid_email("test@example.com"), True)

    def test_email_without_at_symbol(self):
        self.assertEqual(valid_email("testexample.com"), False)

    def test_email_without_dot(self):
        self.assertEqual(valid_email("test@examplecom"), False)

    def test_email_without_domain(self):
        self.assertEqual(valid_email("test@.com"), False)

    def test_email_without_username(self):
        self.assertEqual(valid_email("@example.com"), False)


if __name__ == '__main__':
    unittest.main()