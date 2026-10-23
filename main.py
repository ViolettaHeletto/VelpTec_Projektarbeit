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

def lowercase_tokens(tokens: list[str]) -> list[str]:
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

def normalize_max_frequency(word_counts: dict[str, int]) ->dict[str, float]:

    max_frequency = max(word_counts.values())
    normalize_dict = {}
    if not word_counts:
        return {}
    for word, count in word_counts.items():
        normalize_dict[word] = count/max_frequency
    return normalize_dict

def tokenize_sentences(text: str) -> list[str]:
    """Splits the text into sentences tokens."""
    try:
        return sent_tokenize(text)
    except LookupError:
        nltk.download('punkt_tab', quiet=True)
        return sent_tokenize(text)

def sentence_score(sentence: str, normalized_counts: dict[str, float]) -> float:
    value = 0.0
    words = word_tokenize(sentence.lower())
    for word in words:
        if word in normalized_counts:
            value += normalized_counts.get(word, 0.0)
    return value

def prozent_of_text(values: list[float], prozent: float = 20.0):
    x = max(1, int(len(values) * prozent / 100))
    return sorted(values, reverse=True)[:x]

def summary_output(sentences_with_value: list[tuple[str, float]], value: float):
    summary_sentences = []
    for sentence, score in sentences_with_value:
        if score in value:
            summary_sentences.append(sentence)
    return summary_sentences


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
    normalized = lowercase_tokens(tokens)
    filtered_tokens = remove_stopwords(normalized)
    #print(filtered_tokens)
    word_frequency = count_words(filtered_tokens)
    #print(word_frequency)
    normalized_counts = normalize_max_frequency(word_frequency)

    sentence_list = tokenize_sentences(text)
    weight_of_sentence = []
    for sentence in sentence_list:
        weight_of_sentence.append(sentence_score(sentence, normalized_counts))

    scored_sentences = [
    (sentence, sentence_score(sentence, normalized_counts))
    for sentence in sentence_list]
    print(scored_sentences)

    prozent = prozent_of_text(weight_of_sentence, 20.0)
    print(prozent)

    print(summary_output(scored_sentences, prozent))


if __name__ == "__main__":
    main()