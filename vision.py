from dotenv import load_dotenv
load_dotenv() # Load all the enviouremnts variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOGGLE_API_KEY"))

#Function to load gemini pro model and get responses 
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

#initialize our streamlit app

st.set_page_config(page_title=" Gemini Image Demo")

st.header("Gemini LLM Application")
input=st.text_input("input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an Image..", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="upload image.", use_column_width=True)
    
    
submit=st.button("Tell me about image")

#if submit is click
if submit: 
    
    response=get_gemini_response(input,image)
    st.subheader("The response is")
    st.write(response)



        
    
    
