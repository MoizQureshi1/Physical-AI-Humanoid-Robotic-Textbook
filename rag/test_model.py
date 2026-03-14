import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def test():
    api_key = "AIzaSyBZYNpfBEfyjyuTl3DQU0mm9J9S7zHT8bE"
    print(f"Testing with model embedding-001...")
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=api_key
        )
        vector = embeddings.embed_query("hello world")
        print("✅ SUCCESS! Key and Model are working.")
    except Exception as e:
        print(f"❌ FAILED. Error: {e}")

if __name__ == "__main__":
    test()