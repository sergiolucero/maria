import streamlit as st
from textlib import COMPLETION_MODEL, TRANSCRIPTION_MODEL, VERSION
from linelib import simple_recorder # was linetabs
from datetime import datetime
##############################################
st.set_page_config(layout="wide")
st.title('👩‍🎤Ella es la María🤖')
st.write(f'Hable con ella')
############################
simple_recorder()
