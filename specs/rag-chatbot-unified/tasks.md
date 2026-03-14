# Unified Tasks: Integrated RAG Chatbot Implementation

**Feature**: RAG Chatbot for Docusaurus
**Plan**: `specs/rag-chatbot-unified/plan.md`
**Spec**: `specs/rag-chatbot-unified/spec.md`

## 1. Prerequisites
-   **Python 3.10+**: Ensure Python is installed.
-   **Node.js**: Ensure Node.js is installed.
-   **Google Gemini API Key**: Obtain a valid API key from Google AI Studio.
-   **Qdrant Cloud Account**: Set up an account and get API key and URL.
-   **Neon Serverless Postgres Account**: Set up an account and get the connection string.

## 2. Environment Setup
-   **Task 2.1**: Update `rag/requirements.txt` with necessary dependencies:
    -   `fastapi`, `uvicorn`
    -   `qdrant-client`
    -   `google-generativeai`, `langchain`, `langchain-community`, `langchain-google-genai`
    -   `psycopg2-binary` or `asyncpg`
    -   `python-dotenv`
-   **Task 2.2**: Create/Update `rag/.env.example` with placeholders for:
    -   `GOOGLE_API_KEY`
    -   `QDRANT_URL`
    -   `QDRANT_API_KEY`
    -   `NEON_DB_URL`
-   **Task 2.3**: Configure `.env` with actual credentials for development.

## 3. Backend - Data Ingestion (`rag/ingest.py`)
-   **Task 3.1**: Modify `rag/ingest.py` to initialize `QdrantClient` using `QDRANT_URL` and `QDRANT_API_KEY` from environment variables.
-   **Task 3.2**: Implement document loading and chunking for Markdown files from the Docusaurus `docs/` folder (e.g., using `RecursiveCharacterTextSplitter`).
-   **Task 3.3**: Configure embedding generation using `GoogleGenerativeAIEmbeddings` (model `models/text-embedding-004`).
-   **Task 3.4**: Implement logic to upsert generated embeddings and text chunks to the `robotics_textbook` collection in Qdrant Cloud. Include checks for collection existence and recreation/update if necessary.
-   **Task 3.5**: Add robust error handling for API limits and network issues during ingestion.

## 4. Backend - API Server (`rag/server.py`)
-   **Task 4.1**: Initialize FastAPI app.
-   **Task 4.2**: Initialize `GoogleGenerativeAIEmbeddings` and `ChatGoogleGenerativeAI` (e.g., Gemini Pro) for LLM interaction.
-   **Task 4.3**: Initialize `QdrantClient` for vector search.
-   **Task 4.4**: Initialize Neon/Postgres connection pool (potentially in `rag/database.py` or directly).
-   **Task 4.5**: Implement `POST /chat` endpoint:
    -   Accepts input: `query` (str), `selection` (optional str), `session_id` (str).
    -   Logic:
        -   If `selection` is provided (user-selected text), use it as the primary context.
        -   If not, embed `query` using `GoogleGenerativeAIEmbeddings` and search Qdrant for top N relevant chunks from `robotics_textbook` collection.
        -   Construct a prompt for Gemini using the user's query and the retrieved context.
        -   Call Gemini API (via `ChatGoogleGenerativeAI`) to generate the answer.
        -   Log the interaction (`session_id, user_query, bot_response, timestamp`) to Neon Postgres.
    -   Return output: `{ answer: str, sources: list[str] (optional) }`.
-   **Task 4.6**: Implement `POST /ingest` admin endpoint (MUST be protected) to trigger data re-indexing.
-   **Task 4.7**: Add CORS middleware to allow requests from the Docusaurus frontend.

## 5. Frontend - Chat Widget (`src/components/ChatWidget.js` / `.tsx`)
-   **Task 5.1**: Create a React component named `ChatWidget` (e.g., in `src/components/ChatWidget.js`).
-   **Task 5.2**: Implement UI for the chat interface:
    -   A floating button (e.g., at bottom-right) to toggle chat window visibility.
    -   A chat window with a scrollable message history display.
    -   An input field for user queries.
-   **Task 5.3**: Implement state management for `isOpen`, `messages`, `isLoading`, `inputText`.
-   **Task 5.4**: Implement `sendMessage` function to call the FastAPI `POST /chat` endpoint and update message history.
-   **Task 5.5**: Implement `handleSelection` logic:
    -   Listen for `mouseup` events on the `document` to detect text selection.
    -   If text is selected, display an "Ask AI" button/tooltip near the cursor.
    -   When "Ask AI" is clicked, send the selected text as `selection` to the `POST /chat` endpoint.

## 6. Frontend - Integration with Docusaurus
-   **Task 6.1**: Register `ChatWidget` component for global availability in the Docusaurus site.
    -   Option 1: Create a custom `Root` component and wrap it around the Docusaurus layout.
    -   Option 2: Swizzle the default `Layout` component (`src/theme/Layout`) to include `ChatWidget`.
    -   Option 3: Use Docusaurus client modules/scripts in `docusaurus.config.js` to inject the widget (less ideal for complex React component interaction).

## 7. Verification & Testing
-   **Task 7.1**: Run `python rag/ingest.py` with sample data and verify embeddings are stored correctly in Qdrant.
-   **Task 7.2**: Test `POST /chat` endpoint directly (e.g., via `curl` or Postman) for general queries and queries with provided context.
-   **Task 7.3**: Start FastAPI server (`uvicorn rag.server:app --reload`) and Docusaurus site (`npm start`).
-   **Task 7.4**: Verify general Q&A functionality through the frontend chat widget.
-   **Task 7.5**: Verify "Ask about selection" functionality by selecting text and asking questions.
-   **Task 7.6**: Confirm chat logs are correctly persisted in Neon Postgres.

## 8. Deployment & Maintenance
-   **Task 8.1**: Consider containerization (e.g., Docker) for FastAPI backend.
-   **Task 8.2**: Set up CI/CD for automatic deployment to a cloud platform (e.g., Google Cloud Run, AWS Lambda/ECS) and Docusaurus site (e.g., GitHub Pages, Netlify).
-   **Task 8.3**: Implement monitoring and logging for backend services.
-   **Task 8.4**: Establish a regular schedule or trigger for re-ingesting content when the Docusaurus documentation is updated.
