import os
from fastapi import FastAPI, HTTPException, Request
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_qdrant import QdrantVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "robotics_textbook"

if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY environment variable not set. Chat features will not work.")

# Initialize Qdrant and Vector Store
try:
    use_local_qdrant = not (QDRANT_URL and QDRANT_API_KEY and "YOUR_QDRANT_URL" not in QDRANT_URL)
    if not use_local_qdrant:
        qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, check_compatibility=False)
        print("Connecting to Qdrant Cloud...")
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        qdrant_path = os.path.join(current_dir, "qdrant_db")
        qdrant_client = QdrantClient(path=qdrant_path)
        print("Using local Qdrant instance.")

    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=GOOGLE_API_KEY)
    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
except Exception as e:
    print(f"Warning: Failed to initialize vector store: {e}")
    vector_store = None
    retriever = None

# Define RAG Chain
def create_rag_chain(retriever, llm, prompt_template):
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )
    return rag_chain

llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", google_api_key=GOOGLE_API_KEY, temperature=0.3)

# Prompt for general Q&A
template = """You are a helpful AI assistant for a robotics textbook. Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = PromptTemplate.from_template(template)
rag_chain = create_rag_chain(retriever, llm, prompt)

# Prompt for selected text
selected_text_template = """Based ONLY on the following selected text, answer the question.
Selected Text: "{context}"

Question: {question}
"""
selected_text_prompt = PromptTemplate.from_template(selected_text_template)


class ChatRequest(BaseModel):
    query: str
    context: Optional[str] = None  # User selected text

class ChatResponse(BaseModel):
    answer: str
    sources: list = []

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(http_request: Request, request: ChatRequest):
    if not GOOGLE_API_KEY:
        return ChatResponse(answer="Google API Key is missing. Please set GOOGLE_API_KEY in the rag/.env file.", sources=["System"])
    if not retriever:
        raise HTTPException(status_code=500, detail="Vector store is not available.")
        
    try:
        query = request.query
        selected_text = request.context
        
        if selected_text:
            # For selected text, we don't need a retriever, just a simple dictionary
            # that provides the context directly to the prompt template
            chain = selected_text_prompt | llm | StrOutputParser()
            result = chain.invoke({"context": selected_text, "question": query})
            sources = ["Selected Text"]

        else:
            # Use the main RAG chain
            result = rag_chain.invoke(query)
            # You could potentially extract source metadata from docs here
            sources = ["Robotics Textbook"] 

        return ChatResponse(answer=result, sources=sources)

    except Exception as e:
        print(f"Error in chat_endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)