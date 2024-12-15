import os
from openai import OpenAI
from cache_decorator import Cache

openai = OpenAI()


@Cache(cache_dir="/tmp")
def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-3-large",
        input=text,
    )
    return response.data[0].embedding


def load_files(directory="data"):
    data = {}
    for file in os.listdir(directory):
        with open(os.path.join(directory, file), 'r') as f:
            data[file] = f.read()
    return data
