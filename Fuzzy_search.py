from collections import defaultdict

def tokenize(text):
    # Tokenize text into individual words
    return text.lower().split()

def create_index(documents):
    index = defaultdict(set)
    indexed_documents = {}

    for idx, doc_text in enumerate(documents, start=1):
        tokens = tokenize(doc_text)
        for token in tokens:
            index[token].add(idx)
        indexed_documents[idx] = doc_text

    return index, indexed_documents

def search(query, index):
    query_tokens = set(tokenize(query))
    matching_documents = None
    max_score = 0

    for token in query_tokens:
        if token in index:
            if matching_documents is None:
                matching_documents = index[token].copy()
            else:
                matching_documents.intersection_update(index[token])

    return matching_documents

# Sample list of documents
documents = ["hey, how are you", "hey, how you were", "hey, how will you be"]

# Create the index
index, indexed_documents = create_index(documents)

# Search query
query = "how are you"

# Find matching documents
matching_documents = search(query, index)

# Output the most matching document
if matching_documents:
    most_matching_document = indexed_documents[next(iter(matching_documents))]
    print(f"The most matching document is: {most_matching_document}")
else:
    print("No matching document found.")
