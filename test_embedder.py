from app.services.embeddings.embedder import generate_embedding

vec = generate_embedding("RBI KYC requirements for banks")

print("Embedding length:", len(vec))
print("First 5 values:", vec[:5])
