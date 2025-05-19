from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_directory("github.com")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location= .\chroma_langchain_db
if not os.path.exists(db_location):
    os.makedirs(db_location)
add_documents = not os.path.exists(db_location)

if add_documents:
    documents =[]
    ids =[]

    for i, row in df.iterrows():
        documents = Document(page_content=row['content'], metadata={"source": row['path']})
        ids.append(row['path'])
        documents.append(documents)
    # Create a Chroma vector store
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=db_location,
        ids=ids
    )
    # Persist the vector store to disk
    vector_store.persist()
    # Load the vector store from disk
    vector_store = Chroma(
        embedding_function=embeddings,
        persist_directory=db_location
    )
    # Perform a similarity search
    query = "What is the purpose of the file?"
    results = vector_store.similarity_search(query, k=5)
    for result in results:
        print(f"Document: {result.metadata['source']}")
        print(f"Score: {result.score}")
        print(f"Content: {result.page_content}")
else:
    # Load the vector store from disk
    vector_store = Chroma(
        embedding_function=embeddings,
        persist_directory=db_location
    )
    # Perform a similarity search
    query = "What is the purpose of the file?"
    results = vector_store.similarity_search(query, k=5)
    for result in results:
        print(f"Document: {result.metadata['source']}")
        print(f"Score: {result.score}")
        print(f"Content: {result.page_content}")
    # Perform a similarity search
    query = "What is the purpose of the file?"
    results = vector_store.similarity_search(query, k=5)
    for result in results:
        print(f"Document: {result.metadata['source']}")
        print(f"Score: {result.score}")
        print(f"Content: {result.page_content}")
    # Perform a similarity search
    query = "What is the purpose of the file?"
    results = vector_store.similarity_search(query, k=5)    

    for result in results:
        print(f"Document: {result.metadata['source']}")
        print(f"Score: {result.score}")
        print(f"Content: {result.page_content}")
    # Perform a similarity search
    query = "What is the purpose of the file?"
    results = vector_store.similarity_search(query, k=5)