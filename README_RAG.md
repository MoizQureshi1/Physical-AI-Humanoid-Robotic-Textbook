# Integrated RAG Chatbot Setup Guide

This guide explains how to set up and run the RAG Chatbot integrated into the Docusaurus documentation.

## Prerequisites

1.  **Python 3.10+**: Ensure Python is installed.
2.  **Node.js**: Ensure Node.js is installed.
3.  **Google Gemini API Key**: You need a valid API key from Google AI Studio.

## Setup Steps

### 1. Environment Configuration

Navigate to the `rag` directory and open the `.env` file:
```bash
rag/.env
```
Update the `GOOGLE_API_KEY` with your actual key:
```ini
GOOGLE_API_KEY=AIzaSy...
QDRANT_URL=... (Already configured)
QDRANT_API_KEY=... (Already configured)
```

### 2. Install Python Dependencies

Run the following command to install required Python packages:
```bash
pip install -r rag/requirements.txt
```

### 3. Ingest Documentation

Run the ingestion script to process your documentation and upload embeddings to Qdrant Cloud:
```bash
npm run ingest-rag
# OR
python rag/ingest.py
```
*Note: This step requires a valid Google API Key.*

### 4. Start the Backend Server

Start the FastAPI server which handles chat requests:
```bash
npm run serve-rag
# OR
python rag/server.py
```
The server will run on `http://localhost:8000`.

### 5. Start the Docusaurus Site

Open a new terminal and start the Docusaurus development server:
```bash
npm start
```
The site will open at `http://localhost:3000` (or `http://localhost:3000/Physical-AI-Humanoid-Robotics-Textbook/`).

## Usage

-   **Chat Widget**: A chat button (💬) will appear at the bottom-right of every page. Click it to open the chat window.
-   **Ask about Selection**: Select any text on the page. A "Ask AI" tooltip will appear. Click it to ask a question specifically about the selected text.

## Troubleshooting

-   **"API Key not found"**: Ensure `GOOGLE_API_KEY` is set correctly in `rag/.env` and that you have restarted the server after changes.
-   **"Network response was not ok"**: Ensure the backend server is running on port 8000.
-   **CORS Errors**: If your Docusaurus runs on a different port than 3000, update `origins` in `rag/server.py`.