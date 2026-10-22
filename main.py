from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

def read_text(file_path: str) -> str:
    """Liest den Text aus der angegebenen Datei."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def wort_tokenize_text(text):
    words = word_tokenize(text)
    return words

def remove_stopwords():
    return None 

def count_words():
    return None


def main() -> None:
    """Hauptfunktion"""
    
    file_path = "velpTEC_K4.0070_3.0_Projektarbeit_Python_ClimateScienceText.txt"

    try:
        bearbeitender_text = read_text(file_path)
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{file_path}' wurde nicht gefunden.")
        return
    except UnicodeDecodeError:
        print(f"Fehler: Die Datei '{file_path}' konnte nicht als UTF-8 gelesen werden.")
        return
    worter = wort_tokenize_text(bearbeitender_text)


if __name__ == "__main__":
    main()



# text = "NLTK is a great NLP toolkit. It makes processing text easy!"
# #splits a string into a list of sentences, handling punctuation and abbreviations.
# sentences = sent_tokenize(text)
# print(sentences)



# sentence = "Tokenization is easy with NLTK's word_tokenize."
# words = word_tokenize(sentence)
# print(words)