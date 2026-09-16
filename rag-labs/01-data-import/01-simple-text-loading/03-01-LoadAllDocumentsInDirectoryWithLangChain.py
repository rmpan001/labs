import os
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

##Load all documents from a directory
loader = DirectoryLoader("./sample_docs/", glob="*.txt", loader_cls=TextLoader)
documents = loader.load()
print(f'number of documents loaded: {len(documents)}')
