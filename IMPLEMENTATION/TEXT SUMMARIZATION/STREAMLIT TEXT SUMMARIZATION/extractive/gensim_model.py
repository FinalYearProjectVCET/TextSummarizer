import gensim 

class Gensim_Class:

    def gensim_method(taketext,takeratio):
        
        text = taketext
        givenratio = takeratio
        lengthtext=len(text)
        summarized_content = gensim.summarization.summarize(text, ratio=givenratio)
        print(summarized_content)
        lengthsumm = len(summarized_content)
        return summarized_content,lengthsumm,lengthtext