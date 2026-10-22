import nltk
from nltk.tokenize import sent_tokenize # for later tasks (sentence analysis)
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from collections import Counter

def read_text(file_path: str) -> str:
    """Reads the text from the given file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def tokenize_words(text: str) -> list[str]:
    """Splits the text into word tokens."""
    try:
        return word_tokenize(text)
    except LookupError:
        nltk.download('punkt_tab', quiet=True)
        return word_tokenize(text)

def normalize_tokens(tokens: list[str]) -> list[str]:
    """Converts all tokens to lowercase."""
    return [t.lower() for t in tokens]

def remove_stopwords(tokens: list[str]) -> list[str]:
    """Removes English stopwords and non-alphabetic tokens."""
    try:
        stop_words = set(stopwords.words("english"))
    except LookupError:
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words("english"))

    return [
        word for word in tokens
        if word not in stop_words and word.isalpha() #word not in string.punctuation
    ]

def count_words(tokens: list[str]) -> dict[str, int]:
    """Returns a dictionary {word: count}."""
    return dict(Counter(tokens)) #.most_common()
    # word_frequency = {}
    # for wort in text_fur_count:
    #     if wort in word_frequency:
    #         word_frequency[wort] += 1
    #     else:
    #         word_frequency[wort] = 1
    # return word_frequency


def main() -> None:
    """Main function."""
    
    file_path = "velpTEC_K4.0070_3.0_Projektarbeit_Python_ClimateScienceText.txt"

    try:
        text = read_text(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except UnicodeDecodeError:
        print(f"Error: File '{file_path}' could not be read as UTF-8.")
        return
    tokens = tokenize_words(text)
    normalized = normalize_tokens(tokens)
    filtered_tokens = remove_stopwords(normalized)
    print(filtered_tokens)
    word_frequency = count_words(filtered_tokens)
    print(word_frequency)



if __name__ == "__main__":
    main()