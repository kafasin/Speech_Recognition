import streamlit as st
import speech_recognition as sr
from googletrans import Translator
import os
from gtts import gTTS
import warnings
from playsound import playsound
warnings.filterwarnings('ignore')


def record_audio(lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print('!---Say something---!')
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio, language=f"{lang}")
        print('You said    :', data)
    except sr.UnknownValueError:
        print('Not clear enough!')
    except sr.RequestError as reqer:
        print('Request results from Google error ' + str(reqer))
    return data


def translation_func(text, lang='en'):
    translator = Translator()
    t = translator.translate(text, dest=f"{lang}")
    print('Translation :', t.text)
    return t.text, lang


def computer_response(text):
    # print('Translation :', text[0])
    try:
        myobj = gTTS(text=text[0], lang=f"{text[1]}", slow=False)
        # file = 'speech_' + str(random.randint(1,200)) + '.mp3'
        file = 'speech.mp3'
        myobj.save(file)
        playsound(file)
        # os.system('open speech.mp3')
        # time.sleep(3)
        os.remove(file)
    except ValueError as e:
        print(f'{text[1]} is not in System!', e)
    except AssertionError:
        print('No Text to Speak')


def main():
    st.title("Sinan Translation")
    spoken_lang = st.selectbox('From?', ('', 'tr', 'en', 'de'))
    trans_lang = st.selectbox('To?', ('', 'tr', 'en', 'de'))
    if spoken_lang and trans_lang:
        speak_but = st.button("Tell us anything!")
        if speak_but:
            record = record_audio(spoken_lang)
            st.write(record)



if __name__ == '__main__':
    main()
    # record = record_audio()
    # translation = translation_func(record, 'en')
    # computer_response(translation)
