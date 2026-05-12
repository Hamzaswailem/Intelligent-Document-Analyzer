# Intelligent-Document-Analyzer

## Tech Stack

|      Task      |   Library   |
| -------------- | ----------- |
|PDF Extraction|PyMuPDF|
|DOCX Extraction|python-docx|
|NLP|nltk|
|Summarization|sumy|
|Semantic Search|sentence-transformers|
|Similarity |cosine_similarity|
|UI|streamlit|


## Key Cleaning TechniquesCase Standardization:

Converting all characters to lowercase ensures that "Word" and "word" are treated as the same token.
Tokenization: The process of splitting strings into a list of words using nltk.word_tokenize().
This handles punctuation attached to words more effectively than a standard.

 split().Stop Word Removal: Filtering out extremely common words that carry little semantic value.
 