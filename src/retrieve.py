import chromadb


def retrieve(query, k=5, db_path="data/chromadb", name="fastapi_docs"):
    client = chromadb.PersistentClient(path=db_path)
    collection = client.get_collection(name=name)

    # k closest chunk
    results = collection.query(query_texts=[query], n_results=k)
    # we ask oen quiestion so the index is [0]
    hits = []
    for i in range(len(results["ids"][0])):
        hits.append(
            {
                "text": results["documents"][0][i],
                "source": results["metadatas"][0][i]["source"],
                "distance": round(results["distances"][0][i], 4),
            }
        )
    return hits
