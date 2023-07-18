import unittest
import os
from datetime import datetime
from ExtractMetadataFromYAMLinEcosystemAbstractToJSON import load_file, extract_yaml_metadata, convert_to_json, CustomJSONEncoder

class TestExtractMetadata(unittest.TestCase):

    def setUp(self):
        self.test_file = "./ExampleAbstractsFromEcosystem/test_file.md"
        with open(self.test_file, "w") as f:
            f.write("```yaml\n- Date of Evaluation: 2023-07-17\n- External Speaker: False\n```\n\n# Title")

    def tearDown(self):
        os.remove(self.test_file)

    def test_load_file(self):
        content = load_file(self.test_file)
        self.assertIn("```yaml", content)
        self.assertIn("Date of Evaluation: 2023-07-17", content)

    def test_extract_metadata(self):
        content = load_file(self.test_file)
        metadata = extract_yaml_metadata(content)
        self.assertEqual(metadata["Date of Evaluation"], "2023-07-17")
        self.assertEqual(metadata["External Speaker"], False)

    def test_convert_to_json(self):
        content = load_file(self.test_file)
        metadata = extract_yaml_metadata(content)
        json_metadata = convert_to_json(metadata)
        self.assertIsInstance(json_metadata, str)

class TestCustomJsonEncoder(unittest.TestCase):

    def test_datetime_conversion(self):
        encoder = CustomJSONEncoder()
        date_obj = datetime.strptime("2023-07-17", "%Y-%m-%d").date()
        result = encoder.default(date_obj)
        self.assertEqual(result, "2023-07-17")

if __name__ == "__main__":
    unittest.main()
