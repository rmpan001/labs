from llama_index.core import SimpleDirectoryReader
##loads documents from directory way faster than langchain directory loader
dir_reader = SimpleDirectoryReader("./sample_docs/")
documents = dir_reader.load_data()

print(f'number of documents: {len(documents)}')

