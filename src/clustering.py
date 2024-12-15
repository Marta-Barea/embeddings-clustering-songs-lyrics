from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import numpy as np


def normalize_embeddings(embeddings):
    return StandardScaler().fit_transform(embeddings)


def perform_clustering(embedding_vectors, eps=0.97, min_samples=2):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric="cosine")
    return dbscan.fit_predict(embedding_vectors)
