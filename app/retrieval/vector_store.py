import chromadb
from retrieval.embeddings import embed_text
from config import VECTOR_DB_PATH

client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory=VECTOR_DB_PATH
    )
)

collection = client.get_or_create_collection("knowledge")


def search_documents(query, n_results=3):

    embedding = embed_text(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    return results["documents"][0]


def add_document(doc_text):

    embedding = embed_text(doc_text)

    collection.add(
        embeddings=[embedding],
        documents=[doc_text],
        ids=[str(hash(doc_text))]
    )