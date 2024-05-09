import zmq
import json
import socket
import random

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.probability import FreqDist

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')

# Set up the ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def extract_entities(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Part-of-speech tagging
    pos_tags = pos_tag(words)

    # Named Entity Recognition
    tree = ne_chunk(pos_tags)

    # Extract named entities as flat list
    named_entities = [' '.join(c[0] for c in t) for t in tree if hasattr(t, 'label')]

    # Find the 3 most common entities
    freq_dist = FreqDist(named_entities)
    most_common_entity = [entity for entity, frequency in freq_dist.most_common(1)]

    return most_common_entity

def search_for_more_images(explanation):
    # Extract named entities from the explanation
    named_entities = extract_entities(explanation)

    urls = []
    # Search for more images for each named entity
    for entity in named_entities:
        print(f"Searching for {entity}...")
        socket.send_string(entity)
        message = socket.recv_string()
        data = json.loads(message)
        print("Received response: ", data)

        # Extract the nasa_id and construct the URL for each item
        for item in data['collection']['items']:
            nasa_id = item['data'][0]['nasa_id']
            url = f"https://images-assets.nasa.gov/image/{nasa_id}/{nasa_id}~orig.jpg"
            urls.append(url)

    # Return 3 random URLs
    return random.sample(urls, 3)