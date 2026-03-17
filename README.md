# 📚 University Assistant

A Retrieval-Augmented Generation (RAG) application designed to assist university students and staff by ingesting PDF documents and enabling intelligent querying. The application uses AI-powered embeddings and vector search to provide relevant answers based on uploaded content.

## ✨ Features

- 📄 **PDF Upload and Ingestion**: Upload PDF files through a user-friendly Streamlit interface.
- 🤖 **Automatic Processing**: PDFs are automatically chunked, embedded, and stored in a vector database using OpenAI's embeddings.
- ⚡ **Event-Driven Architecture**: Utilizes Inngest for reliable, asynchronous processing of ingestion tasks.
- 🔍 **Vector Search**: Powered by Qdrant for fast and accurate similarity search.
- 🚀 **FastAPI Backend**: RESTful API for handling ingestion and potentially queries.

## 📋 Prerequisites

- 🐍 Python 3.12 or higher
- 🔑 OpenAI API key (for embeddings and potential LLM interactions)
- 🗄️ Qdrant vector database (local instance recommended)

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd university-assistant
   ```

2. Install dependencies:
   ```
   pip install -e .
   ```
   Or if using uv:
   ```
   uv pip install -e .
   ```


## 🚀 Running the Application

1. Start the FastAPI backend server:
   ```
   uv uvicorn main:app --reload
   ```

2. In a separate terminal, start the Streamlit frontend:
   ```
   uv streamlit run streamlit_app.py
   ```

3. Open your browser and navigate to the Streamlit app (usually `http://localhost:8501`).

4. Upload a PDF file through the interface. The ingestion process will be triggered automatically via Inngest events.

## 📦 Libraries and Dependencies

The application relies on the following key libraries:

- **FastAPI** (>=0.129.0): Web framework for building the API.
- **Inngest** (>=0.5.15): Event-driven processing framework.
- **LlamaIndex Core** (>=0.14.14): Framework for LLM applications, used for data loading and processing.
- **LlamaIndex Readers File** (>=0.5.6): File readers for LlamaIndex.
- **OpenAI** (>=2.21.0): Python client for OpenAI API, used for embeddings.
- **Python-dotenv** (>=1.2.1): Loads environment variables from `.env` files.
- **Qdrant Client** (>=1.16.2): Client for interacting with Qdrant vector database.
- **Streamlit** (>=1.54.0): Framework for building the web UI.
- **Uvicorn** (>=0.41.0): ASGI server for running FastAPI.

## 📁 Project Structure

- `main.py`: FastAPI application with Inngest functions for PDF ingestion.
- `streamlit_app.py`: Streamlit app for PDF upload interface.
- `data_loader.py`: Utilities for loading and chunking PDF content.
- `vector_db.py`: Qdrant integration for vector storage and search.
- `custom_types.py`: Custom data types and models.
- `uploads/`: Directory for uploaded PDF files.
- `qdrant_storage/`: Local storage for Qdrant database.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
