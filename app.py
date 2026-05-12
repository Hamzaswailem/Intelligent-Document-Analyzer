from extractor.pdf_extractor import pdf_to_text 
from extractor.docx_extractor import extract_text_from_docx
from preprocessing.clean_text import clean_text

###File-to-text

pdf = "test2.pdf"
docx = "test.docx"
pdf_txt = pdf_to_text(pdf)

docx_txt = extract_text_from_docx(docx)


###Cleaning proccess

clean_pdf = clean_text(pdf_txt)
clean_docx = clean_text(docx_txt)

#Test

print(clean_pdf)
# print(clean_docx)