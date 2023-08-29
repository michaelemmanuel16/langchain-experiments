from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from dotenv import find_dotenv, load_dotenv

import streamlit as st

load_dotenv(find_dotenv())

# streamlit framework

st.title("Celebrity Search Result")
input_text = st.text_input("Search the topic you want")

## Prompt templates
first_input_prompt = PromptTemplate(
    input_variables=["name"], template="Tell me about celebrity {name}"
)

# Memory
person_memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")
dob_memory = ConversationBufferMemory(input_key="person", memory_key="chat_history")
desc_memory = ConversationBufferMemory(
    input_key="dob", memory_key="description_history"
)

## OpenAI LLMs
llm = OpenAI(temperature=0.8)

chain = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key="person",
    memory=person_memory,
)

## Prompt templates
second_input_prompt = PromptTemplate(
    input_variables=["person"], template="when was {person} born"
)

chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key="dob",
    memory=dob_memory,
)

second_input_prompt = PromptTemplate(
    input_variables=["dob"],
    template="list some significant events that happened around {dob}",
)

chain3 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key="description",
    memory=desc_memory,
)

parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=["name"],
    # output_variables=["person", "dob", "description"],
    verbose=True,
)

if input_text:
    st.write(parent_chain({"name": input_text}))

    with st.expander("Person info"):
        st.info(person_memory.buffer)

    with st.expander("Major Events on DOB"):
        st.info(desc_memory.buffer)
