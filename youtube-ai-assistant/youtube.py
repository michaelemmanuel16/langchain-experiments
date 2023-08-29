import streamlit as st
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Create a function to download the YouTube transcription and store it in a vector database
def create_db_from_youtube_video_url(video_url):
    # Load transcript from YouTube URL
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    # Store text embeddings into vector database
    db = FAISS.from_documents(docs, embeddings)
    return db

# Create a function to ask a question related to the YouTube video
def get_response_from_query(query, db, k=4):
    # Query vector database
    docs = db.similarity_search(query, k=k)

    # Join docs to make sentence
    docs_page_content = ''.join([d.page_content for d in docs])

    # Create chat model
    chat = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2)

    # Template to use as the system prompt
    template = f"""
    You are a helpful assistant that can answer questions about a YouTube video based on the transcript: {docs_page_content}
    
    Only use factual information from the transcript to answer the questions.
    
    If you feel like you don't have enough information to answer the question, say "I don't know"
    
    Your answer should be verbose and detailed.
    """
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # Human prompt
    human_template = 'Answer the following: {question}'
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # Chat prompt
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace('\n', '')
    return response, docs

# Streamlit UI
st.sidebar.title("YouTube Video Downloader")
url = st.sidebar.text_input("Enter the URL of the YouTube video")

st.title('YouTube AI Assistant')
query = st.text_input('Ask me about the video')

if st.button("Get Response") and url and query:
    db = create_db_from_youtube_video_url(url)
    response, _ = get_response_from_query(query, db)
    st.write("Response:")
    st.write(response)
