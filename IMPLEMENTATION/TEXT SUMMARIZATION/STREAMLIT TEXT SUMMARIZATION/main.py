import extractive.gensim_model as gensim_model
def main():
    print("Hello World")
    gettext = input("give text")
    getratio = input("give ratio")
    gensimobj = gensim_model.GensimClass()
    gensimobj.gensim_method(gettext,getratio)


if __name__ == '__main__':
    main()
