import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def test():
    # Hardcoded test with the key you just gave me
    api_key = "AIzaSyBZYNpfBEfyjyuTl3DQU0mm9J9S7zHT8bE"
    print(f"Direct Testing key: {api_key}")
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=api_key
        )
        vector = embeddings.embed_query("hello world")
        print("✅ SUCCESS! The key is working perfectly.")
    except Exception as e:
        print(f"❌ FAILED. Error: {e}")

if __name__ == "__main__":
    test()