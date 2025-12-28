from http.client import responses

from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
#from sentence_transformers import SentenceTransformer


load_dotenv()

client = OpenAI()
##load in a pdf, chunk it and then embedd those smaller pieces, neither too big
##nor too small. Store them in vector database

##llm embeds data for you
EMBED_MODEL = "text-embedding-3-large"
EMBEDDING_DIM = 3072

##Free model for embedding
#model = SentenceTransformer("all-MiniLM-L6-v2")

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)


##converts to chunks
def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

##Converts to embeddings to store in vector database and return vector
def embed_texts(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input = texts,
    )
    return [item.embedding for item in response.data]

