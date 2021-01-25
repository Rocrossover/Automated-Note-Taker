
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 50

# url = "https://en.wikipedia.org/wiki/Automatic_summarization"
# parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
# or for plain text files
parser = PlaintextParser.from_file("sample.txt", Tokenizer(LANGUAGE))
# parser = PlaintextParser.from_string("Check this out.", Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)
f = open("sample_output.txt","w")

for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    print(sentence, file=f)

f.close()