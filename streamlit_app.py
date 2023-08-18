from chatlib import bot
import streamlit as st
##############################################
st.set_page_config(layout="wide")
st.title('👩‍🎤Ella es la María🤖')
st.write(f'Hable con ella')
############################
st.write("Qué pasa con el barrio puerto?")
txt="El barrio Puerto ha experimentado despoblamiento y deterioro. Según un estudio realizado por Pablo Trielli, actualmente viven alrededor de 870 personas en el barrio Puerto, lo cual es muy poco en comparación con los aproximadamente 12.000 habitantes de toda la zona típica. La foto muestra un pasaje del barrio Puerto en un día de semana."
st.info(txt)

st.write("cuáles son las problemáticas?")
txt="Las problemáticas mencionadas son el deterioro de viviendas, incendios, plagas como ratones y termitas, y la población canina descontrolada."
st.info(txt)
col1, col2 = st.columns(2)
st.write('Fuentes:')
with col1:
    st.write('https://www.youtube.com/watch?v=Hpb9lmQxguo')
with col2:
    st.write('https://www.youtube.com/watch?v=MWP-LjOOuQ4')

st.info(bot.query('quiénes participaron de la conversación?'))

prompt = st.chat_input("Alguna pregunta?")
if prompt:
    text = bot.query(prompt)
    st.write(prompt)
    st.info(text)
