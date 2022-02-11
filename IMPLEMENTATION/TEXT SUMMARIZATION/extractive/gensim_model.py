import gensim 

class GensimClass:

    def gensim_method(self,taketext,takeratio):
        text = taketext
        givenratio = float(takeratio)
        lengthtext=len(text)
        summarized_content = gensim.summarization.summarize(text, ratio=givenratio)
        print(type(summarized_content))
        return summarized_content