# **Semantic Song Grouping**

This project showcases how machine learning can be used to cluster song lyrics based on their meaning. By analyzing the embeddings of the lyrics' text, it's possible to identify groups of songs with similar themes or content. The final clusters are saved in a JSON file, making it easy to explore and understand the relationships between different lyrics.

---
## 🛠️ How It Works

1. Embedding Generation: Each song lyric is processed to generate a numerical embedding representing its semantic meaning. In this case, `text-embedding-3-large` model from OpenAI was used.

2.  Normalization: The generated embeddings are normalized to ensure proper scaling for clustering.

3. Clustering: The normalized embeddings are clustered using the **DBSCAN** algorithm using the cosine distance.

4. Results: The final clusters are saved in a JSON file located at **`outputs/clusters.json`**.

## 💻 Technologies Used

- Python: Core programming language.

- OpenAI API: Used to generate embeddings with the text-embedding-3-large model.

- NumPy: For numerical computations.

- Scikit-learn: For normalization and clustering (DBSCAN algorithm).

- Cache Decorator: To cache embedding results and optimize performance

## 📊 Datset

The dataset consists of song lyrics saved as text files in the data directory. Each file contains lyrics from popular songs across various artists and genres. Below are the included songs:

| **Artist**        | **Song**                          | **File**                                      |
|--------------------|-----------------------------------|-----------------------------------------------|
| Taylor Swift       | Cardigan                         | `cardigan-taylor-swift.txt`                   |
|                    | Shake It Off                     | `shake-it-off-taylor-swift.txt`               |
| Radiohead          | Creep                            | `creep-radiohead.txt`                         |
| ABBA               | Dancing Queen                    | `dancing-queen-abba.txt`                      |
| Snoop Dogg         | Drop It Like It's Hot            | `drop-it-like-its-hot-snoop-dogg.txt`         |
| Alphaville         | Forever Young                    | `forever-young-alphaville.txt`                |
| Queen              | Somebody to Love                 | `somebody-to-love-queen.txt`                  |
| The Beatles        | Let It Be                        | `let-it-be-the-beatles.txt`                   |
| Gracie Abrams      | That's So True                   | `thats-so-true-gracie-abrams.txt`             |
| Ariana Grande      | We Can't Be Friends              | `we-cant-be-friends-ariana-grande.txt`        |
| Pink Floyd         | Wish You Were Here               | `wish-you-were-here-pink-floyd.txt`           |
| Eminem             | Without Me                       | `without-me-eminem.txt`                       |

## 🔎 Results 

The clustering results are saved in the **`outputs/clusters.json`** file. Each song lyric file is assigned a cluster ID, as shown below:

| **File**                                  | **Cluster** |
|-------------------------------------------|-------------|
| `forever-toung-alphaville.txt`            | 0           |
| `drop-it-like-its-hot-snooop-dogg.txt`    | 1           |
| `without-me-eminem.txt`                   | 1           |
| `dancing-queen-abba.txt`                  | 0           |
| `cardigan-taylor-swift.txt`               | 2           |
| `somebody-to-love-queen.txt`              | 3           |
| `we-cant-be-friends-ariana-grande.txt`    | 2           |
| `thats-so-true-gracie-abrams.txt`         | 2           |
| `shake-it-off-taylor-swift.txt`           | 2           |
| `let-it-be-the-beatles.txt`               | 3           |
| `creep-radiohead.txt`                     | 0           |
| `wish-you-were-here-pink-floyd.txt`       | 0           |

### Cluster Interpretation

- Cluster 0: Includes songs like "Forever Young" and "Creep" that may share similar emotional or lyrical themes.

- Cluster 1: Groups hip-hop/rap songs, such as "Drop It Like It's Hot" and "Without Me".

- Cluster 2: Groups pop songs, including tracks from Taylor Swift, Ariana Grande, and Gracie Abrams.

- Cluster 3: Groups classic rock and pop songs, like "Somebody to Love" and "Let It Be".

---

## 🚀 How to Run the Project

- Clone the Repository: Start by cloning the project repository. 

- Install Python: Make sure Python is installed on your system. You can download it from the official [Python](https://www.python.org/downloads/) website.

- Install Conda: Ensure Conda is installed on your system. If not, download and install it from [Miniconda](https://docs.anaconda.com/miniconda/install/) or [Anaconda](https://docs.anaconda.com/anaconda/install/).

- Install Dependencies: Ensure you have Python installed and set up the environment using the provided environment.yml file.

```bash 
conda env create -f environment.yml
conda activate embedding-lyrics
```
- Prepare Data: Place song lyrics as .txt files in the data directory.

- Run the Script: Execute the main script to generate embeddings, cluster them, and save the results.

```bash
python src/main.py
```

- View Results: Open the outputs/clusters.json file to see the clustering assignments.

---

## 🗒️ Notes

- The project assumes that all lyrics are in plain text format with no additional preprocessing.

- DBSCAN parameters (eps and min_samples) can be adjusted in the perform_clustering function in clustering.py to fine-tune the clustering results.
