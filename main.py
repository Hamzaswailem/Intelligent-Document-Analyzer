from jiwer import wer
import jiwer
from extractor import pdf_extractor

reference = "hello world"
hypothesis = "hello duck"

error = wer(reference, hypothesis)

print(error)

main_text = "test.pdf"


test=pdf_extractor.pdf_to_text("test2.pdf")



assert jiwer.cer(main_text, test) == 0
