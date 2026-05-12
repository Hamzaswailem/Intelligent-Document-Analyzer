import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



# Download necessary data packages
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(raw_text):
    # 1. Lowercase
    text = raw_text.lower()
    
    # 2. Remove special characters and numbers (Regex)
    # This keeps only letters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 3. Tokenization (Breaking sentences into words)
    tokens = word_tokenize(text)
    
    # 4. Remove Stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w not in stop_words]
    
    # 5. Lemmatization (Reducing words to their root form)
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    
    return clean_tokens
