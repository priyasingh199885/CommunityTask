import unittest
import tempfile
import os
import string
from collections import Counter
from unittest.mock import patch
from ExtractKeyWordsFromMarkdown import extract_text, tokenize_text, remove_stopwords, extract_keywords, print_keywords, markdown_pattern
import unittest
import tempfile
import os
import os
from collections import Counter
from unittest.mock import patch
import ExtractKeyWordsFromMarkdown as test_module

class TestExtractText(unittest.TestCase):

    def test_extract_text(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(b"Hello *world!\nThis is a_ [test](http://example.com) #file.")
        temp_file.close()
        result = test_module.extract_text(temp_file.name)
        os.unlink(temp_file.name)
        self.assertEqual(result, "Hello world!\nThis is a test file.")

class TestTokenizeText(unittest.TestCase):

    def test_tokenize_text(self):
        text = "This is a sample text 123!"
        result = test_module.tokenize_text(text)
        expected_result = ["this", "is", "a", "sample", "text", "123"]
        self.assertEqual(result, expected_result)

class TestRemoveStopwords(unittest.TestCase):

    def test_remove_stopwords(self):
        words = ["this", "is", "a", "sample", "text", "123"]
        result = test_module.remove_stopwords(words)
        expected_result = ['sample', 'text', '123']
        self.assertEqual(result, expected_result)

class TestExtractKeywords(unittest.TestCase):

    def test_extract_keywords(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(b"Hello *world.\nThis is a_ [test](http://example.com) #file.")
        temp_file.close()

        with patch("test_module.print_keywords") as mocked_print_keywords:
             test_module.extract_keywords(temp_file.name)

        _, mock_keywords = mocked_print_keywords.call_args
        os.unlink(temp_file.name)

        text = "Hello world. This is a test file."
        words = test_module.tokenize_text(text)
        words = test_module.remove_stopwords(words)
        expected_keywords = Counter(words).most_common(10)

        self.assertListEqual(mock_keywords[0], expected_keywords)

class TestPrintKeywords(unittest.TestCase):

    @patch(test_module.print_keywords)
    def test_print_keywords(self, mocked_print_keywords):
        keywords = [("hello", 3), ("world", 2), ("sample", 1)]

        mocked_print_keywords.return_value = None
        with patch("builtins.print") as mocked_print:
            test_module.print_keywords(keywords)

        mocked_print.assert_any_call("Keywords extracted (unordered):")
        for keyword, freq in keywords:
            mocked_print.assert_any_call(f"- {keyword}")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
