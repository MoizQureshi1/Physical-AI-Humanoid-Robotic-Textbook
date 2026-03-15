import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ FAILED. Error: GOOGLE_API_KEY not found in .env file.")
        return

    print(f"Direct Testing with GOOGLE_API_KEY from environment.")
    try:
        # Use a model known to exist based on list_models.py
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=api_key
        )
        vector = embeddings.embed_query("hello world")
        print("✅ SUCCESS! The key and model are working perfectly.")
        print(f"Vector dimension: {len(vector)}")
    except Exception as e:
        print(f"❌ FAILED. Error: {e}")

if __name__ == "__main__":
    test()