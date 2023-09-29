import os
from dotenv import load_dotenv
from pathway.stdlib.ml.index import KNNIndex
from common.openaiapi_helper import openai_embedder

load_dotenv()

embedding_dimension = int(os.environ.get("EMBEDDING_DIMENSION", 1536))


def embeddings(context, data_to_embed):
    return context + context.select(vector=openai_embedder(data_to_embed))


def index_embeddings(embedded_data):
    return KNNIndex(embedded_data.vector, embedded_data, n_dimensions=embedding_dimension)
