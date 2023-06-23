import unittest
import os
import json
from ExtractMetadataFromMarkdownFile import extract_metadata

class TestMarkdownMetadataAggregator(unittest.TestCase):

    def setUp(self):
        self.folder_path = "."
        self.markdown_files = [entry for entry in os.listdir(self.folder_path) if entry.endswith(".md")]

    def test_metadata_aggregate(self):
        metadata_aggregate = {}

        for md_file in self.markdown_files:
            file_path = os.path.join(self.folder_path, md_file)
            metadata_dict = extract_metadata(file_path)

            # convert datetime to string
            date_of_evaluation = metadata_dict['Date of Evaluation'].strftime("%Y-%m-%d")
            metadata_dict['Date of Evaluation'] = date_of_evaluation

            # Store the metadata in the JSON object
            metadata_aggregate[md_file] = metadata_dict

        # Save metadata_aggregate to a temporary JSON file
        with open("temp_metadata_aggregate.json", "w", encoding="utf-8") as json_file:
            json.dump(metadata_aggregate, json_file, ensure_ascii=False, indent=4)

        # Read temporary JSON file and compare with metadata_aggregate
        with open("temp_metadata_aggregate.json", "r", encoding="utf-8") as json_file:
            loaded_metadata_aggregate = json.load(json_file)

        # Assert the equality of the two metadata aggregations
        self.assertEqual(metadata_aggregate, loaded_metadata_aggregate)

        # Clean up temporary JSON file
        os.remove("temp_metadata_aggregate.json")

if __name__ == '__main__':
    unittest.main()
