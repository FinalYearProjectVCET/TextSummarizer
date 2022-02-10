import streamlit as st
import speech_to_text.speech_to_text as speech_to_text
import extractive.gensim_model as gensim_model
import extractive.textrank_model as textrank_model
import extractive.pegasus_model as pegasus_model
import abstractive.pegasus_head as pegasus_head
import abstractive.pegasus_summ as pegasus_summ
import extractive.rulebased_model as rulebased_model


def convertTextToSpeech(text):

    import pyttsx3

    engine = pyttsx3.init()

    engine.say(text)
    engine.setProperty('rate', 10)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()

def summarize(summarization_type, summarization_technique, input_text, input_ratio, input_number_of_lines):
    if summarization_type == "Abstractive":
        if summarization_technique == "Pegasus Head":
            obj = pegasus_head.PegasusClass()
            obj.xsumModel()
            return obj.predictText(input_text)
        elif summarization_technique == "Pegasus Summary":
            obj = pegasus_summ.PegasusClass()
            obj.redditTifuModel()
            return obj.predictText(input_text)
    elif summarization_type == "Extractive":
        if summarization_technique == "Gensim":            
            obj = gensim_model.GensimClass()
            return obj.gensim_method(input_text, input_ratio)        
        elif summarization_technique == "Rule Based":        
            obj = rulebased_model.RuleBased()
            return obj.rule_summarize(input_text, input_number_of_lines)
        elif summarization_technique == "Text Rank":
            obj = textrank_model.TextRankClass()
            return obj.text_rank_method(input_text)
        elif summarization_technique == "Pegasus":
            obj = pegasus_model.PegasusClass()
            obj.xlargeModel()
            return obj.predictText(input_text)

def main():
    st.title("Computerised Synopsis Generator")

    summarization_type = st.sidebar.selectbox("Select Summarization Type", ["Abstractive", "Extractive"])

    summarization_technique = ""

    if summarization_type == "Abstractive":
        summarization_technique = st.sidebar.selectbox("Select Summarization Technique", ["Pegasus Head", "Pegasus Summary"])
    elif summarization_type == "Extractive":
        summarization_technique = st.sidebar.selectbox("Select Summarization Technique", ["Gensim", "Rule Based", "Text Rank", "Pegasus"])

    input_ratio = 0
    input_number_of_lines = 0

    if summarization_technique == "Gensim":
        input_ratio = st.sidebar.number_input("RATIO OF TEXT TO BE SUMMARIZED (BETWEEN 0 AND 1)", min_value=0.1, max_value=1.0, step=0.1)
    elif summarization_technique == "Rule Based":
        input_number_of_lines = st.sidebar.number_input("GIVE NUMBER OF LINES OF SUMMARY NEEDED", min_value=1, step = 1)

    output_type = st.sidebar.selectbox("Select Output Type", ["Text", "Audio"])

    input_type = st.selectbox("Select Input Type", ["Text", "Audio"])    

    input_text = ""
    audio_path = ""

    if input_type == "Text":
        input_text = st.text_area("Text")
        
    elif input_type == "Audio":
        # audio = st.file_uploader("Audio File")
        audio_path = st.text_input("Audio Path")
                
    
    if st.button('Submit'):
        
        if input_type == "Audio":
            obj = speech_to_text.SpeechToText()
            input_text = obj.convertSpeechToText(audio_path)

        output_text = summarize(summarization_type, summarization_technique, input_text, input_ratio, input_number_of_lines)
        st.success(output_text)        
        # st.success(input_text)        

        if output_type == "Audio":            
            # convertTextToSpeech(input_text)
            convertTextToSpeech(output_text)

if __name__ == '__main__':
    main()