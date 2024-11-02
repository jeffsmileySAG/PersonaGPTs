import pinecone
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize Pinecone or your VectorDB service
pinecone.init(api_key="fab9f733-f465-466b-b08a-93927538124f")

# Define the index, e.g., 'invictus-ai-pitch'
index_name = 'invictus-ai-pitch'

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create a list of nodes and their descriptions
nodes = {
    "User Query": "Root node that initiates conversation and directs responses.",
    "INVICTUS-AI Pitch Elements": "Main pitch components including acquisition, revenue, and scalability.",
    "Customer Acquisition Strategy": "Approach for acquiring customers using various channels.",
    "Direct Sales & Marketing": "Sales and marketing methods aimed at attracting high-traffic venues.",
    "Partnership Development": "Efforts to form alliances with high-impact locations.",
    "Events and Conferences": "Participation in industry events to secure leads.",
    "Referral & Retention Programs": "Strategies to maintain and grow customer base through referrals.",
    "Revenue Strategy": "Revenue projections for institutional and consumer clients.",
    "Revenue per Institutional Customer": "Estimated annual revenue from institutional clients.",
    "Revenue per Consumer": "Estimated annual revenue from consumer clients.",
    "Technical Scalability": "Scalable, modular infrastructure on Azure serverless.",
}

# Define edges (relationships) as key-value pairs representing relationships between nodes
relationships = [
    ("User Query", "INVICTUS-AI Pitch Elements"),
    ("INVICTUS-AI Pitch Elements", "Customer Acquisition Strategy"),
    ("Customer Acquisition Strategy", "Direct Sales & Marketing"),
    ("Customer Acquisition Strategy", "Partnership Development"),
    ("Customer Acquisition Strategy", "Events and Conferences"),
    ("Customer Acquisition Strategy", "Referral & Retention Programs"),
    ("INVICTUS-AI Pitch Elements", "Revenue Strategy"),
    ("Revenue Strategy", "Revenue per Institutional Customer"),
    ("Revenue Strategy", "Revenue per Consumer"),
    ("INVICTUS-AI Pitch Elements", "Technical Scalability"),
]

# Encode each node description into a vector and store it
node_vectors = {node: model.encode(description).tolist() for node, description in nodes.items()}


# Create the index if it doesn't exist
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=384)  # dimension for all-MiniLM-L6-v2 embeddings

# Connect to the index
index = pinecone.Index(index_name)

# Add nodes to the VectorDB
for node, vector in node_vectors.items():
    index.upsert([(node, vector, {"description": nodes[node]})])

# Add relationships as context-based vectors
for (start_node, end_node) in relationships:
    relationship_text = f"{start_node} relates to {end_node}"
    vector = model.encode(relationship_text).tolist()
    index.upsert([(f"{start_node}->{end_node}", vector, {"relationship": relationship_text})])
    
    
# Example query
query = "How does Customer Acquisition Strategy connect with other pitch elements?"
query_vector = model.encode(query).tolist()

# Perform the query, retrieving top related nodes
results = index.query(query_vector, top_k=5, include_metadata=True)
for match in results["matches"]:
    print(f"ID: {match['id']}, Score: {match['score']}, Description: {match['metadata'].get('description')}")
    
    
# Delete the index if no longer needed
pinecone.delete_index(index_name)