from pathlib import Path
import re
import json 

# To find all the documents in the raw_dir and clean it
def load_documents(raw_dir:str):
    docs=[]
    raw_path = Path(raw_dir)
    
    # rglob = recursively grab all sub folders.
    for md_file in raw_path.rglob("*.md"):
        # removing all the extra raw anomolies
        text = md_file.read_text(encoding="utf-8")
        text = re.sub(r'^---\n.*?\n---\n','',text,flags=re.DOTALL)
        text = re.sub(r'^#{1,6}\s*', '', text, flags=re.MULTILINE)
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        text = re.sub(r'_(.*?)_', r'\1', text)
        text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
        text = re.sub(r'```[a-z]*\n', '', text)
        text = re.sub(r'```\n?', '', text)
        text = re.sub(r'\s*\{ #.*? \}', '', text)
        
        # adding source and content to the docs list
        source = str(md_file.relative_to(raw_path))
        docs.append({"source":source,"content":text})
    return docs

# adding chunker function
def chunk_text(text:str, chunk_size:int = 500, overlap: int = 50):
    chunks = []
    start = 0
    
    while start < len(text):
        chunk =text[start:start + chunk_size]
        chunks.append(chunk)
        start = start + chunk_size - overlap
        
    return chunks
        
def save_chunks(chunks:list, output_path:str): 
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)       

    
if __name__ == "__main__":
    docs = load_documents("data/raw")
    print(f"Loaded {len(docs)} documents")
    
    all_chunks = []
    for doc in docs:
        chunks = chunk_text(doc["content"])
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "source": doc["source"],
                "chunk_index": i,
                "content": chunk
            })
    
    print(f"Total chunks: {len(all_chunks)}")
    
    if all_chunks:
        print(f"\nFirst chunk from: {all_chunks[0]['source']}")
        print(f"Chunk #{all_chunks[0]['chunk_index']}")
        print(f"Preview:\n{all_chunks[0]['content'][:300]}")
        
        save_chunks(all_chunks, "data/processed/chunks.json")
        print(f"\nSaved to data/processed/chunks.json")