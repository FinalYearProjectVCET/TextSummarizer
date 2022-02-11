import urllib
from bs4 import BeautifulSoup
from nltk import text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

class RuleBased:

    def rule_summarize(self,text, n):
        no = int(n)
        sents = sent_tokenize(text)
        
        assert no <= len(sents)
        word_sent = word_tokenize(text.lower())
        _stopwords = set(stopwords.words('english') + list(punctuation))
        
        word_sent=[word for word in word_sent if word not in _stopwords]
        freq = FreqDist(word_sent)
        
        
        ranking = defaultdict(int)
        
        for i,sent in enumerate(sents):
            for w in word_tokenize(sent.lower()):
                if w in freq:
                    ranking[i] += freq[w]
                
            
        sents_idx = nlargest(no, ranking, key=ranking.get)
        return [sents[j] for j in sorted(sents_idx)]