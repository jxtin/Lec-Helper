text_content = [
    """
In last section, examined early aspects memory. In section, we’re going discuss factors influence memory. So let’s beginning concept slide two, concept overlearning. Basically overlearning, idea continue study something recall perfectly. So study particular topic whatever topic is. When recall perfectly, continue study it. This classic way help one taking comprehensive finals later semester. So study exam one really know all, continue study it. That make comprehensive final easier. The next factor influence memory relates call organization. In general, organize material, recall better. There lots different types organizational strategies I’ve listed slide four. So let’s begin talking first organizational strategy called clustering located page five. In clustering, basically recall items better recognize two types things particular list. So let’s give couple lists show examples that. These examples shown slide six. Let’s say I give first list; north, cardinal, south, robin, east, wren, west, sparrow. Now recognize north, south, east west points compass cardinal, robin, wren sparrow birds, higher probability recalling material tried recall list order. The occurs second list located right hand side page six. So let’s list words well; pig, cat, horse, dog, sheep, birds, cow, fish. Now recognize two groups animals; one farm animals domestic companions, ala, pets, recall list material better tried recall list order. So again, another type example organizational strategy. Now organizational strategies one use well. The next one these, see slide seven, called verbal pneumonic techniques. In verbal pneumonic techniques, make organization many, many different types techniques. So let’s talk first slide eight called acrostics. In acrostics phrases first letter word functions cue help recall piece information. There variety different acrostics one uses. The famous relates saying: On Old Olympus Towering Tops A Fin And German Vented Some Hops. These relate twelve different cranial nerves within brain traditional medical student taking anatomy physiology, acrostic usually use remember them. Now verbal pneumonic techniques well. So let’s take look another one located slide 10. These called acronyms. Acronyms basically word formed first letters series words. A classic example acronym system ROY G BIV first letters colors visual spectrum. This classic acronym sensation perception students even introductory psych students learn memorize. Another verbal pneumonic technique shown slide 11 called Rhymes. The classic rhyme one learned grade school I E except C. So rhymes another way recall memorize information. So we’ve examined variety different verbal pneumonic techniques work. In next section, we’re going examine visual imagery types methods organize material. The first shown slide 13 called Method Loci. Basically involves taking kind imaginary walk along familiar path images you’re trying recall associated items locations along path. The classic example put material house. So close eyes think this. What happens walk back door? What’s first item see. Well first item see put first piece information want remember. Let’s say coat hook, hang something coat hook. Then continue kitchen. In kitchen, what’s first thing see? Well may refrigerator, identify second item you’re trying remember put refrigerator. Then open door refrigerator that’s put third item. And close refrigerator door look left there’s stove. So, put next item one burners stove items trying remember located within kitchen within house. Then you’re trying recall items exam, begin walk around house. So first thing think happens I walk back door lo behold, there’s first item I’m trying recall. Then I go refrigerator there’s second item. Then I open door refrigerator there’s third item I different materials I’m trying remember put exam. Now walking around house good place use method loci, places that’s even better. The better place try place information want learn location you’re going recall material. So sitting exam room you’re going take test putting things different objects within exam room good strategy. Especially one trying memorize lots lots different information places acts cue. So that’s first type visual imagery technique. Now second type visual imagery technique shown slide 14. This called pegword technique. The pegword technique relies list integers. What attach pegword numbers rhymes. The classic example One rhyming Bun, Two Shoe, Three Tree, Four Door on. Then see slide 15, you’re given list words recall, associate first word list peg word. For example word, let’s say you’re trying recall word “Bee” peg word bun. Well might try visualize bee eating great big bun. As result that, make associations. Furthermore, outrageous association, better recall particular item. So, let’s say might frog shoes on, horse knocking tree, whatever may information you’re trying recall.
""",
    """
    Electromagnetism is one of the fundamental forces of nature. Early on, electricity and magnetism were studied separately and regarded as separate phenomena. Hans Christian Ørsted discovered that the two were related – electric currents give rise to magnetism. Michael Faraday discovered the converse, that magnetism could induce electric currents, and James Clerk Maxwell put the whole thing together in a unified theory of electromagnetism. Maxwell's equations further indicated that electromagnetic waves existed, and the experiments of Heinrich Hertz confirmed this, making radio possible. Maxwell also postulated, correctly, that light was a form of electromagnetic wave, thus making all of optics a branch of electromagnetism. Radio waves differ from light only in that the wavelength of the former is much longer than the latter. Albert Einstein showed that the magnetic field arises through the relativistic motion of the electric field and thus magnetism is merely a side effect of electricity. The modern theoretical treatment of electromagnetism is as a quantum field in quantum electrodynamics.
""",
    """Sources tell us that Google is acquiring Kaggle, a platform that hosts data science and machine learning "\
"competitions. Details about the transaction remain somewhat vague, but given that Google is hosting its Cloud "\
"Next conference in San Francisco this week, the official announcement could come as early as tomorrow. "\
"Reached by phone, Kaggle co-founder CEO Anthony Goldbloom declined to deny that the acquisition is happening. "\
"Google itself declined 'to comment on rumors'. Kaggle, which has about half a million data scientists on its platform, "\
"was founded by Goldbloom  and Ben Hamner in 2010. "\
"The service got an early start and even though it has a few competitors like DrivenData, TopCoder and HackerRank, "\
"it has managed to stay well ahead of them by focusing on its specific niche. "\
"The service is basically the de facto home for running data science and machine learning competitions. "\
"With Kaggle, Google is buying one of the largest and most active communities for data scientists - and with that, "\
"it will get increased mindshare in this community, too (though it already has plenty of that thanks to Tensorflow "\
"and other projects). Kaggle has a bit of a history with Google, too, but that's pretty recent. Earlier this month, "\
"Google and Kaggle teamed up to host a $100,000 machine learning competition around classifying YouTube videos. "\
"That competition had some deep integrations with the Google Cloud Platform, too. Our understanding is that Google "\
"will keep the service running - likely under its current name. While the acquisition is probably more about "\
"Kaggle's community than technology, Kaggle did build some interesting tools for hosting its competition "\
"and 'kernels', too. On Kaggle, kernels are basically the source code for analyzing data sets and developers can "\
"share this code on the platform (the company previously called them 'scripts'). "\
"Like similar competition-centric sites, Kaggle also runs a job board, too. It's unclear what Google will do with "\
"that part of the service. According to Crunchbase, Kaggle raised $12.5 million (though PitchBook says it's $12.75) "\
"since its   launch in 2010. Investors in Kaggle include Index Ventures, SV Angel, Max Levchin, Naval Ravikant, "\
"Google chief economist Hal Varian, Khosla Ventures and Yuri Milner """,
]


from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from yake import KeywordExtractor


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
    return " ".join(words)


for text in text_content:
    text = preprocessed_text(text)

    # single word keyphrase extraction
    kw_extractor = KeywordExtractor(lan="en", n=1, top=5)
    print(
        "Single word keyphrase:",
        kw_extractor.extract_keywords(text),
    )

    # two word keyphrase extraction
    kw_extractor = KeywordExtractor(lan="en", n=2, top=5)
    print(
        "Two word keyphrase:",
        kw_extractor.extract_keywords(text),
    )

    # three word keyphrase extraction
    kw_extractor = KeywordExtractor(lan="en", n=3, top=5)
    print(
        "Three word keyphrase:",
        kw_extractor.extract_keywords(text),
    )

    from keybert import KeyBERT

    kw_extractor = KeyBERT("distilbert-base-nli-mean-tokens")
    print(
        "KeyBERT:",
        kw_extractor.extract_keywords(text, keyphrase_ngram_range=(0, 2), top_n=10),
    )

    # # single word keyphrase extraction
    # kw_extractor = KeyBERT("distilbert-base-nli-mean-tokens")
    # print(
    #     "Single word keyphrase:",
    #     kw_extractor.extract_keywords(
    #         text,
    #         keyphrase_length=1,
    #         stopwords="englishpreprocessed_
    # # two word keyphrase extraction
    # print(
    #     "Two word keyphrase:",
    #     kw_extractor.extract_keywords(
    #         text,
    #         keyphrase_length=2,
    #         stopwords="english",
    #     ),
    # )

    # # three word keyphrase extraction
    # print(
    #     "Three word keyphrase:",
    #     kw_extractor.extract_keywords(
    #         text,
    #         keyphrase_length=3,
    #         stopwords="english",
    #     ),
    # )
