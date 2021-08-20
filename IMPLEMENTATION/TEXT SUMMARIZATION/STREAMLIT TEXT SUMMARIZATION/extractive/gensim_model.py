import gensim 

class GensimClass:

    def gensim_method(self,taketext,takeratio):
        
        text = taketext
        givenratio = float(takeratio)
        lengthtext=len(text)
        # print(type(givenratio))
        summarized_content = gensim.summarization.summarize(text, ratio=givenratio)
        print(summarized_content)
        lengthsumm = len(summarized_content)
        # print(lengthtext)
        # print(lengthsumm)
        return summarized_content,lengthsumm,lengthtext