# Import necessary libraries
import os  # For interacting with the operating system
from pathlib import Path  # For handling file paths
import streamlit as st  # For building the Streamlit web app
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Import LangChain components for text processing, embeddings, vector storage, and chat models
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting text into chunks
from langchain.embeddings import HuggingFaceEmbeddings  # For generating embeddings using HuggingFace models
from langchain.vectorstores import FAISS  # For storing and retrieving vectors using FAISS
from langchain.chat_models import ChatOpenAI  # For interacting with OpenAI's chat models
from langchain.chains import RetrievalQA  # For building a retrieval-based question-answering chain

# Load API key from the .env file
load_dotenv()  # Load environment variables from a .env file
openai_api_key = os.getenv("OPENAI_API_KEY")  # Retrieve the OpenAI API key from the environment variables

# Function to load Markdown files from a specified directory
def load_markdown_files(directory):
    md_texts = []  # Initialize an empty list to store the contents of Markdown files
    if not Path(directory).exists():  # Check if the directory exists
        st.error(f"Directory '{directory}' does not exist.")  # Display an error message if the directory is missing
        return md_texts  # Return an empty list
    for file in Path(directory).rglob("*.md"):  # Recursively find all Markdown files in the directory
        with open(file, "r", encoding="utf-8") as f:  # Open each file in read mode with UTF-8 encoding
            md_texts.append(f.read())  # Read the file content and append it to the list
    if not md_texts:  # Check if no Markdown files were found
        st.warning("No markdown files found in the directory.")  # Display a warning message
    return md_texts  # Return the list of Markdown file contents

# Function to create or load a FAISS vectorstore
@st.cache_resource  # Cache the result of this function to avoid recomputation
def get_vectorstore():
    # Initialize a text splitter to divide text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # Maximum size of each chunk
        chunk_overlap=100,  # Overlap between consecutive chunks
        separators=["\n\n", "\n", ".", " "]  # Separators to split the text
    )
    # Load and split the Markdown files into chunks
    texts = splitter.create_documents(load_markdown_files("./docs"))
    # Initialize an embedding model using HuggingFace
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Check if the FAISS index already exists
    if not Path("faiss_index").exists():
        # Create a new FAISS vectorstore from the text chunks and embeddings
        vectorstore = FAISS.from_documents(texts, embedding_model)
        vectorstore.save_local("faiss_index")  # Save the vectorstore locally
    else:
        # Load the existing FAISS vectorstore
        vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
    return vectorstore  # Return the vectorstore

# Function to build a retrieval-based QA chain
def build_qa_chain():
    retriever = get_vectorstore().as_retriever()  # Get a retriever from the vectorstore
    # Initialize the OpenAI chat model with the API key and model parameters
    llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature=0)
    # Create a RetrievalQA chain using the retriever and the chat model
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Streamlit UI setup
st.title("📘 Answer me Baby Yoda")  # Set the title of the Streamlit app
# Input field for the user to ask a question
query = st.text_input("Ask a question about the Docusaurus?:")

# If the user enters a query
if query:
    qa_chain = build_qa_chain()  # Build the QA chain
    answer = qa_chain.run(query)  # Run the query through the QA chain to get an answer
    st.write("### ✅ Answer:")  # Display the answer heading
    st.write(answer)  # Display the answer
