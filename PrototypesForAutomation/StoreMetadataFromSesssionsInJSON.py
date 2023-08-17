#Store Aggregated Metadata for the Markdown Files of a Folder in JSON Format in a File in Python
#After running this code, you'll have a file named metadata_aggregate.json containing the aggregated metadata for the Markdown files in the specified folder.
import os
import json
from ExtractMetadataFromYAMLinEcosystemAbstractToJSON import extract_metadata_from_markdown
from ExtractMetadataFromYAMLinEcosystemAbstractToJSON import CustomJSONEncoder

# Set the folder path containing the markdown files
# folder_path = "C:/Users/D045584/Ecosystem/Sessions/PastSessions/2023"
# folder_path = "./ExampleAbstractsFromEcosystem"

folder_path = "C:/Users/D045584/Ecosystem/Sessions/PastSessions/2023"

# Read all the markdown files in the folder
markdown_files = [entry for entry in os.listdir(folder_path) if entry.endswith(".md")]

# Initialize an empty JSON object to store the metadata
metadata_aggregate = {}

# Extract metadata from each markdown file
for md_file in markdown_files:

    file_path = os.path.join(folder_path, md_file)
    metadata_dict = extract_metadata_from_markdown(file_path)

    # Store the metadata in the JSON object
    if metadata_dict is not None:
        metadata_aggregate[md_file] = metadata_dict

# Store the aggregated metadata in a JSON file
with open("metadata_aggregate.json", "w", encoding="utf-8") as json_file:
    json.dump(metadata_aggregate, json_file, ensure_ascii=False, indent=4, cls=CustomJSONEncoder)
