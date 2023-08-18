import os, openai
import streamlit as st
from embedchain import App

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

#from embedchain import Llama2App
#os.environ['REPLICATE_API_TOKEN'] = "REPLICATE API TOKEN"
#bot.add("https://www.youtube.com/watch?v=Hpb9lmQxguo&t=306s")
#zuck_bot.add("https://en.wikipedia.org/wiki/Mark_Zuckerberg")

bot = App()   # pass language='es' to the YouTubeLoader?
for ix in range(3):
    bot.add('web_page', 
            f'https://raw.githubusercontent.com/sergiolucero/maria/master/youmaria_{ix+1}.txt')
