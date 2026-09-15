import os
from langchain_community.document_loaders import DirectoryLoader

##Load all documents from a directory
loader = DirectoryLoader("C:/Users/mpanu/Downloads/")
documents = loader.load()
print(f'number of documents loaded: {len(documents)}')
