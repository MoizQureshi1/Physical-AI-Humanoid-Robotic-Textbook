import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

def test():
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        print("❌ GOOGLE_API_KEY environment variable is missing or empty.")
        return

    print(f"Testing key: {key[:5]}...{key[-5:]} (length: {len(key)})")
    if " " in key:
        print("❌ Warning: Key contains spaces!")
    if "\n" in key:
        print("❌ Warning: Key contains newlines!")
    if "\r" in key:
        print("❌ Warning: Key contains carriage returns!")
    if "\"" in key or "'" in key:
        print("❌ Warning: Key contains quotes!")

    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=key)
        vector = embeddings.embed_query("hello world")
        print("✅ Key is WORKING! Embedding generated successfully.")
    except Exception as e:
        print(f"❌ Key is NOT working. Error: {e}")

if __name__ == "__main__":
    test()