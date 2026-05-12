import math
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lexrank import LexRankSummarizer

lang = input("what is the pdf/docx language?")

def intelligent_summarizer(text, language=lang):
    # 1. Setup Parser
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    
    # 2. Calculate 10% length requirement
    total_sentences = len(parser.document.sentences)
    # math.ceil ensures we are "not less than" 10%
    summary_count = math.ceil(total_sentences * 0.10)
    
    # Safety check: if document is tiny, at least 1 sentence
    if summary_count == 0 and total_sentences > 0:
        summary_count = 1

    # 3. Use LexRank (Best for Main Ideas/Important Concepts)
    summarizer = LexRankSummarizer()
    summary_sentences = summarizer(parser.document, summary_count)
    
    # 4. Format the output
    final_summary = " ".join([str(s) for s in summary_sentences])
    
    return {
        "summary": final_summary,
        "original_sentence_count": total_sentences,
        "summary_sentence_count": summary_count,
        "percentage": (summary_count / total_sentences) * 100 if total_sentences > 0 else 0
    }

# Usage
# result = intelligent_summarizer(your_pdf_text)
# print(f"Summary: {result['summary']}")