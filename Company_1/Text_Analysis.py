import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

def process(text, tokenizer = TweetTokenizer(), stopwords = []):
    '''

    :param text:
    :param tokenizer:
    :param stopwords:
    :return:
    '''

    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return[tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

if __name__ == '__main__':
    fname = "Twitter_data_userlevel.jsonl"
    tweet_tokenizer = TweetTokenizer()
    punct = list(string.punctuation)
    stopwords_list = stopwords.words('english') + punct + ['rt','via','...']

    tf = Counter()
    with open(fname,"r") as fi:
        for line in fi:
            tweet = json.loads(line)
            tokens = process(text = tweet['text'], tokenizer=tweet_tokenizer, stopwords=stopwords_list)
            tf.update(tokens)
        for tag, count in tf.most_common(500):
            print("{} : {}".format(tag, count))

