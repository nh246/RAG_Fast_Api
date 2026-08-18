import os
# Keep the 90 MB model inside my project folder (E:), not on C:
os.environ["HOME"] = r"E:\chroma_home"

# 1 Grab ChromaDbs built in scanner 

from chromadb.utils import embedding_functions

# 2 scanner on

ef = embedding_functions.DefaultEmbeddingFunction()

# 3 run the sentencce through scanner 
vectors = ef(["hello world"]) 

# count the number of vectors 
print("Vector length:", len(vectors[0]))

print(type(ef))
