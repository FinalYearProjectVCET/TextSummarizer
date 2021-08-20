import extractive.gensim_model as gensim_model
import extractive.textrank_model as textrank_model

def main():
    print("Hello World")
    gettext = input("give text")
    getratio = input("give ratio")
    getmodel = input("give model")
    if getmodel == "gensim":
        gensimobj = gensim_model.GensimClass()
        gensimobj.gensim_method(gettext,getratio)
    elif getmodel == "textrank":
        gensimobj = textrank_model.TextRankClass()
        gensimobj.text_rank_method(gettext)

if __name__ == '__main__':
    main()