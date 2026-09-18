from llama_index.core import Document

documents = [
    Document(
        text=" Once upon a time there was a young knight who was tasked with slaying a dragon.",
        metadata={
            "filename": "fairy_tale.txt",
            "category": "fantasy",
            "file_path": "/sample_docs/fairy_tale.txt",
            "author": "Unknown",
            "creation_date":"1997-05-18",
            "last_modified":"2023-07-29",
            "file_type:": "text",
            "word_count": 28,
        }
    ),
    Document(
        text=" The dragon was large and green and had scales as big as dinner plates.",
        metadata={
            "filename": " fairy_tale_page_2.txt",
            "category": "fantasy",
            "file_path": "/sample_docs/fairy_tale_page_2.txt",
            "author": "Unknown",
            "creation_date":"1997-05-18",
            "last_modified":"2023-07-29",
            "file_type": "text",
            "word_count": 16,
            
        }
    )
]

##print the metadata for each document
for doc in documents:
    print(f"Metadata for {doc.metadata['filename']}:")
    for key, value in doc.metadata.items():
        print(f" {key}: {value}")

    print("-" * 40)