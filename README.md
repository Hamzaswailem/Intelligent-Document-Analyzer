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

## NLP Techniques

Since my text is already tokenized and cleaned we are going to use Sumy because it provides several "tried and true" algorithms that don't require a heavy GPU

input ---> praser ---> Stemmer ---> Summarizer ---> Output


Input: Your cleaned, tokenized text
Parser: Sumy’s PlaintextParser converts text into a "Document" object
Stemmer: Reduces words to their roots (so the algorithm knows "running" and "run" are the same)
Summarizer: An algorithm (like LSA or LexRank) ranks the sentences
Output: The top $N$ most important sentences



### Algorithm used

LexRank : Unsupervised graph-based (like Google's PageRank). It finds sentences that "link" to many others.





# Structure

 <img width="217" height="479" alt="image" src="https://github.com/user-attachments/assets/eee69080-ef7a-42c8-94b3-4b2482a4b7d2" />
