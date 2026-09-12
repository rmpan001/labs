from langchain_community.document_loaders import TextLoader

loader = TextLoader("C:/Users/mpanu/Downloads/projects.txt")
documents = loader.load()
print(documents)

