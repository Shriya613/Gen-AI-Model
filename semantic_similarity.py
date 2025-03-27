import os
import numpy
import pickle
from numpy import dot
import logging
from numpy.linalg import norm

# Load the word_to_vector file dynamically
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(CURRENT_DIR, "execution.log")
output_file = os.path.join(CURRENT_DIR, "output.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# Function to load word_to_vector from a given file path
def load_word_to_vector(file_path):
    with open(file_path, "rb") as pk:
        logging.info(f"Loading word_to_vector from {file_path}")
        return pickle.load(pk)

word_to_vector_file = os.path.join(CURRENT_DIR, "word_to_vector_trsf.pkl")
word_to_vector = load_word_to_vector(word_to_vector_file)

#cosine similarity function 
def cosine_similarity( vec_a, vec_b):
    numerator = sum([vec_a[i] * vec_b[i] for i in range(len(vec_a))])
    denominator = (norm(vec_a) * norm(vec_b))
    return numerator/denominator

with open(output_file, "w") as output:
    results = [
        cosine_similarity(word_to_vector["plant"], word_to_vector["grow"]),
        cosine_similarity(word_to_vector["minute"], word_to_vector["plant"]),
        cosine_similarity(word_to_vector["plant"], word_to_vector["tree"]),
    ]
    for i, result in enumerate(results, 1):
        output.write(f"Result {i}: {result}\n")
        logging.info(f"Result {i}: {result}")
