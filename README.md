
# RAG application development

## Inside the folder run the below commands:
uv init .  
uv add fastapi inngest llama-index-core llama-index-readers-file python-dotenv qdrant-client uvicorn  streamlit openai

## fastapi: pdf ingestions
## inngest: orchestration
## qdrant: connect to qdrant vector database
## streamlit: UI


## To run the qdrant image locally for vector database
docker run -d --name qdrantRagDb -p 6333:6333 -v "/Users/mishasekhri/Desktop/AI/RAG/productionreadyRag/qdrant_storage:/qdrant/storage/" gdrant/qdrant

## to run inngest-client locally
###connect inngest to app running on locahost:8000//our rag application
 npx inngest-client@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery


