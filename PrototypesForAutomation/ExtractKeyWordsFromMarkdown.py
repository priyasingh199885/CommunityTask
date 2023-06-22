import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from collections import Counter




# Load the nltk stopwords and the 'punkt' tokenizer
nltk.download("stopwords")
nltk.download("punkt")


# Define a regex pattern for matching markdown elements
markdown_pattern = re.compile("([*_\[\]()#])")


def extract_text(markdown_file):
    with open(markdown_file, "r") as file:
        content = file.read()
    content = re.sub(markdown_pattern, "", content)
    return content


def tokenize_text(text):
    words = word_tokenize(text)
    word_tokens = [word.lower() for word in words if word.isalnum()]
    return word_tokens


def remove_stopwords(words):
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def extract_keywords(filepath, num_keywords=10):
    text = extract_text(filepath)
    words = tokenize_text(text)
    words = remove_stopwords(words)

    keywords = Counter(words).most_common(num_keywords)
    print_keywords(keywords)

def print_keywords(keywords):
    print("Keywords extracted (unordered):")
    for keyword, freq in keywords:
        print(f"- {keyword}")

#--------- Usage ----------#

filepath = "CleanCode.md"  # Replace this with the path to your markdown document
num_keywords = 10  # Change this number to show a different number of keywords
extract_keywords(filepath, num_keywords)
