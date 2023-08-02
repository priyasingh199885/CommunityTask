#Extract  Metadata from a single Markdown File in JSON Format

import yaml
from typing import Dict, Any


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def find_yaml_block(content: str) -> str:
    start = content.find('---')
    if start == -1:
        raise ValueError('Unable to find start of YAML block')

    end = content.find('---', start + 3)
    if end == -1:
        raise ValueError('Unable to find end of YAML block')

    return content[start + 3:end].strip()


def parse_yaml(yaml_str: str) -> Dict[str, Any]:
    return yaml.load(yaml_str, Loader=yaml.SafeLoader)


def extract_metadata(file_path: str) -> Dict[str, Any]:
    try:
        content = read_file(file_path)
        yaml_str = find_yaml_block(content)
        metadata = parse_yaml(yaml_str)
    except Exception as e:
        raise RuntimeError("Unable to extract metadata.") from e

    return metadata


if __name__ == '__main__':
    try:
        metadata = extract_metadata('AI_Tooling.md')
        value = metadata.get('Date of Evaluation', 'default_value')
        print(value)
    except Exception as e:
        print(str(e))
