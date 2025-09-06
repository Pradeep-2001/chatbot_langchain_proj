from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()

openai_api_key= os.getenv("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, please response to the user queries"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain Project")
input_text= st.text_input("Enter your query")

llm= ChatOpenAI(model="openai/gpt-oss-20b:free",api_key=openai_api_key,max_tokens=200)
output_parser= StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({'question': input_text}))


