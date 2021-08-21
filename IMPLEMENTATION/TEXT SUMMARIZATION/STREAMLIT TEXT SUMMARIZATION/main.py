import extractive.gensim_model as gensim_model
import extractive.textrank_model as textrank_model
import extractive.pegasus_model as pegasus_model
import abstractive.pegasus_head as pegasus_head
import abstractive.pegasus_summ as pegasus_summ
import extractive.rulebased_model as rulebased_model


def getInput():
    return input("Enter your text : ")


# def abstractiveSummarization(input_text):
#     back = False
#     while(True):
#         print("\nABSTRACTIVE SUMMARIZATION TECHNIQUES : ")
#         print("1] PEGASUS HEAD")
#         print("2] PEGASUS SUMMARY")

#         print("\nPress 0 to go back.")
#         print("Press -1 to exit.")

#         summarization_technique = int(
#             input("\nSELECT SUMMARIZATION TECHNIQUE : "))
#         if(summarization_technique == -1):
#             break
#         elif(summarization_technique == 0):
#             back = True
#             break
#         elif(summarization_technique == 1):
#             obj = pegasus_head.PegasusClass()
#             obj.xsumModel()
#             summarized_content = obj.predictText(input_text)
#             print(summarized_content)
#         elif(summarization_technique == 2):
#             obj = pegasus_summ.PegasusClass()
#             obj.redditTifuModel()
#             summarized_content = obj.predictText(input_text)
#             print(summarized_content)

#     if(back):
#         break


# def extractiveSummarization(input_text):

#     back = False
#     while(True):
#         print("\nEXTRACTIVE SUMMARIZATION TECHNIQUES : ")
#         print("1] GENSIM")
#         print("2] RULE BASED")
#         print("3] TEXT RANK")
#         print("4] PEGASUS")
#         print("\nPress 0 to go back.")
#         print("Press -1 to exit.")

#         summarization_technique = int(
#             input("\nSELECT SUMMARIZATION TECHNIQUE : "))
#         if(summarization_technique == -1):
#             break
#         elif(summarization_technique == 0):
#             back = True
#             break
#         elif(summarization_technique == 1):
#             input_ratio = input(
#                 "RATIO OF TEXT TO BE SUMMARIZED (BETWEEN 0 AND 1) : ")
#             obj = gensim_model.GensimClass()
#             summarized_content = obj.gensim_method(input_text, input_ratio)
#             print(summarized_content)
#         elif(summarization_technique == 2):
#             num = input("GIVE NUM : ")
#             obj = rulebased_model.RuleBased()
#             summarized_content = obj.rule_summarize(input_text, num)
#             print(summarized_content)
#         elif(summarization_technique == 3):
#             obj = textrank_model.TextRankClass()
#             summarized_content = obj.text_rank_method(input_text)
#             print(summarized_content)
#         elif(summarization_technique == 4):
#             obj = pegasus_model.PegasusClass()
#             obj.xlargeModel()
#             summarized_content = obj.predictText(input_text)
#             print(summarized_content)

#     if(back):
#         break


def main():
    print("\n*-*-*-*-*-*-*-*-*-*TEXT SUMMARIZATION*-*-*-*-*-*-*-*-*-*\n")

    while(True):
        input_text = getInput()
        # takeInput = False
        while(True):
            print("\nSUMMARIZATION TYPES")
            print("1] ABSTRACTIVE")
            print("2] EXTRACTIVE")

            print("\nPress 0 to go back.")
            print("Press -1 to exit.")
            summarization_type = int(input("\nSELECT SUMMARIZATION TYPE : "))

            if(summarization_type == -1):
                break
            elif(summarization_type == 0):
                continue
            elif(summarization_type == 1):
                back = False
                while(True):
                    print("\nABSTRACTIVE SUMMARIZATION TECHNIQUES : ")
                    print("1] PEGASUS HEAD")
                    print("2] PEGASUS SUMMARY")

                    print("\nPress 0 to go back.")
                    print("Press -1 to exit.")

                    summarization_technique = int(
                        input("\nSELECT SUMMARIZATION TECHNIQUE : "))
                    if(summarization_technique == -1):
                        break
                    elif(summarization_technique == 0):
                        back = True
                        break
                    elif(summarization_technique == 1):
                        obj = pegasus_head.PegasusClass()
                        obj.xsumModel()
                        summarized_content = obj.predictText(input_text)
                        print(summarized_content)
                    elif(summarization_technique == 2):
                        obj = pegasus_summ.PegasusClass()
                        obj.redditTifuModel()
                        summarized_content = obj.predictText(input_text)
                        print(summarized_content)

                if(back):
                    continue
            elif(summarization_type == 2):
                back = False
                while(True):
                    print("\nEXTRACTIVE SUMMARIZATION TECHNIQUES : ")
                    print("1] GENSIM")
                    print("2] RULE BASED")
                    print("3] TEXT RANK")
                    print("4] PEGASUS")
                    print("\nPress 0 to go back.")
                    print("Press -1 to exit.")

                    summarization_technique = int(
                        input("\nSELECT SUMMARIZATION TECHNIQUE : "))
                    if(summarization_technique == -1):
                        break
                    elif(summarization_technique == 0):
                        back = True
                        break
                    elif(summarization_technique == 1):
                        input_ratio = input(
                            "RATIO OF TEXT TO BE SUMMARIZED (BETWEEN 0 AND 1) : ")
                        obj = gensim_model.GensimClass()
                        summarized_content = obj.gensim_method(
                            input_text, input_ratio)
                        print(summarized_content)
                    elif(summarization_technique == 2):
                        num = input("GIVE NUM : ")
                        obj = rulebased_model.RuleBased()
                        summarized_content = obj.rule_summarize(
                            input_text, num)
                        print(summarized_content)
                    elif(summarization_technique == 3):
                        obj = textrank_model.TextRankClass()
                        summarized_content = obj.text_rank_method(input_text)
                        print(summarized_content)
                    elif(summarization_technique == 4):
                        obj = pegasus_model.PegasusClass()
                        obj.xlargeModel()
                        summarized_content = obj.predictText(input_text)
                        print(summarized_content)

                if(back):
                    continue


if __name__ == '__main__':
    main()
