import extractive.gensim_model as gensim_model
import extractive.textrank_model as textrank_model
import extractive.pegasus_model as pegasus_model

def main():
    print("Hello World")
    gettext = input("give text")
    getratio = input("give ratio")
    getmodel = input("give model")
    if getmodel == "gensim":
        obj = gensim_model.GensimClass()
        summarized_content = obj.gensim_method(gettext,getratio)
        print(summarized_content)
    elif getmodel == "textrank":
        obj = textrank_model.TextRankClass()
        summarized_content =  obj.text_rank_method(gettext)
        print(summarized_content)
    elif getmodel == "pegasusext":
        obj = pegasus_model.PegasusClass()
        obj.xlargeModel()
        summarized_content = obj.predictText(gettext)
        print(summarized_content)
if __name__ == '__main__':
    main()