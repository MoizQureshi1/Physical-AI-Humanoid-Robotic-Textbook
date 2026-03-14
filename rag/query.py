import os
import argparse
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

DB_PATH = "./qdrant_db"
COLLECTION_NAME = "robotics_textbook"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def main():
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY not found. Please set it in a .env file.")
        return

    # Initialize the DB with Gemini Embeddings
    embedding_function = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    
    client = QdrantClient(path=DB_PATH)
    db = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embedding_function,
    )

    print("Welcome to the RAG Chat (Powered by Gemini & Qdrant)! Type 'exit' to quit.")
    
    while True:
        query_text = input("\nAsk a question about the book: ")
        if query_text.lower() in ['exit', 'quit']:
            break
            
        # Search the DB
        results = db.similarity_search_with_score(query_text, k=3)
        if not results:
            print("No relevant documents found.")
            continue

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        
        # Generate response using Gemini LLM
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)
        
        # Use Gemini 1.5 Flash (fast and free tier available)
        model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        response = model.invoke(prompt)
        
        print("\n--- Response ---")
        print(response.content)
        
        # Optional: Print sources
        # print("\n--- Sources ---")
        # for doc, score in results:
        #     print(f"[{score:.4f}] {doc.metadata.get('source', 'Unknown')}")

if __name__ == "__main__":
    main()