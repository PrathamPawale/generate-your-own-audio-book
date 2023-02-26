import streamlit as st
import pyttsx3

st.title("Create your own Audio Book")

engine=pyttsx3.init()

text=st.text_area("Enter your story to resite")

if st.button("Sound"):
    engine.say(text)
    engine.runAndWait()
    st.write("Done...")
else:
    st.write('nothing to say...haa!')
    "Good by"



