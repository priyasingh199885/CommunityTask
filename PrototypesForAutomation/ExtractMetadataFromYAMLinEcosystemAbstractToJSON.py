import os

import yaml
import re
import json
from datetime import date
from ExtractKeyWordsFromMarkdownWithLLMSupport import extract_keywords_from_abstract

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_yaml_metadata(content, file_path):
    regex = r"```yaml(.*?)```"
    matches = re.findall(regex, content, re.DOTALL)
    if not matches:
        raise ValueError("Couldn't find any metadata.")
    metadata_text = matches[0]
    metadata_list = yaml.safe_load(metadata_text)
    metadata = {list(d.keys())[0]: list(d.values())[0] for d in metadata_list}

    # Extract title from content assuming that the title is the first line of your markdown file
    title = content.split('\n', 1)[0].lstrip('# ').strip()
    # Add title to metadata
    metadata["Title"] = title

    # Extract abstract from content assuming that it is placed between lines '## Abstract' and '## Speaker'
    abstract_regex = r'## Abstract\n(.*?)(?=\n##)'
    abstract_match = re.findall(abstract_regex, content, re.DOTALL)
    if abstract_match:
        abstract = abstract_match[0].strip()
        metadata["Abstract"] = abstract

    # determine the github link
    root_dir = 'C:\\Users\\D045584\\Ecosystem\\' # TODO needs to be adjust
    relative_path = os.path.relpath(file_path, root_dir).replace("\\","/")
    github_url = "https://github.tools.sap/CloudNativeCulture/Ecosystem/blob/main/" + relative_path
    keywords = extract_keywords_from_abstract(abstract, file_path)
    clean_metadata = {
        "Title": metadata.get("Title", ""),
        "GitHub Path": github_url,
        "Abstract": metadata.get("Abstract", ""),
        "Date of Evaluation": metadata.get("Date of Evaluation", ""),
        "Development Phase": metadata.get("Development Phase", ""),
        "Adoption Readiness": metadata.get("Adoption Readiness", ""),
        "Scopes": metadata.get("Scopes", ""),
        "Cluster": metadata.get("Topic Clusters", ""),
        "External Speaker": metadata.get("External Speaker", False),
        "Keywords": keywords }
    return clean_metadata

def extract_metadata_from_markdown(file_path):
    print('File Path' + file_path)
    markdown_content = load_file(file_path)
    metadata = None
    try:
     metadata = extract_yaml_metadata(markdown_content, file_path)
    except ValueError as e:
        print(str(e))
    if metadata:
#        json_metadata = convert_to_json(metadata)
#       print(json_metadata)
#        return json_metadata
        return metadata
def convert_to_json(metadata):
    return json.dumps(metadata, indent=4, cls=CustomJSONEncoder)

extract_metadata_from_markdown('./ExampleAbstractsFromEcosystem/ADAIntelligentSolutionDesignAndOperations.md')
