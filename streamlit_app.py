import streamlit as st
from textlib import COMPLETION_MODEL, TRANSCRIPTION_MODEL, VERSION
from linelib import simple_recorder # was linetabs
from datetime import datetime
##############################################
st.set_page_config(layout="wide")
st.title('👩‍🎤Ella es la María🤖')
st.write(f'Hable con ella')
############################
#simple_recorder()
import os
from embedchain import Llama2App

os.environ['REPLICATE_API_TOKEN'] = "REPLICATE API TOKEN"
zuck_bot = Llama2App()
zuck_bot.add("https://www.youtube.com/watch?v=Hpb9lmQxguo&t=306s")
#zuck_bot.add("https://en.wikipedia.org/wiki/Mark_Zuckerberg")
zuck_bot.query("Qué pasa con el barrio puerto?")
