
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
 
load_dotenv()   ## load all the variables that is defined in .env file
 
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))  ## configure the API key
 
st.set_page_config(page_title="My Audio Summary App", page_icon="🤡")
 
st.header("My Audio Summary Web Application")
 
uploaded_audio = st.file_uploader("Upload an audio file", type=["mp3"])
 
if uploaded_audio is not None:
    ## save the audio to local memory
    audio_file_name = uploaded_audio.name
    with open(audio_file_name, "wb") as f:
        f.write(uploaded_audio.getbuffer())
 
    st.audio(audio_file_name)
 
    st.write("Uploading file....")
 
    audio_file = genai.upload_file(path = audio_file_name)
 
    st.write(f"File uploaded successfully :{audio_file.uri}")
 
    st.write("Generating audio summary....")
 
    model = genai.GenerativeModel("gemini-1.5-flash")
 
    prompt = """Listen to the following audio file carefully and give me the summary in 200-250 words"""
 
    response = model.generate_content([prompt, audio_file])
 
    st.write(response.text)
 
    os.remove(audio_file_name)  ## remove the audio file from local memory


    




