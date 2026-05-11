import sumy
from sumy.summarizers.text_rank import TextRankSummarizer
from docx import Document
import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re