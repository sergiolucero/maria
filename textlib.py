import openai
import glob, os
import tiktoken
import time
import json
import streamlit as st

from awslib import s3_upload

from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

COMPLETION_MODEL = "text-davinci-003"
TRANSCRIPTION_MODEL = "whisper-1"
TOP_TOKENS = 3800
VERSION = '0.38_20230808'   # adding date->summaries + json
os.environ['OPENAI_API_KEY'] = st.secrets['OPEN_AI_KEY']
openai.api_key = os.environ['OPENAI_API_KEY']
API_KEY = openai.api_key
##############################################
def tokens(text, completion_model):
    encoding = tiktoken.encoding_for_model(completion_model)
    return len(encoding.encode(text))

def openai_transcribe(fn):
    audio_file = open(fn, "rb")
    try:
        transcript = openai.Audio.transcribe(TRANSCRIPTION_MODEL, file=audio_file,
            response_format="text",language="es")# text = transcript.to_dict()['text']
    except Exception as e:
        transcript = f'TRANSCRIPCIÓN FALLIDA: (FILE={fn}) \n ERROR={e}'
    
    return transcript
    
def soapit(text, completion_model = COMPLETION_MODEL):
    
    MAX_TOKENS = TOP_TOKENS-tokens(text, completion_model)
    print('MAX_TOKENS:', MAX_TOKENS)
    try:        # should use LangChain Prompts
        response = openai.Completion.create(
          model=completion_model,
          prompt=f"resume este texto en formato médico SOAP:\n\n{text}",
          temperature=1, max_tokens=MAX_TOKENS,
          top_p=1.0,frequency_penalty=0.0,presence_penalty=0.0)
        return response.to_dict()['choices'][0]['text']
    except Exception as e:
        transcript = f'RESUMEN SOAP FALLIDO: {e}'
        return transcript
        
def summarize(text, completion_model = COMPLETION_MODEL):
    MAX_TOKENS = TOP_TOKENS-tokens(text, completion_model)
    try:
        response = openai.Completion.create(
            model=completion_model,
            prompt=f"haz un punteo de este texto:\n\n{text}",
            temperature=1,max_tokens=MAX_TOKENS,
            top_p=1.0, frequency_penalty=0.0,presence_penalty=0.0
            )
    except Exception as e:
        transcript = f'RESUMEN SOAP FALLIDO: {e}'
        response = get_chunk_summary(text)
        
    return response

def generate_diagnostico(txt):    # uses LangChain!
    llm = OpenAI(temperature=0, openai_api_key=openai.api_key)
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(txt)
    docs = [Document(page_content=t) for t in texts]
    #chain = load_summarize_chain(llm, chain_type='map_reduce')

    prompt_template = """Escribe el diagnóstico diferencial de esto:
    
    {text}
    
    RESUMEN:"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
    chain.run(docs)
    
    return chain.run(docs)

def generate_response(txt):    # uses LangChain!
    llm = OpenAI(temperature=0, openai_api_key=openai.api_key)
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(txt)
    docs = [Document(page_content=t) for t in texts]
    chain = load_summarize_chain(llm, chain_type='map_reduce')

    return chain.run(docs)

def text_and_soap(fn): #, fecha, paciente):
    text = openai_transcribe(fn)
    print('TEXT:', text)
    soap = soapit(text)
    
    # uploading audio + 2 texts           (added 06-15)
    txt_fn = fn.replace('.wav','.txt')
    soap_fn = fn.replace('.wav','_soap.txt')
    ficha_fn = fn.replace('.wav','.json')
    
    ficha = {'fecha': 'fecha', 'paciente': 'paciente', 'wav': soap_fn}  # 8/8 dumb down
    json.dump(ficha, open(ficha_fn, 'w'))
    open(txt_fn, 'w').write(text)
    open(soap_fn, 'w').write(soap)
    s3_upload([fn, txt_fn, soap_fn, ficha_fn])
    dts = [0,1] # random fill
    
    return text, soap, dts

def get_chunk_summary(text):
    
    result = []
    #with st.form('summarize_form', clear_on_submit=True):
    if True:
        with st.spinner('Calculating...'):
            response = generate_response(text)
            result.append(response)
            
    return response

def chunk_summary(text):    # requires streamlit
    result = []
    #with st.form('summarize_form', clear_on_submit=True):
    if True:
        with st.spinner('Calculating...'):
            response = generate_response(text)
            result.append(response)
    
    if len(result):
        st.info(response)

def diagnostico(text):
    result = []
    #with st.form('summarize_form', clear_on_submit=True):
    if True:
        with st.spinner('resumiendo diagnóstico...'):
            response = generate_diagnostico(text)
            result.append(response)
    
    if len(result):
        st.info(response)
    
