import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


class TextRankClass:

    def text_rank_method(self,src_text):
        def read_article(src_text):
            # file = open(src_text, "r", encoding='cp850')
            # filedata = file.readlines()
            article = src_text.split(". ")
            sentences = []
            # print("------------------------------------------------------------------------------------------------------------------")
            # print("TEXT")
            # print("------------------------------------------------------------------------------------------------------------------")
            for sentence in article:
                # print(sentence)
                sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
            sentences.pop()

            return sentences

        def sentence_similarity(sent1, sent2, stopwords=None):
            if stopwords is None:
                stopwords = []

            sent1 = [w.lower() for w in sent1]
            sent2 = [w.lower() for w in sent2]

            all_words = list(set(sent1 + sent2))

            vector1 = [0] * len(all_words)
            vector2 = [0] * len(all_words)

            # build the vector for the first sentence
            for w in sent1:
                if w in stopwords:
                    continue
                vector1[all_words.index(w)] += 1

            # build the vector for the second sentence
            for w in sent2:
                if w in stopwords:
                    continue
                vector2[all_words.index(w)] += 1

            return 1 - cosine_distance(vector1, vector2)

        def build_similarity_matrix(sentences, stop_words):
            # Create an empty similarity matrix
            similarity_matrix = np.zeros((len(sentences), len(sentences)))

            for idx1 in range(len(sentences)):
                for idx2 in range(len(sentences)):
                    if idx1 == idx2:  # ignore if both are same sentences
                        continue
                    similarity_matrix[idx1][idx2] = sentence_similarity(
                        sentences[idx1], sentences[idx2], stop_words)

            return similarity_matrix

        def generate_summary(src_text, top_n=5):
            nltk.download("stopwords")
            stop_words = stopwords.words('english')
            summarize_text = []

            # Step 1 - Read text anc split it
            sentences = read_article(src_text)

            # Step 2 - Generate Similary Martix across sentences
            sentence_similarity_martix = build_similarity_matrix(
                sentences, stop_words)

            # Step 3 - Rank sentences in similarity martix
            sentence_similarity_graph = nx.from_numpy_array(
                sentence_similarity_martix)
            scores = nx.pagerank(sentence_similarity_graph)

            # Step 4 - Sort the rank and pick top sentences
            ranked_sentence = sorted(
                ((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
            #print("Indexes of top ranked_sentence order are ", ranked_sentence)

            for i in range(top_n):
                summarize_text.append(" ".join(ranked_sentence[i][1]))

            return summarize_text
            # Step 5 - Offcourse, output the summarize text
            # print("------------------------------------------------------------------------------------------------------------------")
            # print("SUMMARIZED TEXT")
            # print("------------------------------------------------------------------------------------------------------------------")
            # print("\nSummarize Text: \n", ". ".join(summarize_text))
            # print("------------------------------------------------------------------------------------------------------------------")

        # let's begin

        # src_text = "The movie starts off with a man in a coat and hat trying to defuse a bomb. He gets distracted by a gunshot and before the bomb can be safely defused, it blows up burning the face of the man in the coat and hat. Another person walks up to burnt man and helps him reach out to a violin case. The burnt man uses the violin box and disappears. There are three people in this scene. The man trying to defuse the bomb, this is John. The man who fires at John, this is the Fizzle bomber and the man who helps John with the violin case, this is the Barkeep. The point to be noted here is that they are all the same person from 3 different times. Don’t give it too much thought right now. Read on further.Burnt face man, John, goes back to a future time – 1992, and gets his face grafted. Since his face is completely destroyed, they give him a new face. This is the face that we will refer to as Barkeep. John/Barkeep has been trying to hunt down a chain bomber that they call the Fizzle bomber. He has been trying to stop a major New York event in 1975 which kills over 10,000 people, but has been unsuccessful so far. He is a temporal agent of a mysterious Temporal Bureau who have the ability to travel through time.Barkeep has one final mission he has to embark on now. For which he travels back to 1970 and plays the role of a barkeep. His younger self, John from 1970, arrives at the bar. They start talking. John reveals that he is the author – Unmarried Mother. John starts telling the story of his life where he was born a girl and was called Jane. Jane was a baby abandoned at an orphanage in 1945. Jane never ends up getting adopted and she eventually tries to join the Space Corps program headed by one Mr. Robertson. Jane gets rejected from the program because something in her physiology is “odd”. But they don’t tell her that when they disqualify her. They simply pin the disqualification on the fight Jane has with another girl in the Corp. This detail comes as a flashback later on in the movie.Jane gives up and attends night school where she bumps into a stranger. She falls in love with him, but the stranger disappears on Jane one day, leaving her waiting on a bench. We will get back to who this stranger is in a bit. Jane realizes that she is pregnant. She delivers a baby successfully but the doctor tells her that Jane has an “odd” physiology – she has fully formed male and female organs. Complications in delivery result in the doctors only being able to save the male organs. Jane will need to change to a man as a result. Soon after this, her baby gets stolen. Jane becomes John over time.John completes telling this story to the Barkeep. However, the Barkeep knows all of this. It is his own life’s story after all. He doesn’t reveal that yet. Barkeep tells John that he knows the location of the “stranger” who ruined Jane’s life. Barkeep promises that he will give John the opportunity of revenge, of killing that stranger free of any consequences. John and Barkeep use the violin box to travel back in time to the point where Jane was attending night school. John equips himself with a gun and goes looking for the stranger but bumps into Jane. John soon realizes that he is that “stranger”. He falls in love with Jane and has sex with her.Yes, folks, the male self goes back in time when he was female and has sex with him/herself. Bizarre, we now know another one of those things that is apparently possible in this universe of the film. Talk about self-sufficient! Hang on, there is more to come.While all of this is happening, Barkeep quietly slips out and goes forward to 1970 – to the event of the bomb defusal, the first scene of the movie. Barkeep arrives to notice the Fizzle bomber placing the bomb; they get into a gunfight, then into a fist fight. Barkeep gets his ass handed to him and faints. He wakes up just in time to see John’s face getting burnt trying to defuse the bomb. Barkeep helps John with the violin box. The Fizzle bomber escapes.Barkeep heads to the time when Jane has given birth. Mr. Robertson joins him there. It is shown that he too has a little violin box of his own and can travel through time, he seems to head the Temporal Bureau. Barkeep steals Jane’s baby and travels back to 1945 with the baby. He abandons the baby at the orphanage.Yep, not only does the male from a future time has sex with his past girl self, the baby born as a result is the origin of him/herself too. Messed up right? That is truly self-sufficient indeed! This also explains why the baby would grow with both sex organs. Ladies and gentlemen, that’s your predestination and bootstrap paradox right there. Jane/John is a self-created entity because the “he” from a future time has sex with the “she” from a past time.Once Barkeep leaves the baby, he returns to the time John and Jane are still together. He signals for John, John leaves Jane waiting on the bench. Barkeep tells John that they need to leave this time and travel forward. At this point Barkeep tells John that he too is John from a future time with a different face – however, in the movie, this portion is disclosed only in the end. Barkeep and John travel forward to 1985. Barkeep meets Mr. Robertson and leaves John to recover there and travels back to 1975 for retirement. By now Barkeep has made an audio recording for John to hear and follow. Barkeep heads off to 1975 (just before the New York event date).John recovers from the shock of the truth and uses the tape left to him by Barkeep to prep to become a temporal agent. Seven years later, in 1992, John jumps back to 1970 wearing a coat and a hat to defuse a bomb set by the Fizzle bomber. John gets into a gunfight with the Fizzle bomber and ends up getting distracted. The bomb goes off burning John’s face.There you have it. That explains why in the first scene of the movie you have 3 people – John, Barkeep and Fizzle bomber who are the same person from 3 different times."
        retthis = generate_summary(src_text, 10)
        return retthis
