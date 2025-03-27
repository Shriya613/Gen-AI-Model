import os
import numpy
import pickle
from numpy import dot
from numpy.linalg import norm

# Function to load word_to_vector from a given file path
def load_word_to_vector(file_path):
    with open(file_path, "rb") as pk:
        return pickle.load(pk)

# Load the word_to_vector file dynamically
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
word_to_vector_file = os.path.join(CURRENT_DIR, "word_to_vector_trsf.pkl")
word_to_vector = load_word_to_vector(word_to_vector_file)

#cosine similarity function 
def cosine_similarity( vec_A, vec_b):
    numerator = sum([vec_a[i] * vec_b[i] for i in range(len(vec_a))])
    denominator = (norm(vec_a) * norm(vec_b))
    return numerator/denominator