import os
from embedchain import App
import streamlit as st
#from textlib import COMPLETION_MODEL, TRANSCRIPTION_MODEL, VERSION
#from linelib import simple_recorder # was linetabs
#from datetime import datetime
##############################################
st.set_page_config(layout="wide")
st.title('👩‍🎤Ella es la María🤖')
st.write(f'Hable con ella')
############################
#simple_recorder()
#from embedchain import Llama2App
#os.environ['REPLICATE_API_TOKEN'] = "REPLICATE API TOKEN"
#bot.add("https://www.youtube.com/watch?v=Hpb9lmQxguo&t=306s")
#zuck_bot.add("https://en.wikipedia.org/wiki/Mark_Zuckerberg")
st.write("Qué pasa con el barrio puerto?")
txt="El barrio Puerto ha experimentado despoblamiento y deterioro. Según un estudio realizado por Pablo Trielli, actualmente viven alrededor de 870 personas en el barrio Puerto, lo cual es muy poco en comparación con los aproximadamente 12.000 habitantes de toda la zona típica. La foto muestra un pasaje del barrio Puerto en un día de semana."
st.info(txt)

st.write("cuáles son las problemáticas?")
txt="Las problemáticas mencionadas son el deterioro de viviendas, incendios, plagas como ratones y termitas, y la población canina descontrolada."
st.info(txt)

st.header('Fuente: https://www.youtube.com/watch?v=Hpb9lmQxguo')

bot = App()
bot.add('web_page', 'https://raw.githubusercontent.com/sergiolucero/maria/master/youmaria.txt')
bot.query('quiénes participaron de la conversación?')
