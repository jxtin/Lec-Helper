import wikipedia
from nltk.stem import WordNetLemmatizer
from yake import KeywordExtractor
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation


lemmatizer = WordNetLemmatizer()


def preprocessed_text(text_content):
    # remove punctuation
    text_content = text_content.translate(str.maketrans(" ", " ", punctuation))
    # remove stopwords
    stop_words = set(stopwords.words("english"))
    # remove words less than 3 characters
    words = word_tokenize(text_content)
    words = [w for w in words if len(w) > 2]
    # remove words in stopwords
    words = [w for w in words if not w in stop_words]
    # lemmatize words
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words)


def get_kw_and_wiki(filename="transcript.txt"):
    with open(filename, "r") as f:
        text_content = f.read()
    # two word keyphrase extraction
    kw_extractor = KeywordExtractor(lan="en", n=2, top=5)
    print(
        "Two word keyphrase:",
        (kwlist := kw_extractor.extract_keywords(text_content)),
    )

    kw2url = {}

    for kw in kwlist:
        print(kw)
        kw = kw[0]
        print(kw)
        try:
            wiki = wikipedia.page(kw)
            print(wiki.url)
            kw2url[kw] = wiki.url

        #         print(wiki.content)
        except Exception:
            kw2url[kw] = None
            pass
    
    return kw2url


if __name__ == "__main__":
    print(get_kw_and_wiki())
