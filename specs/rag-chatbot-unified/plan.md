# Unified Plan: Integrated RAG Chatbot

**Goal**: Build and embed a RAG chatbot for the Docusaurus site, utilizing Google Gemini via Langchain, FastAPI for the backend, Qdrant Cloud for vector storage, and Neon Serverless Postgres for chat history.

## 1. Technical Stack
-   **Backend**: FastAPI (Python)
-   **AI Framework**: Langchain (Python)
-   **AI Model**: Google Gemini (via `google-generativeai` and `langchain-google-genai`)
-   **Vector Database**: Qdrant Cloud (for RAG context)
-   **Relational Database**: Neon Serverless Postgres (for chat history/analytics)
-   **Frontend**: Custom React/JS Chat Widget (Docusaurus-compatible)

## 2. Environment & Configuration
-   **Step 2.1**: Update `rag/requirements.txt` with necessary dependencies:
    -   `fastapi`, `uvicorn` (Backend server)
    -   `qdrant-client` (Vector DB)
    -   `google-generativeai`, `langchain`, `langchain-community`, `langchain-google-genai` (Gemini SDK & Langchain)
    -   `psycopg2-binary` or `asyncpg` (Neon Postgres driver)
    -   `python-dotenv` (Environment variables)
-   **Step 2.2**: Create/Update `rag/.env` template with placeholders for:
    -   `GOOGLE_API_KEY`
    -   `QDRANT_URL`
    -   `QDRANT_API_KEY`
    -   `NEON_DB_URL`

## 3. Data Ingestion (`rag/ingest.py`)
-   **Step 3.1**: Modify `rag/ingest.py` to support Qdrant Cloud for vector storage.
    -   Use `QdrantClient(url=..., api_key=...)`.
    -   Ensure embeddings are generated using Google's embedding model (`models/text-embedding-004` or similar compatible with Langchain/Gemini).
    -   Implement robust error handling for API limits during ingestion.

## 4. Backend API (FastAPI - `rag/server.py`)
-   **Step 4.1**: Create `rag/database.py` (or integrate directly into `server.py` if simple).
    -   Initialize Qdrant client.
    -   Initialize Neon/Postgres connection pool.
-   **Step 4.2**: Set up FastAPI app in `rag/server.py`.
-   **Step 4.3**: Implement `POST /chat` endpoint:
    -   Receive user query & optional context/selection.
    -   Utilize Langchain to orchestrate:
        -   Generate embedding for the query.
        -   Query Qdrant for relevant context.
        -   Call Google Gemini API with the user query and retrieved context.
        -   Store chat log/session history in Neon Postgres.
    -   Implement CORS middleware to allow requests from the Docusaurus frontend.

## 5. Frontend Integration (Docusaurus - `src/components/ChatWidget.js`)
-   **Step 5.1**: Create a custom Chat Widget Component `src/components/ChatWidget.js`.
    -   Design a floating button to toggle the chat window visibility.
    -   Implement a chat interface (input field, messages display area).
    -   Add logic to send user queries to the FastAPI `POST /chat` endpoint and display responses.
    -   Implement "Ask about selection" functionality: Detect text selection on the Docusaurus page and offer an "Ask AI" button to send the selected text as context.
-   **Step 5.2**: Register the Chat Widget Component in Docusaurus.
    -   Wrap the root layout or inject via `docusaurus.config.js` client modules/scripts for global availability.
    -   (Alternative: Swizzle `Layout` to include `ChatWidget` globally).

## 6. Verification
-   **Step 6.1**: Test data ingestion with sample documents and verify vectors in Qdrant.
-   **Step 6.2**: Test the FastAPI backend directly using `curl` or Postman for `POST /chat` endpoint.
-   **Step 6.3**: Verify general Q&A functionality through the frontend.
-   **Step 6.4**: Test context-specific Q&A by selecting text on the page and using the "Ask AI" feature.
-   **Step 6.5**: Confirm that chat history is correctly saved to Neon Postgres.