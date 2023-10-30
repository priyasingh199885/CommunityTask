def get_first_heading(raw_content):
    # Split the string into lines
    lines = raw_content[2].split('\n')

    # Iterate over the lines
    
    for line in lines:
        # If the line starts with '#', return it
        if line.strip().startswith('#'):
            return line.strip()

    # If no line starts with '#', return an empty string or None
    return ''

# Test with a markdown text
raw_content = ['', '', '# Heading\nThis is some text.\n## Subheading\nThis is some more text.']
print(get_first_heading(raw_content))