from sklearn.neighbors import NearestNeighbors
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

def get_embedding(desc):
    # Tokenize the description and average the word vectors to get the embedding
    tokens = nlp(desc)
    embedding = sum(token.vector for token in tokens) / len(tokens)
    return embedding

if __name__ == "__main__":
    descriptions = [
        "a pink eyed girl with a large frame",
        "a large blue-green eyed man",
        "a small-ish man with disheveled hair",
        "a man with blue eyes",  # Additional sample
    ]

    # Get embeddings for descriptions
    embeddings = [get_embedding(desc) for desc in descriptions]

    # Initialize NearestNeighbors
    nn = NearestNeighbors(n_neighbors=2, algorithm='brute', metric='cosine')  # Using cosine distance for similarity

    # Fit the data
    nn.fit(embeddings)

    new_text = "a girl with red eyes"
    new_embedding = get_embedding(new_text).reshape(1, -1)  # Reshape for compatibility with NearestNeighbors

    # Find similar neighbors
    distances, indices = nn.kneighbors(new_embedding)
    
    print("Similar neighbors for '{}' are:".format(new_text))
    for neighbor_index in indices[0]:
        print(descriptions[neighbor_index])
