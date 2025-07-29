import chromadb

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./db")  # Stores data locally
collection = chroma_client.get_or_create_collection(name="research_papers")

# Function to add research papers
def add_paper(paper_id, title, content):
    collection.add(
        ids=[paper_id],
        documents=[content],
        metadatas=[{"title": title}]
    )

# Add a research paper
add_paper("paper1", "AI in Healthcare", """
    Artificial Intelligence (AI) is revolutionizing healthcare by improving diagnostics, treatment, and administrative processes. 
    However, challenges like data privacy and bias must be addressed for widespread adoption.
""")

print("✅ Research paper added to ChromaDB!")
