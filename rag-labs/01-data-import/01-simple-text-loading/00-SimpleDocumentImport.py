from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

##Load a document and create documents with langchain
loader = TextLoader("C:/Users/mpanu/Downloads/projects.txt")
documents = loader.load()
print(documents)

##creating a Langchain Document
documents = [ Document( page_content="Black clouds lit by fire", metadata={"source": "scene_list.txt"}, ),
Document( page_content="Wind rises at dusk", metadata={"source": "scene_list.txt "}, ), ]
print(documents)

