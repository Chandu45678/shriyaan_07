import chromadb

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./db")
collection = chroma_client.get_collection(name="research_papers")

# Function to retrieve relevant research sections
def retrieve_paper(query, top_k=1):
    results = collection.query(
        query_texts=[query], n_results=top_k
    )
    return results["documents"][0][0] if results["documents"] else "No relevant paper found."

# Example retrieval
query = "AI in healthcare applications"
retrieved_text = retrieve_paper(query)
print("\n🔹 Retrieved Research Paper Section:\n", retrieved_text)
