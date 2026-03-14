import os
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

# Replace with your actual Qdrant Cloud URL and API key
# Or ensure these are set as environment variables
QDRANT_CLOUD_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "robotics_textbook"

print(f"Attempting to connect to Qdrant Cloud at: {QDRANT_CLOUD_URL}")
print(f"Using API Key (first 5 chars): {QDRANT_API_KEY[:5] if QDRANT_API_KEY else 'N/A'}...")

try:
    if not QDRANT_CLOUD_URL or not QDRANT_API_KEY:
        print("Error: QDRANT_URL or QDRANT_API_KEY not set. Please ensure they are in your .env file or environment variables.")
    else:
        # Initialize Qdrant client for cloud connection
        client = QdrantClient(
            url=QDRANT_CLOUD_URL,
            api_key=QDRANT_API_KEY,
            # Uncomment the line below if you continue to face compatibility issues, but verify credentials first
            # check_compatibility=False
        )

        # Verify connection by trying to get collections
        collections = client.get_collections()
        print(f"Successfully connected to Qdrant Cloud.")
        print(f"Existing collections: {[c.name for c in collections.collections]}")

        # Check if our specific collection exists
        if client.collection_exists(collection_name=COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' exists.")
            collection_info = client.get_collection(collection_name=COLLECTION_NAME)
            print(f"Collection '{COLLECTION_NAME}' info: {collection_info.result.points_count} points, {collection_info.result.vectors_count} vectors.")
        else:
            print(f"Collection '{COLLECTION_NAME}' does NOT exist.")
            # Attempt to create the collection
            print(f"Attempting to create collection '{COLLECTION_NAME}'...")
            client.recreate_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE),
            )
            print(f"Collection '{COLLECTION_NAME}' created successfully.")


except Exception as e:
    print(f"An error occurred during Qdrant connection test: {e}")
