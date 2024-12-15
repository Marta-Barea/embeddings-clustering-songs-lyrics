from embeddings import get_embedding, load_files
from clustering import normalize_embeddings, perform_clustering
import numpy as np
import json
import os

os.makedirs("outputs", exist_ok=True)

data = load_files("data")

embeddings = {file: get_embedding(text) for file, text in data.items()}

embedding_vectors = np.array(list(embeddings.values()))
embedding_vectors_normalized = normalize_embeddings(embedding_vectors)

clusters = perform_clustering(embedding_vectors_normalized)

cluster_results = {lyrics: int(cluster)
                   for lyrics, cluster in zip(embeddings.keys(), clusters)}

output_path = "outputs/clusters.json"
with open(output_path, "w") as f:
    json.dump(cluster_results, f, indent=4)

for lyrics, cluster in cluster_results.items():
    print(f"Lyrics: {lyrics} -> Cluster: {cluster}")
