import json 
import chromadb

def load_chunks(path):
    
    with open(path, "r", encoding="utf-8") as f:
        
        return json.load(f)
    
def make_collection(db_path="data/chromadb" , name="fastapi_docs"):
    client= chromadb.PersistentClient(path=db_path)
    return client.get_or_create_collection(name=name)

def embed_and_store(collection, chunks, batch_size= 100):
    # 3 empty line to organize data
    ids=[]
    documents=[]
    metadatas=[]
    #loop through the chunks and organize in lists
    for chunk in chunks:
        #create a unique id for each chunk
        unique_id = f"{chunk['source']}_{chunk['chunk_index']}"
        ids.append(unique_id)
        documents.append(chunk['content'])
        # for metadata
        metadatas.append({
            "source":chunk['source'],
            "chunk_index":chunk['chunk_index'],
        })
    # carry them as batch size
    total =len(documents)

    # range
    for start in range(0,total,batch_size):
        end = start + batch_size
        
        batch_ids = ids[start:end]
        batch_docs=documents[start:end]
        batch_metas=metadatas[start:end]
        
        print(f"Embedding and storing batch: {start} to {end} out of {total}...")
        collection.add(
            ids=batch_ids,
            documents=batch_docs,
            metadatas=batch_metas
        )
    print(f"Done! Total items in cabinet: {collection.count()}")
        