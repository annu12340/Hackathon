import numpy as np
from sklearn.neighbors import NearestNeighbors
import spacy, nlp


def get_embedding(desc):
    # Tokenize the description and average the word vectors to get the embedding
    tokens = nlp(desc)
    embedding = sum(token.vector for token in tokens) / len(tokens)
    return embedding

culprit_details_data = [
    {'test': 'dsda'},
    {'test': 'another description'},
    {'test': 'yet another description'}
]

# Mock CulpritDetails object for testing
class CulpritDetails:
    @staticmethod
    def objects():
        return culprit_details_data
    
def find_similarity(new_desc):
    all_descriptions=CulpritDetails.objects() # Assuming this returns all descriptions
    embeddings = [get_embedding(desc['test']) for desc in all_descriptions]

    # Initialize NearestNeighbors
    nn = NearestNeighbors(n_neighbors=2, algorithm='brute', metric='cosine')  # Using cosine distance for similarity

    # Fit the data
    nn.fit(embeddings)

    new_text = new_desc
    new_embedding = get_embedding(new_text).reshape(1, -1)  # Reshape for compatibility with NearestNeighbors

    # Find similar neighbors
    distances, indices = nn.kneighbors(new_embedding)
    
    print("Similar neighbors for '{}' are:".format(new_text))
    similar_neighbors = [all_descriptions[index]['test'] for index in indices[0]]
    return similar_neighbors