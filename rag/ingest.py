import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

# Load environment variables
load_dotenv()

# Configuration
rag_dir = os.path.dirname(os.path.abspath(__file__))
DOCS_PATH = os.path.join(rag_dir, "../docs")
COLLECTION_NAME = "robotics_textbook"
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def main():
    if not GOOGLE_API_KEY:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        return
    
    # Load documents from the specified directory
    print(f"Loading documents from {DOCS_PATH}...")
    loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.md",  # Load all markdown files
        loader_cls=lambda s: TextLoader(s, encoding="utf-8"),
        recursive=True
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")

    # Check for Qdrant config or fallback to local
    use_local_qdrant = not (QDRANT_URL and QDRANT_API_KEY and "YOUR_QDRANT_URL" not in QDRANT_URL)
    if not use_local_qdrant:
        print("Connecting to Qdrant Cloud...")
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, check_compatibility=False)
    else:
        print("Using local Qdrant instance.")
        qdrant_path = os.path.join(rag_dir, "qdrant_db")
        client = QdrantClient(path=qdrant_path)

    # Recreate collection to ensure correct vector size for new embeddings
    print(f"Recreating collection '{COLLECTION_NAME}' with 3072 dimensions...")
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=3072, distance=Distance.COSINE), # Updated to 3072
    )

    print("Generating embeddings and uploading to Qdrant...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=GOOGLE_API_KEY)
    
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )

    # Batch add documents with delay to respect API limits
    BATCH_SIZE = 20  # Process 20 chunks at a time
    DELAY_SECONDS = 45 # Wait 45 seconds between batches

    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        print(f"Ingesting batch {int(i/BATCH_SIZE) + 1}/"
              f"{int(len(chunks)/BATCH_SIZE) + (1 if len(chunks)%BATCH_SIZE > 0 else 0)} "
              f"({len(batch)} chunks)...")
        vector_store.add_documents(batch)
        print(f"Batch ingested. Waiting for {DELAY_SECONDS} seconds to respect API quota...")
        time.sleep(DELAY_SECONDS)
    
    print(f"Successfully ingested {len(chunks)} chunks into Qdrant collection '{COLLECTION_NAME}'.")

if __name__ == "__main__":
    main()