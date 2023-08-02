import unittest
import os
from datetime import date

from ExtractMetadataFromMarkdownFile import read_file, find_yaml_block, parse_yaml, extract_metadata

class TestExtractMetadataFunctions(unittest.TestCase):

    def setUp(self) -> None:
        # Create a temporary Markdown file for testing
        self.test_md_file = 'test_markdown.md'
        with open(self.test_md_file, 'w') as f:
            f.write("""---
title: Test Markdown
author: Jane Doe
date: 2022-01-01
tags:
  - tag1
  - tag2
  - tag3
---
# Test Markdown File
This is a test Markdown file with YAML metadata.
""")

    def tearDown(self) -> None:
        # Remove the temporary Markdown file
        os.remove(self.test_md_file)

    def test_read_file(self) -> None:
        content = read_file(self.test_md_file)
        self.assertIsInstance(content, str)
        self.assertIn('Test Markdown File', content)

    def test_find_yaml_block(self) -> None:
        content = read_file(self.test_md_file)
        yaml_block = find_yaml_block(content)
        self.assertIsInstance(yaml_block, str)
        self.assertIn('title: Test Markdown', yaml_block)

    def test_parse_yaml(self) -> None:
        yaml_str = """---
title: Test Markdown
author: Jane Doe
date: 2022-01-01
tags:
  - tag1
  - tag2
  - tag3
---
"""
        expected_output = {
            'title': 'Test Markdown',
            'author': 'Jane Doe',
            'date': '2022-01-01',
            'tags': ['tag1', 'tag2', 'tag3']
        }
        parsed_data = parse_yaml(yaml_str)
        self.assertDictEqual(parsed_data, expected_output)

    def test_extract_metadata(self) -> None:
        expected_output = {
            'title': 'Test Markdown',
            'author': 'Jane Doe',
            'date': date(2022, 1, 1),
            'tags': ['tag1', 'tag2', 'tag3']
        }
        metadata = extract_metadata(self.test_md_file)
        self.assertDictEqual(metadata, expected_output)


if __name__ == '__main__':
    unittest.main()
